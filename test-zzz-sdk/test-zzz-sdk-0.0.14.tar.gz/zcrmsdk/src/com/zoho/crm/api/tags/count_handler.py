import sys

if sys.version > '3':
	from abc import ABC, abstractmethod

	class CountHandler(ABC):
		def __init__(self):
			"""Creates an instance of CountHandler"""
			pass

else:
	from abc import ABCMeta, abstractmethod

	class CountHandler:
		__metaclass__ = ABCMeta

		def __init__(self):
			"""Creates an instance of CountHandler"""
			pass

