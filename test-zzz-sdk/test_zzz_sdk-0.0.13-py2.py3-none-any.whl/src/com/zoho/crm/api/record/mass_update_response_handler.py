import sys

if sys.version > '3':
	from abc import ABC, abstractmethod

	class MassUpdateResponseHandler(ABC):
		def __init__(self):
			"""Creates an instance of MassUpdateResponseHandler"""
			pass

else:
	from abc import ABCMeta, abstractmethod

	class MassUpdateResponseHandler:
		__metaclass__ = ABCMeta

		def __init__(self):
			"""Creates an instance of MassUpdateResponseHandler"""
			pass

