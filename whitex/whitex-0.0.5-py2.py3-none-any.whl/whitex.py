"""Main module."""

from whitex.commands import clean


def clean_buffer(*, input_buf, keep_comments):
    return clean(
        input_buf.read(),
        keep_comments=keep_comments,
    )
