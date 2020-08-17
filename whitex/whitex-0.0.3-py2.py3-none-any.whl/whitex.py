"""Main module."""

from whitex.commands import clean


def clean_buffer(*, input_buf, output_buf, keep_comments):
    out_string = clean(
        input_buf.read(),
        keep_comments=keep_comments,
    )
    output_buf.write(out_string)
