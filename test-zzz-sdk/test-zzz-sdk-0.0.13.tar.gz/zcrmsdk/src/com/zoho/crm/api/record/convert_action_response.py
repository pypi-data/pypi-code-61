import sys

if sys.version > '3':
	from abc import ABC, abstractmethod

	class ConvertActionResponse(ABC):
		def __init__(self):
			"""Creates an instance of ConvertActionResponse"""
			pass

else:
	from abc import ABCMeta, abstractmethod

	class ConvertActionResponse:
		__metaclass__ = ABCMeta

		def __init__(self):
			"""Creates an instance of ConvertActionResponse"""
			pass

