import sys

if sys.version > '3':
	from abc import ABC, abstractmethod

	class RecordActionResponse(ABC):
		def __init__(self):
			"""Creates an instance of RecordActionResponse"""
			pass

else:
	from abc import ABCMeta, abstractmethod

	class RecordActionResponse:
		__metaclass__ = ABCMeta

		def __init__(self):
			"""Creates an instance of RecordActionResponse"""
			pass

