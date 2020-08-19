import sys

if sys.version > '3':
	from abc import ABC, abstractmethod

	class DeleteActionResponse(ABC):
		def __init__(self):
			"""Creates an instance of DeleteActionResponse"""
			pass

else:
	from abc import ABCMeta, abstractmethod

	class DeleteActionResponse:
		__metaclass__ = ABCMeta

		def __init__(self):
			"""Creates an instance of DeleteActionResponse"""
			pass

