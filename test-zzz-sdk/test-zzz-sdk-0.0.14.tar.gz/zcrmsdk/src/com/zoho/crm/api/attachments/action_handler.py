import sys

if sys.version > '3':
	from abc import ABC, abstractmethod

	class ActionHandler(ABC):
		def __init__(self):
			"""Creates an instance of ActionHandler"""
			pass

else:
	from abc import ABCMeta, abstractmethod

	class ActionHandler:
		__metaclass__ = ABCMeta

		def __init__(self):
			"""Creates an instance of ActionHandler"""
			pass

