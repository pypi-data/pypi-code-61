"""
Exceptions for pyJsConsole.

© Anime no Sekai - 2020
"""

class BrowserError(Exception):
    """
    When the browser isn't available.
    """
    def __init__(self, msg=None):
        self.msg = msg 
    def __str__(self):
        exception_msg = f"\n\n⚠️ ⚠️ ⚠️\n{self.msg}\n"
        return exception_msg

class ReadOnlyError(Exception):
    """
    When the property is read-only.
    """
    def __init__(self, msg=None):
        self.msg = msg 
    def __str__(self):
        exception_msg = f"\n\n⚠️ ⚠️ ⚠️\n{self.msg}\n"
        return exception_msg