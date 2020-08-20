import sys

if sys.version > '3':
	from abc import ABC, abstractmethod

	class MassUpdateActionResponse(ABC):
		def __init__(self):
			"""Creates an instance of MassUpdateActionResponse"""
			pass

else:
	from abc import ABCMeta, abstractmethod

	class MassUpdateActionResponse:
		__metaclass__ = ABCMeta

		def __init__(self):
			"""Creates an instance of MassUpdateActionResponse"""
			pass

