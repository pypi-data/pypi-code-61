

class DeviceGroup(object):
	"""Emulated.DeviceGroup class

	An abstract container for emulated device containers.

	Args
	----
	- name (Union[str, type(None)]): Unique name of an object that is the primary key for objects found in  arrays.
	- ports (Union[list[Union[str, type(None)]], type(None)]): One or more port names that the emulated device containers will share.
	- devices (Union[list[Union[Device, type(None)]], type(None)]): One or more emulated device containers.
	"""
	def __init__(self, name=None, ports=None, devices=None):
		if isinstance(name, (str, type(None))) is True:
			self.name = name
		else:
			raise TypeError('name must be an instance of (str, type(None))')
		if isinstance(ports, (list, type(None))) is True:
			self.ports = ports
		else:
			raise TypeError('ports must be an instance of (list, type(None))')
		if isinstance(devices, (list, type(None))) is True:
			self.devices = devices
		else:
			raise TypeError('devices must be an instance of (list, type(None))')


class Device(object):
	"""Emulated.Device class

	An abstract container for emulated protocols.

	Args
	----
	- name (Union[str, type(None)]): Unique name of an object that is the primary key for objects found in  arrays.
	- devices_per_port (Union[float, int, type(None)]): The number of devices that will be created on each port
	- parent (Union[str, type(None)]): The name of a device container or network container that is  the parent of this container.  Use this property to establish a hierarchical relationship between  device containers. 
	- protocols (Union[list[None], type(None)]): The emulated protocols in this device container
	"""
	def __init__(self, name=None, devices_per_port=None, parent=None, protocols=None):
		if isinstance(name, (str, type(None))) is True:
			self.name = name
		else:
			raise TypeError('name must be an instance of (str, type(None))')
		if isinstance(devices_per_port, (float, int, type(None))) is True:
			self.devices_per_port = devices_per_port
		else:
			raise TypeError('devices_per_port must be an instance of (float, int, type(None))')
		if isinstance(parent, (str, type(None))) is True:
			self.parent = parent
		else:
			raise TypeError('parent must be an instance of (str, type(None))')
		if isinstance(protocols, (list, type(None))) is True:
			self.protocols = protocols
		else:
			raise TypeError('protocols must be an instance of (list, type(None))')


class Ethernet(object):
	"""Emulated.Ethernet class

	Emulated ethernet protocol

	Args
	----
	- name (Union[str, type(None)]): Unique name of an object that is the primary key for objects found in  arrays.
	- mac (Union[str, type(None)]): TBD
	- mtu (Union[str, type(None)]): TBD
	"""
	def __init__(self, name=None, mac=None, mtu=None):
		if isinstance(name, (str, type(None))) is True:
			self.name = name
		else:
			raise TypeError('name must be an instance of (str, type(None))')
		if isinstance(mac, (str, type(None))) is True:
			self.mac = mac
		else:
			raise TypeError('mac must be an instance of (str, type(None))')
		if isinstance(mtu, (str, type(None))) is True:
			self.mtu = mtu
		else:
			raise TypeError('mtu must be an instance of (str, type(None))')


class Vlan(object):
	"""Emulated.Vlan class

	Emulated vlan protocol

	Args
	----
	- name (Union[str, type(None)]): Unique name of an object that is the primary key for objects found in  arrays.
	- parent (Union[str, type(None)]): Unique name of an object that is the primary key for objects found in  arrays.
	- tpid (Union[str, type(None)]): Vlan tag protocol identifier.
	- priority (Union[str, type(None)]): Vlan priority.
	- id (Union[str, type(None)]): Vlan id.
	"""
	def __init__(self, name=None, parent=None, tpid=None, priority=None, id=None):
		if isinstance(name, (str, type(None))) is True:
			self.name = name
		else:
			raise TypeError('name must be an instance of (str, type(None))')
		if isinstance(parent, (str, type(None))) is True:
			self.parent = parent
		else:
			raise TypeError('parent must be an instance of (str, type(None))')
		if isinstance(tpid, (str, type(None))) is True:
			self.tpid = tpid
		else:
			raise TypeError('tpid must be an instance of (str, type(None))')
		if isinstance(priority, (str, type(None))) is True:
			self.priority = priority
		else:
			raise TypeError('priority must be an instance of (str, type(None))')
		if isinstance(id, (str, type(None))) is True:
			self.id = id
		else:
			raise TypeError('id must be an instance of (str, type(None))')


