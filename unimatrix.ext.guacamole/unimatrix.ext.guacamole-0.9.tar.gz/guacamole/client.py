"""
The MIT License (MIT)

Copyright (c)   2014 rescale
                2014 - 2016 Mohab Usama
"""
import socket
import logging

from guacamole import logger as guac_logger
from guacamole.connection import GuacamoleConnection
from guacamole.exceptions import GuacamoleError
from guacamole.instruction import INST_TERM
from guacamole.instruction import GuacamoleInstruction as Instruction

# supported protocols
PROTOCOLS = ('vnc', 'rdp', 'ssh')

PROTOCOL_NAME = 'guacamole'

BUF_LEN = 4096


class GuacamoleClient(object):
    """Guacamole Client class."""

    def __init__(self, host, port, timeout=20, debug=False, logger=None):
        """
        Guacamole Client class. This class can handle communication with guacd
        server.

        :param host: guacd server host.

        :param port: guacd server port.

        :param timeout: socket connection timeout.

        :param debug: if True, default logger will switch to Debug level.
        """
        self.host = host
        self.port = port
        self.timeout = timeout

        self._client = None

        # handshake established?
        self.connected = False

        # Receiving buffer
        self._buffer = bytearray()

        # Client ID
        self._id = None

        self.logger = guac_logger
        if logger:
            self.logger = logger

        if debug:
            self.logger.setLevel(logging.DEBUG)

        self.client = GuacamoleConnection(self.host, self.port)

    @property
    def id(self):
        """Return client id"""
        return self._id

    async def close(self):
        """
        Terminate connection with Guacamole guacd server.
        """
        await self.client.close()
        self._client = None
        self.connected = False
        self.logger.debug('Connection closed.')

    async def receive(self):
        """
        Receive instructions from Guacamole guacd server.
        """
        start = 0

        while True:
            idx = self._buffer.find(INST_TERM.encode(), start)
            if idx != -1:
                # instruction was fully received!
                line = self._buffer[:idx + 1].decode()
                self._buffer = self._buffer[idx + 1:]
                self.logger.debug('Received instruction: %s' % line)
                return line
            else:
                start = len(self._buffer)
                # we are still waiting for instruction termination
                buf = await self.client.recv(BUF_LEN)
                if not buf:
                    # No data recieved, connection lost?!
                    await self.close()
                    self.logger.debug(
                        'Failed to receive instruction. Closing.')
                    return None
                self._buffer.extend(buf)

    async def send(self, data):
        """
        Send encoded instructions to Guacamole guacd server.
        """
        self.logger.debug('Sending data: %s' % data)
        return await self.client.sendall(data.encode())

    async def read_instruction(self):
        """
        Read and decode instruction.
        """
        self.logger.debug('Reading instruction.')
        buf = await self.receive()
        return Instruction.load(buf)

    async def send_instruction(self, instruction):
        """
        Send instruction after encoding.
        """
        self.logger.debug('Sending instruction: %s' % str(instruction))
        return await self.send(instruction.encode())

    async def handshake(self, protocol='vnc', width=1024, height=768, dpi=96,
                  audio=None, video=None, image=None, **kwargs):
        """
        Establish connection with Guacamole guacd server via handshake.

        """
        if protocol not in PROTOCOLS and 'connectionid' not in kwargs:
            self.logger.debug('Invalid protocol: %s '
                              'and no connectionid provided' % protocol)
            raise GuacamoleError('Cannot start Handshake. '
                                 'Missing protocol or connectionid.')

        await self.client.connect(kwargs.pop('timeout', 5.0))
        self.logger.debug('Client connected with guacd server (%s, %s, %s)'
                          % (self.host, self.port, self.timeout))
        if audio is None:
            audio = list()

        if video is None:
            video = list()

        if image is None:
            image = list()

        # 1. Send 'select' instruction
        self.logger.debug('Send `select` instruction.')

        # if connectionid is provided - connect to existing connectionid
        if 'connectionid' in kwargs:
            await self.send_instruction(Instruction('select',
                                              kwargs.get('connectionid')))
        else:
            await self.send_instruction(Instruction('select', protocol))

        # 2. Receive `args` instruction
        instruction = await self.read_instruction()
        self.logger.debug('Expecting `args` instruction, received: %s'
                          % str(instruction))

        if not instruction:
            await self.close()
            raise GuacamoleError(
                'Cannot establish Handshake. Connection Lost!')

        if instruction.opcode != 'args':
            await self.close()
            raise GuacamoleError(
                'Cannot establish Handshake. Expected opcode `args`, '
                'received `%s` instead.' % instruction.opcode)

        # 3. Respond with size, audio & video support
        self.logger.debug('Send `size` instruction (%s, %s, %s)'
                          % (width, height, dpi))
        await self.send_instruction(Instruction('size', width, height, dpi))

        self.logger.debug('Send `audio` instruction (%s)' % audio)
        await self.send_instruction(Instruction('audio', *audio))

        self.logger.debug('Send `video` instruction (%s)' % video)
        await self.send_instruction(Instruction('video', *video))

        self.logger.debug('Send `image` instruction (%s)' % image)
        await self.send_instruction(Instruction('image', *image))

        # 4. Send `connect` instruction with proper values
        connection_args = [
            kwargs.get(arg.replace('-', '_'), '') for arg in instruction.args
        ]

        self.logger.debug('Send `connect` instruction (%s)' % connection_args)
        await self.send_instruction(Instruction('connect', *connection_args))

        # 5. Receive ``ready`` instruction, with client ID.
        instruction = await self.read_instruction()
        self.logger.debug('Expecting `ready` instruction, received: %s'
                          % str(instruction))

        if instruction.opcode != 'ready':
            self.logger.warning(
                'Expected `ready` instruction, received: %s instead')

        if instruction.args:
            self._id = instruction.args[0]
            self.logger.debug(
                'Established connection with client id: %s' % self.id)

        self.logger.debug('Handshake completed.')
        self.connected = True
