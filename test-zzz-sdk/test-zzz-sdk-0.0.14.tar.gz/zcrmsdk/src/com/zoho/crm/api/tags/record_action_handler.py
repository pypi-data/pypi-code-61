import sys

if sys.version > '3':
	from abc import ABC, abstractmethod

	class RecordActionHandler(ABC):
		def __init__(self):
			"""Creates an instance of RecordActionHandler"""
			pass

else:
	from abc import ABCMeta, abstractmethod

	class RecordActionHandler:
		__metaclass__ = ABCMeta

		def __init__(self):
			"""Creates an instance of RecordActionHandler"""
			pass

