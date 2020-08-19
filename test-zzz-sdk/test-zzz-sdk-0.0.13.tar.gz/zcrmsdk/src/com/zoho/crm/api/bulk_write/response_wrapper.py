import sys

if sys.version > '3':
	from abc import ABC, abstractmethod

	class ResponseWrapper(ABC):
		def __init__(self):
			"""Creates an instance of ResponseWrapper"""
			pass

else:
	from abc import ABCMeta, abstractmethod

	class ResponseWrapper:
		__metaclass__ = ABCMeta

		def __init__(self):
			"""Creates an instance of ResponseWrapper"""
			pass

