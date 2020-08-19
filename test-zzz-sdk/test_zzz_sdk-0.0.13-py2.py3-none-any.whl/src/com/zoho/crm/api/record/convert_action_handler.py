import sys

if sys.version > '3':
	from abc import ABC, abstractmethod

	class ConvertActionHandler(ABC):
		def __init__(self):
			"""Creates an instance of ConvertActionHandler"""
			pass

else:
	from abc import ABCMeta, abstractmethod

	class ConvertActionHandler:
		__metaclass__ = ABCMeta

		def __init__(self):
			"""Creates an instance of ConvertActionHandler"""
			pass

