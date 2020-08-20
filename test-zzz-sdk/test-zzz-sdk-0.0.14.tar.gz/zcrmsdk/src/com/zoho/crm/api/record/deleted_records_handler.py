import sys

if sys.version > '3':
	from abc import ABC, abstractmethod

	class DeletedRecordsHandler(ABC):
		def __init__(self):
			"""Creates an instance of DeletedRecordsHandler"""
			pass

else:
	from abc import ABCMeta, abstractmethod

	class DeletedRecordsHandler:
		__metaclass__ = ABCMeta

		def __init__(self):
			"""Creates an instance of DeletedRecordsHandler"""
			pass

