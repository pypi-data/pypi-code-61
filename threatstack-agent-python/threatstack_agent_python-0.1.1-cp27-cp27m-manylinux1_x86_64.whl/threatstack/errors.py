"""
    Custom Errors
"""

class ThreatstackError(Exception):
   """Base class for other exceptions"""
   pass

class RequestBlockedError(ThreatstackError):
   """Request Blocked Error for sqli"""
   pass   

class ThreatstackStackError(ThreatstackError):
   """Stack Error to get filename, linenumber"""
   pass      