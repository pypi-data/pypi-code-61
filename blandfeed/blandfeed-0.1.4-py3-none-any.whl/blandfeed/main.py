#!/usr/bin/env python3
import asyncio
import json
from pathlib import Path
import socket
import appdirs
import traceback
import base64
import subprocess
import argparse
import datetime
import re
import random

from aiohttp import web
import aiohttp
import dbus
from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop
import nacl.secret
import nacl.utils


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--listen", help="Listen address")
    parser.add_argument("-p", "--publish", help="Publish address (public address)")
    parser.add_argument("-m", "--max-messages", help="Max backlog", default=10)
    args = parser.parse_args()

    here = Path(__file__).parent

    cache = Path(appdirs.user_cache_dir("blandfeed", "rendaw"))
    cache.mkdir(parents=True, exist_ok=True)
    keypath = cache / "key"
    key = None
    try:
        with open(keypath, "rb") as source:
            key = source.read()
    except FileNotFoundError:
        pass
    except:
        traceback.print_exc()
    if key is None:
        key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
        with open(keypath, "wb") as keydest:
            keydest.write(key)
    cipher = nacl.secret.SecretBox(key)

    host, port = args.listen.split(":") if args.listen else None, 8765
    if host is None:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("10.255.255.255", 1))
            host = s.getsockname()[0]
        finally:
            s.close()
    listen = "{}:{}".format(host, port)
    publish = args.publish or listen

    loop = asyncio.get_event_loop()

    queues = []
    messages = []

    # Web server
    def static_send(path, mime, subs):
        def inner(_):
            with open(here / path, "rt", encoding="utf-8") as source:
                t = source.read()
            for k, v in subs.items():
                t = re.sub(k, str(v), t)
            return web.Response(body=t.encode("utf-8"), headers={"Content-Type": mime})

        return inner

    async def ws_send(request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)

        async for msg in ws:
            if msg.type != aiohttp.WSMsgType.TEXT:
                continue
            last = [int(msg.data)]
            break

        try:
            queue = asyncio.Queue(args.max_messages)
            queues.append(queue)

            async def send(message):
                await ws.send_str(
                    base64.urlsafe_b64encode(
                        cipher.encrypt(json.dumps(message).encode("utf-8"))
                    )
                    .decode("utf-8")
                    .rstrip("=")
                )

            async def flush():
                before = True
                m2 = list(messages)
                for message in m2:
                    if before:
                        if message["id"] == last[0]:
                            before = False
                    else:
                        await send(message)
                        last[0] = message["id"]
                if before:  # id never found, assume everything's fresh
                    for message in m2:
                        await send(message)
                        last[0] = message["id"]

            await flush()
            while True:
                await queue.get()
                await flush()
        finally:
            queues.remove(queue)

        return ws

    httpapp = web.Application(debug=True)
    httpapp.add_routes(
        [
            web.get("/", static_send("main.html", "text/html", {"ADDRESS": publish},),),
            web.get("/main.css", static_send("main.css", "text/css", {})),
            web.get(
                "/main.js",
                static_send(
                    "main.js",
                    "application/javascript",
                    {"ADDRESS": publish, "MAX": args.max_messages,},
                ),
            ),
            web.get(
                "/sodium.js", static_send("sodium.js", "application/javascript", {})
            ),
            web.get("/ws", ws_send),
        ]
    )

    # Notification listener
    dbus_loop = GLib.MainLoop()

    def dbus_listen():
        ids = [random.randint(0, 99999999)]

        def handle(_bus, message):
            if message.get_path() != "/org/freedesktop/Notifications":
                return
            (
                app_name,
                _replaces_id,
                _app_icon,
                summary,
                body,
                _actions,
                _hints,
                _expire_timeout,
            ) = message.get_args_list()
            message = {
                str(k): str(v)
                for k, v in dict(name=app_name, summary=summary, body=body).items()
            }
            message["id"] = ids[0]
            ids[0] = ids[0] + 1
            message["date"] = datetime.datetime.now().strftime("%H:%M")
            messages.append(message)
            while len(messages) > args.max_messages:
                messages.pop(0)

            async def wake():
                for queue in queues:
                    await queue.put(True)

            asyncio.run_coroutine_threadsafe(wake(), loop)

        DBusGMainLoop(set_as_default=True)
        bus = dbus.SessionBus()
        bus.add_match_string_non_blocking(
            "eavesdrop=true, interface='org.freedesktop.Notifications', member='Notify'"
        )
        bus.add_message_filter(handle)
        dbus_loop.run()

    # QR code + link
    link = "http://{}/#{}".format(
        publish, base64.urlsafe_b64encode(key).decode("utf-8").rstrip("=")
    )
    print("Open {}".format(link))
    subprocess.check_call(["qrencode", "-t", "UTF8", link])

    # Loopy things
    loop.run_until_complete(loop.create_server(httpapp.make_handler(), host, port))
    loop.run_in_executor(None, dbus_listen)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        dbus_loop.quit()
