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

from aiohttp import web
import dbus
from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop
import nacl.secret
import nacl.utils

static = """
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>{address} feed</title>
        <style>
* {{
    margin: 0;
    padding: 0;
    font-family: sans-serif;
}}
body {{
    display: flex;
    flex-direction: column;
    position: relative;
    align-items: center;
}}
body > div {{
    margin: 4mm;
    width: 10cm;
    max-width: calc(100% - 4mm);
    box-sizing: border-box;
}}
.message {{
    border: 1.5px solid #88AAFF;
    border-radius: 2mm;
    padding: 2mm;
    display: grid;
    grid-template-columns: auto 1fr;
    transform: translate(0%, -100%);
    margin-bottom: 0;
}}
.message.created {{
    transition: transform 0.35s, border-color 600s;
    transform: translate(0%, 0%);
    border-color: #AAAAAA;
}}
.message div {{
    margin: 1mm;
    margin-top: 0;
}}
.message .date {{
    grid-column: 1;
    color: #AAAAAA;
    font-size: 0.9em;
}}
.message .name {{
    grid-column: 2;
    text-align: right;
    font-size: 0.9em;
    font-weight: bold;
}}
.message .summary {{
    grid-column: 1 / span 2;
    whitespace: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    font-size: 0.9em;
    color: #888888;
    max-width: 100%;
}}
.message .body {{
    grid-column: 1 / span 2;
}}
        </style>
    </head>
    <body>
        <script src="/sodium.js"></script>
        <script>
(async () => {{
await sodium.ready;

const key = sodium.from_base64(window.location.hash.substring(1));

const post = node => {{
    document.body.insertBefore(node, document.body.firstChild);
    while (document.body.children.length > {max}) {{
        document.body.lastChild.remove();
    }}

    node.offsetWidth = node.offsetWidth;
    node.classList.add('created');

    window.scrollTo(0, 0);
}};

const connect = () => {{
    const ws = new WebSocket("ws://{address}/ws");
    ws.onmessage = async event => {{
        const predata = sodium.from_base64(event.data);
        const nonce = predata.slice(0, sodium.crypto_secretbox_NONCEBYTES);
        const ciphertext = predata.slice(sodium.crypto_secretbox_NONCEBYTES);
        const data = JSON.parse(new TextDecoder().decode(sodium.crypto_secretbox_open_easy(ciphertext, nonce, key)));

        const container = document.createElement('div');
        container.classList.add('message');
        const date = document.createElement('div');
        date.classList.add('date');
        const now = new Date();
        date.textContent = (
            now.getHours().toString().padStart(2, '0') + ':' +
            now.getMinutes().toString().padStart(2, '0')
        );
        const name = document.createElement('div');
        name.classList.add('name');
        name.textContent = data.name;
        const summary = document.createElement('div');
        summary.classList.add('summary');
        summary.textContent = data.summary;
        const body = document.createElement('div');
        body.classList.add('body');
        body.textContent = data.body;
        if (body.textContent.length > 200) {{
            body.textContent = body.textContent.substring(0, 200) + '...';
        }}
        container.appendChild(date);
        container.appendChild(name);
        container.appendChild(summary);
        container.appendChild(body);

        post(container);
    }};
    ws.onclose = async event => {{
        const line = document.createElement('div');
        line.textContent = 'Lost connection, reconnecting';
        post(line);
        await new Promise(resolve => setTimeout(resolve, 10000));
        connect();
    }};
}};

connect();

}})();
        </script>
    </body>
</html>
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--listen", help="Listen address")
    parser.add_argument("-p", "--publish", help="Publish address (public address)")
    parser.add_argument("-m", "--max-messages", help="Max backlog", default=50)
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

    global static
    static = static.format(address=publish, max=args.max_messages)

    queue = asyncio.Queue(args.max_messages)

    # Web server
    async def http_send(_):
        return web.Response(body=static, headers={"Content-Type": "text/html"})

    async def http_send_sodium(_):
        with open(here / "sodium.js", "rb") as source:
            body = source.read()
        return web.Response(
            body=body, headers={"Content-Type": "application/javascript"}
        )

    async def ws_send(request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)

        while True:
            message = await queue.get()
            await ws.send_str(
                base64.urlsafe_b64encode(
                    cipher.encrypt(json.dumps(message).encode("utf-8"))
                )
                .decode("utf-8")
                .rstrip("=")
            )

        return ws

    httpapp = web.Application(debug=True)
    httpapp.add_routes(
        [
            web.get("/", http_send),
            web.get("/sodium.js", http_send_sodium),
            web.get("/ws", ws_send),
        ]
    )

    # Notification listener
    dbus_loop = GLib.MainLoop()

    def dbus_listen():
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
            asyncio.run_coroutine_threadsafe(queue.put(message), loop)

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
