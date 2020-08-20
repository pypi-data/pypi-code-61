import sys

if sys.version > '3':
	from abc import ABC, abstractmethod

	class BaseCurrencyActionHandler(ABC):
		def __init__(self):
			"""Creates an instance of BaseCurrencyActionHandler"""
			pass

else:
	from abc import ABCMeta, abstractmethod

	class BaseCurrencyActionHandler:
		__metaclass__ = ABCMeta

		def __init__(self):
			"""Creates an instance of BaseCurrencyActionHandler"""
			pass

