import sys

if sys.version > '3':
	from abc import ABC, abstractmethod

	class ActionResponse(ABC):
		def __init__(self):
			"""Creates an instance of ActionResponse"""
			pass

else:
	from abc import ABCMeta, abstractmethod

	class ActionResponse:
		__metaclass__ = ABCMeta

		def __init__(self):
			"""Creates an instance of ActionResponse"""
			pass

