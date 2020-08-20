def __is_dict(var):
	return isinstance(var, dict)

class ConfigKeyNotExistError(Exception):
	pass

class Config:
	def __init__(self, default, custom):
		self.default = default
		self.custom = custom

	def __setitem__(self, key, value):
		self.custom[key] = value

	def __contains__(self, key):
		return key in self.custom or key in self.default

	def __getitem__(self, key):
		if key in self.custom:
			if __is_dict(self.custom[key]) and key in self.default and __is_dict(self.default[key]):
				return dict(Config(self.default[key], self.custom[key]))
			else:
				return self.custom[key]
		
		if key in self.default:
			return self.default[key]

		raise ConfigKeyNotExistError(f'Key {key} not exist')
	
	def __iter__(self):
		all_keys = set(self.default.keys()).union(set(self.custom.keys()))

		for key in all_keys:
			yield key, self[key]

class MultiConfig(Config):
	def __init__(self, configs, custom):
		default, *configs = configs
		for config in configs:
			default = dict(Config(default, config))

		super().__init__(default, custom)

