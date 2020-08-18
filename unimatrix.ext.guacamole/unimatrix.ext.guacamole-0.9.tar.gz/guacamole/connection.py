"""Declares :class:`GuacamoleConnection`."""
import asyncio


class GuacamoleConnection:
    """Provides an asynchronous interface with the Guacamole server."""

    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def connect(self, timeout):
        try:
            fut = asyncio.open_connection(self.host, self.port)
            self.reader, self.writer = await asyncio.wait_for(fut, timeout=timeout)
        except asyncio.TimeoutError:    
            # TODO: some cleanup here
            raise

    def recv(self, bufsize):
        return self.reader.read(bufsize)

    def sendall(self, buf):
        self.writer.write(buf)
        return self.writer.drain()

    def close(self):
        self.writer.close()
        return self.writer.wait_closed()
