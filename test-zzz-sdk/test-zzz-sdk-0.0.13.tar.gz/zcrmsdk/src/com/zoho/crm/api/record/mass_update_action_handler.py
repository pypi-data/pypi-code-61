import sys

if sys.version > '3':
	from abc import ABC, abstractmethod

	class MassUpdateActionHandler(ABC):
		def __init__(self):
			"""Creates an instance of MassUpdateActionHandler"""
			pass

else:
	from abc import ABCMeta, abstractmethod

	class MassUpdateActionHandler:
		__metaclass__ = ABCMeta

		def __init__(self):
			"""Creates an instance of MassUpdateActionHandler"""
			pass

