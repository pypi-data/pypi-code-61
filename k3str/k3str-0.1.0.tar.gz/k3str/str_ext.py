import sys

default_encoding = sys.getdefaultencoding()
if hasattr(sys, 'getfilesystemencoding'):
    default_encoding = sys.getfilesystemencoding()


def to_bytes(s, encoding=None):
    """
    Convert str to bytes.  If it is already bytes, do nothing.

    Args:

        s: str or bytes

        encoding(str):
            the encoding to encode str.
            If it is None, system default encoding is used.

    Returns:
        bytes
    """

    if encoding is None:
        encoding = default_encoding

    if isinstance(s, bytes):
        return s

    if isinstance(s, str):
        return bytes(s, encoding)

    return bytes(str(s), encoding)
