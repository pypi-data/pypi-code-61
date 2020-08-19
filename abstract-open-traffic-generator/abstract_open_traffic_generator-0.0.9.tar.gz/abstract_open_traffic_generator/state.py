

class Config(object):
	"""State.Config class

	placeholder

	Args
	----
	- state (Union[str, type(None)]): TBD
	- ports (Union[list[Union[Port, type(None)]], type(None)]): TBD
	- devices (Union[list[Union[DeviceGroup, type(None)]], type(None)]): TBD
	- flows (Union[list[Union[Flow, type(None)]], type(None)]): TBD
	"""
	def __init__(self, state=None, ports=None, devices=None, flows=None):
		if isinstance(state, (str, type(None))) is True:
			self.state = state
		else:
			raise TypeError('state must be an instance of (str, type(None))')
		if isinstance(ports, (list, type(None))) is True:
			self.ports = ports
		else:
			raise TypeError('ports must be an instance of (list, type(None))')
		if isinstance(devices, (list, type(None))) is True:
			self.devices = devices
		else:
			raise TypeError('devices must be an instance of (list, type(None))')
		if isinstance(flows, (list, type(None))) is True:
			self.flows = flows
		else:
			raise TypeError('flows must be an instance of (list, type(None))')


class Flow(object):
	"""State.Flow class

	Request for the traffic generator to move flows to a specific state.

	Args
	----
	- state (Union[str, type(None)]): The requested state of the flows.
	- flows (Union[list[Union[str, type(None)]], type(None)]): The unique names of flow objects.
	"""
	def __init__(self, state=None, flows=None):
		if isinstance(state, (str, type(None))) is True:
			self.state = state
		else:
			raise TypeError('state must be an instance of (str, type(None))')
		if isinstance(flows, (list, type(None))) is True:
			self.flows = flows
		else:
			raise TypeError('flows must be an instance of (list, type(None))')


class Port(object):
	"""State.Port class

	Request for the traffic generator to move ports to a specific state.

	Args
	----
	- state (Union[str, type(None)]): The requested state of the port.
	- flows (Union[list[Union[str, type(None)]], type(None)]): The unique names of port objects.
	"""
	def __init__(self, state=None, flows=None):
		if isinstance(state, (str, type(None))) is True:
			self.state = state
		else:
			raise TypeError('state must be an instance of (str, type(None))')
		if isinstance(flows, (list, type(None))) is True:
			self.flows = flows
		else:
			raise TypeError('flows must be an instance of (list, type(None))')


class Capture(object):
	"""State.Capture class

	placeholder

	Args
	----
	- requested_state (Union[str, type(None)]): TBD
	- captures (Union[list[Union[str, type(None)]], type(None)]): The names of capture objects.
	"""
	def __init__(self, requested_state=None, captures=None):
		if isinstance(requested_state, (str, type(None))) is True:
			self.requested_state = requested_state
		else:
			raise TypeError('requested_state must be an instance of (str, type(None))')
		if isinstance(captures, (list, type(None))) is True:
			self.captures = captures
		else:
			raise TypeError('captures must be an instance of (list, type(None))')


class Desired(object):
	"""State.Desired class

	The desired state of the traffic generator 

	Args
	----
	- configuration (Union[Config, type(None)]): placeholder
	- traffic (Union[Flow, type(None)]): Request for the traffic generator to move flows to a specific state.
	- capture (Union[Capture, type(None)]): placeholder
	"""
	def __init__(self, configuration=None, traffic=None, capture=None):
		from abstract_open_traffic_generator.state import Config
		from abstract_open_traffic_generator.state import Flow
		from abstract_open_traffic_generator.state import Capture
		if isinstance(configuration, (Config, type(None))) is True:
			self.configuration = configuration
		else:
			raise TypeError('configuration must be an instance of (Config, type(None))')
		if isinstance(traffic, (Flow, type(None))) is True:
			self.traffic = traffic
		else:
			raise TypeError('traffic must be an instance of (Flow, type(None))')
		if isinstance(capture, (Capture, type(None))) is True:
			self.capture = capture
		else:
			raise TypeError('capture must be an instance of (Capture, type(None))')


class Actual(object):
	"""State.Actual class

	The desired and actual state of the traffic generator

	Args
	----
	- states (Union[str, type(None)]): TBD
	- flow (Union[list[Union[str, type(None)]], type(None)]): A list of configured flow names If the list is empty the type will apply to all configured flows
	- capture (Union[float, int, type(None)]): The number of seconds to wait for all the flows to be in the specified state
	"""
	def __init__(self, states=None, flow=None, capture=None):
		if isinstance(states, (str, type(None))) is True:
			self.states = states
		else:
			raise TypeError('states must be an instance of (str, type(None))')
		if isinstance(flow, (list, type(None))) is True:
			self.flow = flow
		else:
			raise TypeError('flow must be an instance of (list, type(None))')
		if isinstance(capture, (float, int, type(None))) is True:
			self.capture = capture
		else:
			raise TypeError('capture must be an instance of (float, int, type(None))')
