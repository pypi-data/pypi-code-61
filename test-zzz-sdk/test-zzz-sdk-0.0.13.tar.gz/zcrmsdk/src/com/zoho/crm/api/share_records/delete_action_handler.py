import sys

if sys.version > '3':
	from abc import ABC, abstractmethod

	class DeleteActionHandler(ABC):
		def __init__(self):
			"""Creates an instance of DeleteActionHandler"""
			pass

else:
	from abc import ABCMeta, abstractmethod

	class DeleteActionHandler:
		__metaclass__ = ABCMeta

		def __init__(self):
			"""Creates an instance of DeleteActionHandler"""
			pass

