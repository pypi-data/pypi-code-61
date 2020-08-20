import sys

if sys.version > '3':
	from abc import ABC, abstractmethod

	class ResponseHandler(ABC):
		def __init__(self):
			"""Creates an instance of ResponseHandler"""
			pass

else:
	from abc import ABCMeta, abstractmethod

	class ResponseHandler:
		__metaclass__ = ABCMeta

		def __init__(self):
			"""Creates an instance of ResponseHandler"""
			pass

