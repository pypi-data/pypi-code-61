import os
import threading
import queue

VERSION = '0.0.0'


def _forward_stream_to_queue(stream, queue_):
    for line in iter(stream.readline, b''):
        queue_.put(line)


def _forward_queue_to_stream(queue_, stream):
    for line in iter(queue_.get, b''):
        stream.write(line)


def _forward_p2q(read_fd, queue_):
    read_stream = os.fdopen(read_fd, mode='rb', buffering=0)
    _forward_stream_to_queue(read_stream, queue_)
    queue_.put(b'')
    read_stream.close()


def _forward_q2p(queue_, write_fd):
    write_stream = os.fdopen(write_fd, mode='wb', buffering=0)
    _forward_queue_to_stream(queue_, write_stream)
    write_stream.close()


def _setup_forward_p2q_thread(read_fd, queue_):
    thread = threading.Thread(target=_forward_p2q, args=(read_fd, queue_), daemon=True)
    thread.start()


def _setup_forward_q2p_thread(queue_, write_fd):
    thread = threading.Thread(target=_forward_q2p, args=(queue_, write_fd), daemon=True)
    thread.start()


def pipe():
    p2qread_fd, p2qwrite_fd = os.pipe()
    q2pread_fd, q2pwrite_fd = os.pipe()
    queue_ = queue.Queue()

    _setup_forward_p2q_thread(p2qread_fd, queue_)
    _setup_forward_q2p_thread(queue_, q2pwrite_fd)

    return q2pread_fd, p2qwrite_fd
