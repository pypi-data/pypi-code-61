import struct
import socket

__all__ = "decode_msg", "encode_msg",


def decode_msg(sock: socket.socket) -> str:
    """
    receive a socket, then calculate the msg length
    :param sock:
    :return:
    """
    token = sock.recv(8)
    msg_length, = struct.unpack('!Q', token)
    msg = sock.recv(msg_length)
    return msg.decode("utf-8")


def encode_msg(msg: str) -> bytes:
    """
    get a msg-bytes length and calculate teh token
    :param msg:
    :return:
    """
    msg = msg.encode("utf-8")
    msg_length = len(msg)
    token = struct.pack("!Q", msg_length)
    return token + msg
