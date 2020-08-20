import sys

if sys.version > '3':
	from abc import ABC, abstractmethod

	class MassUpdateResponse(ABC):
		def __init__(self):
			"""Creates an instance of MassUpdateResponse"""
			pass

else:
	from abc import ABCMeta, abstractmethod

	class MassUpdateResponse:
		__metaclass__ = ABCMeta

		def __init__(self):
			"""Creates an instance of MassUpdateResponse"""
			pass

