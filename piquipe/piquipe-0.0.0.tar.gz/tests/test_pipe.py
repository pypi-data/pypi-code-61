import os

import piquipe

def test_pipe_binary():
    read_fd, write_fd = piquipe.pipe()

    read_stream = os.fdopen(read_fd, mode='rb', buffering=0)
    write_stream = os.fdopen(write_fd, mode='wb', buffering=0)

    input_ = b'''one
    two
    three
    '''

    write_stream.write(input_)
    write_stream.close()
    output = read_stream.read()

    assert output == input_

def test_pipe_text():
    read_fd, write_fd = piquipe.pipe()

    read_stream = os.fdopen(read_fd, mode='r', buffering=1)
    write_stream = os.fdopen(write_fd, mode='w', buffering=1)

    input_ = '''one
    two
    three
    '''

    write_stream.write(input_)
    write_stream.close()
    output = read_stream.read()

    assert output == input_