class Ipv4(object):
	"""Emulated.Ipv4 class

	Emulated ipv4 protocol

	Args
	----
	- name (Union[str, type(None)]): Unique name of an object that is the primary key for objects found in  arrays.
	- address (Union[str, type(None)]): TBD
	- gateway (Union[str, type(None)]): TBD
	- prefix (Union[str, type(None)]): TBD
	"""
	def __init__(self, name=None, address=None, gateway=None, prefix=None):
		if isinstance(name, (str, type(None))) is True:
			self.name = name
		else:
			raise TypeError('name must be an instance of (str, type(None))')
		if isinstance(address, (str, type(None))) is True:
			self.address = address
		else:
			raise TypeError('address must be an instance of (str, type(None))')
		if isinstance(gateway, (str, type(None))) is True:
			self.gateway = gateway
		else:
			raise TypeError('gateway must be an instance of (str, type(None))')
		if isinstance(prefix, (str, type(None))) is True:
			self.prefix = prefix
		else:
			raise TypeError('prefix must be an instance of (str, type(None))')


class Bgpv4(object):
	"""Emulated.Bgpv4 class

	Emulated bgpv4 protocol

	Args
	----
	- name (Union[str, type(None)]): Unique name of an object that is the primary key for objects found in  arrays.
	- as_number_2_byte (Union[str, type(None)]): TBD
	- dut_as_number_2_byte (Union[str, type(None)]): TBD
	- as_number_4_byte (Union[str, type(None)]): TBD
	- as_number_set_mode (Union[str, type(None)]): TBD
	- type (Union[str, type(None)]): The type of BGP topology.  External BGP (EBGP) is used for BGP links between two or more  Autonomous Systems. Internal BGP (IBGP) is used within a single Autonomous System.
	- hold_time_interval (Union[str, type(None)]): TBD
	- keep_alive_interval (Union[str, type(None)]): TBD
	- graceful_restart (Union[str, type(None)]): TBD
	- authentication (Union[str, type(None)]): TBD
	- ttl (Union[str, type(None)]): TBD
	- dut_ipv4_address (Union[str, type(None)]): TBD
	"""
	def __init__(self, name=None, as_number_2_byte=None, dut_as_number_2_byte=None, as_number_4_byte=None, as_number_set_mode=None, type=None, hold_time_interval=None, keep_alive_interval=None, graceful_restart=None, authentication=None, ttl=None, dut_ipv4_address=None):
		if isinstance(name, (str, type(None))) is True:
			self.name = name
		else:
			raise TypeError('name must be an instance of (str, type(None))')
		if isinstance(as_number_2_byte, (str, type(None))) is True:
			self.as_number_2_byte = as_number_2_byte
		else:
			raise TypeError('as_number_2_byte must be an instance of (str, type(None))')
		if isinstance(dut_as_number_2_byte, (str, type(None))) is True:
			self.dut_as_number_2_byte = dut_as_number_2_byte
		else:
			raise TypeError('dut_as_number_2_byte must be an instance of (str, type(None))')
		if isinstance(as_number_4_byte, (str, type(None))) is True:
			self.as_number_4_byte = as_number_4_byte
		else:
			raise TypeError('as_number_4_byte must be an instance of (str, type(None))')
		if isinstance(as_number_set_mode, (str, type(None))) is True:
			self.as_number_set_mode = as_number_set_mode
		else:
			raise TypeError('as_number_set_mode must be an instance of (str, type(None))')
		if isinstance(type, (str, type(None))) is True:
			self.type = type
		else:
			raise TypeError('type must be an instance of (str, type(None))')
		if isinstance(hold_time_interval, (str, type(None))) is True:
			self.hold_time_interval = hold_time_interval
		else:
			raise TypeError('hold_time_interval must be an instance of (str, type(None))')
		if isinstance(keep_alive_interval, (str, type(None))) is True:
			self.keep_alive_interval = keep_alive_interval
		else:
			raise TypeError('keep_alive_interval must be an instance of (str, type(None))')
		if isinstance(graceful_restart, (str, type(None))) is True:
			self.graceful_restart = graceful_restart
		else:
			raise TypeError('graceful_restart must be an instance of (str, type(None))')
		if isinstance(authentication, (str, type(None))) is True:
			self.authentication = authentication
		else:
			raise TypeError('authentication must be an instance of (str, type(None))')
		if isinstance(ttl, (str, type(None))) is True:
			self.ttl = ttl
		else:
			raise TypeError('ttl must be an instance of (str, type(None))')
		if isinstance(dut_ipv4_address, (str, type(None))) is True:
			self.dut_ipv4_address = dut_ipv4_address
		else:
			raise TypeError('dut_ipv4_address must be an instance of (str, type(None))')
