# Copyright (c) 2020 Arda Seremet <ardaseremet@outlook.com>

from ProgettiHWSW.api import API
from ProgettiHWSW.relay import Relay
from ProgettiHWSW.input import Input

class ProgettiHWSWAPI:
	"""Class to communicate with ProgettiHWSW boards."""

	def __init__(self, ip: str):
		"""Initialize the API and return the corresponding object class."""
		self.api = API(f"http://{ip}")
		self.ip = ip

	def get_relay(self, relay_number: int, relay_mode: str = "bistable") -> Relay:
		"""Return the Relay class."""
		return Relay(self.api, relay_number, relay_mode)

	def get_input(self, input_number: int) -> Input:
		"""Return the Input class."""
		return Input(self.api, input_number)