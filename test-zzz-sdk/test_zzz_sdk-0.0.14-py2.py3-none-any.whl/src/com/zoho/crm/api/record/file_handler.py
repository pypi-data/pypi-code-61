import sys

if sys.version > '3':
	from abc import ABC, abstractmethod

	class FileHandler(ABC):
		def __init__(self):
			"""Creates an instance of FileHandler"""
			pass

else:
	from abc import ABCMeta, abstractmethod

	class FileHandler:
		__metaclass__ = ABCMeta

		def __init__(self):
			"""Creates an instance of FileHandler"""
			pass

