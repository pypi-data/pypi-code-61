import sys

if sys.version > '3':
	from abc import ABC, abstractmethod

	class DownloadHandler(ABC):
		def __init__(self):
			"""Creates an instance of DownloadHandler"""
			pass

else:
	from abc import ABCMeta, abstractmethod

	class DownloadHandler:
		__metaclass__ = ABCMeta

		def __init__(self):
			"""Creates an instance of DownloadHandler"""
			pass

