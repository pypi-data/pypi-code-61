class Speed:
	def __init__(self, unit):
		self.unit = unit

	def defUnit(my_unit):
		unit = speedUnits(my_unit)
		return unit 

	def calculateSpeed(unit, distance, time):
		try:
			distance_title = 'distance'
			time_title = 'time'
			get_unit = speedUnits(unit)
			if isinstance(distance, int) or isinstance(distance, float):
				if isinstance(time, int) or isinstance(time, float):
					if isinstance(get_unit, str):  		
						speed_calculation = float(distance / time)
						print_speed_claculation =  str(speed_calculation) + ' ' + get_unit
						print(f'Speed has been calculated and stored successfully: {print_speed_claculation} ')
						return print_speed_claculation
				else: 
					print(f"It seems you have entered unreal values: in '{time_title}': {time} value, try again!")
			else: 
				print(f"It seems you have entered unreal values in '{distance_title}' : {distance} value, try again!")
		except Exception:
			print('There must be something wrong, try again!')

def speedUnits(select_value = 'none'):
	try:
		speed_units = {
			'ms' : 'meter per second', 
		  'cmhr' : 'centimeter per hour', 
		   'cmm' : 'centimeter per minute', 
		   'cms' : 'centimeter per second', 
		  'fthr' : 'foot per hour', 
		 'ftmin' :  'foot per minute', 
		  'fts'  :  'foot per second', 
		  'kmhr' :  'kilometer per hour', 
		  'kmmin':  'kilometer per minute', 
		  'kms'  :  'kilometer per second', 
		  'mhr'  :  'meter per hour', 
		  'mmin' :  'meter per minute', 
		  'ms'   : 'meter per second', 
		  'mihr' : 'mile per hour', 
		  'mimin': 'mile per minute', 
		  'mis'  :  'mile per second', 
		  'nmihr': 'nautical mile per hour', 
		 'nmimin': 'nautical mile per minute', 
		  'nmis' : 'nautical mile per second', 
				}

		if select_value != 'none': 
			return_value = speed_units.get(select_value, 'No value has been found in speed units')
			if return_value == 'No value has been found in speed units':
				print(return_value)
				print('Try again with these values: \n')
				speedUnits()
				print('\nNo value has been returned yet!')
				return False
			else: 	
				return return_value
		elif select_value == 'none': 
			count = 1
			for i in speed_units:
				print(str(count) + ' : ' + "\u0332".join(i) + ' : ' + speed_units[i])
				count += 1
	except Exception: 
		print('There must be something wrong, try again!')

def speedConvertor(select_value, select_convert_value, select_num):
	try:
		converted_value = '' 
		if select_value:
			s_value = select_value
			if select_convert_value: 
				s_c_value = select_convert_value
				if select_num <= 0:
					print(f'Your number {select_num} cannot be converted, try again')
					return False
				elif s_value == "meter per second" and s_c_value == "kilometer per hour": 
					converted_value = float(select_num * 3600) / 1000
					return converted_value
				elif s_value == "kilometer per hour" and s_c_value == "meter per second": 
					 converted_value = float(select_num / 3600) * 1000
					 return converted_value 
				elif s_value == "meter per second" and s_c_value == "centimeter per hour": 
					converted_value = float(select_num * 3600) * 100
					return converted_value
				elif s_value == "centimeter per hour" and s_c_value == "meter per second": 
					converted_value = float(select_num / 3600) / 100
					return converted_value
				elif s_value == "meter per second" and s_c_value == "centimeter per minute": 
					converted_value = float(select_num * 60) * 100
					return converted_value
				elif s_value == "centimeter per minute" and s_c_value == "meter per second": 
					converted_value = float(select_num / 60) / 100
					return converted_value
				elif s_value == "meter per second" and s_c_value == "centimeter per second": 
					converted_value = float(select_num * 1) * 100
					return converted_value
				elif s_value == "centimeter per second" and s_c_value == "meter per second": 
					converted_value = float(select_num / 1) / 100
					return converted_value
				elif s_value == "meter per second" and s_c_value == "foot per hour": 
					converted_value = float(select_num * 3600) * 3.2808399
					return converted_value
				elif s_value == "foot per hour" and s_c_value == "meter per second": 
					converted_value = float(select_num / 3600) / 3.2808399
					return converted_value
				elif s_value == "meter per second" and s_c_value == "foot per minute": 
					converted_value = float(select_num * 60) * 3.2808399
					return converted_value
				elif s_value == "foot per minute" and s_c_value == "meter per second": 
					converted_value = float(select_num / 60) / 3.2808399
					return converted_value
				elif s_value == "meter per second" and s_c_value == "foot per second": 
					converted_value = float(select_num * 1) * 3.2808399
					return converted_value
				elif s_value == "foot per second" and s_c_value == "meter per second": 
					converted_value = float(select_num / 1) / 3.2808399
					return converted_value
				elif s_value == "meter per second" and s_c_value == "kilometer per minute": 
					converted_value = float(select_num * 60) / 1000
					return converted_value
				elif s_value == "kilometer per minute" and s_c_value == "meter per second": 
					converted_value = float(select_num / 60) * 1000
					return converted_value
				elif s_value == "meter per second" and s_c_value == "kilometer per second": 
					converted_value = float(select_num / 1) / 1000
					return converted_value
				elif s_value == "kilometer per second" and s_c_value == "meter per second": 
					converted_value = float(select_num / 1) * 1000
					return converted_value
				elif s_value == "meter per second" and s_c_value == "meter per hour": 
					converted_value = float(select_num * 3600) / 1
					return converted_value
				elif s_value == "meter per hour" and s_c_value == "meter per second": 
					converted_value = float(select_num / 3600) / 1
					return converted_value
				elif s_value == "meter per second" and s_c_value == "meter per minute": 
					converted_value = float(select_num * 60) / 1
					return converted_value	
				elif s_value == "meter per minute" and s_c_value == "meter per second": 
					converted_value = float(select_num / 60) / 1
					return converted_value		
				elif s_value == "meter per second" and s_c_value == "mile per hour": 
					converted_value = float(select_num * 3600) * 0.000621371192
					return converted_value	
				elif s_value == "mile per hour" and s_c_value == "meter per second": 
					converted_value = float(select_num / 3600) / 0.000621371192
					return converted_value	
				elif s_value == "meter per second" and s_c_value == "mile per minute": 
					converted_value = float(select_num * 60) * 0.000621371192
					return converted_value	
				elif s_value == "mile per minute" and s_c_value == "meter per second": 
					converted_value = float(select_num / 60) / 0.000621371192
					return converted_value	
				elif s_value == "meter per second" and s_c_value == "mile per second": 
					converted_value = float(select_num / 1) * 0.000621371192
					return converted_value	
				elif s_value == "mile per second" and s_c_value == "meter per second": 
					converted_value = float(select_num / 1) / 0.000621371192
					return converted_value	
				elif s_value == "meter per second" and s_c_value == "nautical mile per hour": 
					converted_value = float(select_num * 3600 ) / 1852
					return converted_value	
				elif s_value == "nautical mile per hour" and s_c_value == "meter per second": 
					converted_value = float(select_num / 3600 ) * 1852
					return converted_value	
				elif s_value == "meter per second" and s_c_value == "nautical mile per minute": 
					converted_value = float(select_num * 60 ) / 1852
					return converted_value	
				elif s_value == "nautical mile per minute" and s_c_value == "meter per second": 
					converted_value = float(select_num / 60 ) * 1852
					return converted_value
				elif s_value == "meter per second" and s_c_value == "nautical mile per second": 
					converted_value = float(select_num / 1 ) / 1852
					return converted_value
				elif s_value == "nautical mile per second" and s_c_value == "meter per second": 
					converted_value = float(select_num / 1 ) * 1852
					return converted_value	
				elif s_value == "centimeter per hour" and s_c_value == "centimeter per minute": 
					converted_value = float(select_num / 60 ) / 1
					return converted_value	
				elif s_value == "centimeter per minute" and s_c_value == "centimeter per hour": 
					converted_value = float(select_num * 60 ) / 1
					return converted_value
				elif s_value == "centimeter per hour" and s_c_value == "centimeter per second": 
					converted_value = float(select_num / 3600 ) / 1
					return converted_value	
				elif s_value == "centimeter per second" and s_c_value == "centimeter per hour": 
					converted_value = float(select_num * 3600 ) / 1
					return converted_value	
				elif s_value == "centimeter per hour" and s_c_value == "foot per hour": 
					converted_value = float(select_num / 1) / 30.48
					return converted_value
				elif s_value == "foot per hour" and s_c_value == "centimeter per hour": 
					converted_value = float(select_num / 1) * 30.48
					return converted_value
				elif s_value == "centimeter per hour" and s_c_value == "foot per minute": 
					converted_value = float(select_num / 60) / 30.48
					return converted_value
				elif s_value == "foot per minute" and s_c_value == "centimeter per hour": 
					converted_value = float(select_num * 60) * 30.48
					return converted_value
				elif s_value == "centimeter per hour" and s_c_value == "foot per second": 
					converted_value = float(select_num / 3600) / 30.48
					return converted_value
				elif s_value == "foot per second" and s_c_value == "centimeter per hour": 
					converted_value = float(select_num * 3600) * 30.48
					return converted_value
				elif s_value == "centimeter per hour" and s_c_value == "kilometer per hour": 
					converted_value = float(select_num / 1) / 100000
					return converted_value
				elif s_value == "kilometer per hour" and s_c_value == "centimeter per hour": 
					converted_value = float(select_num / 1) * 100000
					return converted_value
				elif s_value == "centimeter per hour" and s_c_value == "kilometer per minute": 
					converted_value = float(select_num / 60) / 100000
					return converted_value
				elif s_value == "kilometer per minute" and s_c_value == "centimeter per hour": 
					converted_value = float(select_num * 60) * 100000
					return converted_value
				elif s_value == "centimeter per hour" and s_c_value == "kilometer per second": 
					converted_value = float(select_num / 3600) / 100000
					return converted_value
				elif s_value == "kilometer per second" and s_c_value == "centimeter per hour": 
					converted_value = float(select_num * 3600) * 100000
					return converted_value
				elif s_value == "centimeter per hour" and s_c_value == "meter per hour": 
					converted_value = float(select_num / 1) / 100
					return converted_value
				elif s_value == "meter per hour" and s_c_value == "centimeter per hour": 
					converted_value = float(select_num / 1) * 100
					return converted_value
				elif s_value == "centimeter per hour" and s_c_value == "meter per minute": 
					converted_value = float(select_num / 60) / 100
					return converted_value
				elif s_value == "meter per minute" and s_c_value == "centimeter per hour": 
					converted_value = float(select_num * 60) * 100
					return converted_value
				elif s_value == "centimeter per hour" and s_c_value == "mile per hour": 
					converted_value = float(select_num / 1) * 0.00000621371
					return converted_value
				elif s_value == "mile per hour" and s_c_value == "centimeter per hour": 
					converted_value = float(select_num / 1) / 0.00000621371
					return converted_value
				elif s_value == "centimeter per hour" and s_c_value == "mile per minute": 
					converted_value = float(select_num / 60) * 0.00000621371
					return converted_value
				elif s_value == "mile per minute" and s_c_value == "centimeter per hour": 
					converted_value = float(select_num * 60) / 0.00000621371
					return converted_value
				elif s_value == "centimeter per hour" and s_c_value == "mile per second": 
					converted_value = float(select_num / 3600) * 0.00000621371
					return converted_value
				elif s_value == "mile per second" and s_c_value == "centimeter per hour": 
					converted_value = float(select_num * 3600) / 0.00000621371
					return converted_value
				elif s_value == "centimeter per hour" and s_c_value == "nautical mile per hour": 
					converted_value = float(select_num / 1) * 0.0000053996
					return converted_value
				elif s_value == "nautical mile per hour" and s_c_value == "centimeter per hour": 
					converted_value = float(select_num / 1) / 0.0000053996
					return converted_value
				elif s_value == "centimeter per hour" and s_c_value == "nautical mile per minute": 
					converted_value = float(select_num / 60) * 0.0000053996
					return converted_value
				elif s_value == "nautical mile per minute" and s_c_value == "centimeter per hour": 
					converted_value = float(select_num * 60) / 0.0000053996
					return converted_value
				elif s_value == "centimeter per hour" and s_c_value == "nautical mile per second": 
					converted_value = float(select_num / 3600) * 0.0000053996
					return converted_value
				elif s_value == "nautical mile per second" and s_c_value == "centimeter per hour": 
					converted_value = float(select_num * 3600) * 0.0000053996
					return converted_value
				elif s_value == "centimeter per minute" and s_c_value == "centimeter per second": 
					converted_value = float(select_num / 60) / 1
					return converted_value
				elif s_value == "centimeter per second" and s_c_value == "centimeter per minute": 
					converted_value = float(select_num * 60) / 1
					return converted_value
				elif s_value == "centimeter per minute" and s_c_value == "foot per hour": 
					converted_value = float(select_num * 60) / 30.48
					return converted_value
				elif s_value == "foot per hour" and s_c_value == "centimeter per minute": 
					converted_value = float(select_num / 60) * 30.48
					return converted_value
				elif s_value == "centimeter per minute" and s_c_value == "foot per minute": 
					converted_value = float(select_num / 1) / 30.48
					return converted_value
				elif s_value == "foot per minute" and s_c_value == "centimeter per minute": 
					converted_value = float(select_num / 1) * 30.48
					return converted_value
				elif s_value == "centimeter per minute" and s_c_value == "foot per second": 
					converted_value = float(select_num / 60) / 30.48
					return converted_value
				elif s_value == "foot per second" and s_c_value == "centimeter per minute": 
					converted_value = float(select_num * 60) * 30.48
					return converted_value
				elif s_value == "centimeter per minute" and s_c_value == "kilometer per hour": 
					converted_value = float(select_num * 60) / 100000
					return converted_value
				elif s_value == "kilometer per hour" and s_c_value == "centimeter per minute": 
					converted_value = float(select_num / 60) * 100000
					return converted_value
				elif s_value == "centimeter per minute" and s_c_value == "kilometer per minute": 
					converted_value = float(select_num / 1) / 100000
					return converted_value
				elif s_value == "kilometer per minute" and s_c_value == "centimeter per minute": 
					converted_value = float(select_num / 1) * 100000
					return converted_value
				elif s_value == "centimeter per minute" and s_c_value == "kilometer per second": 
					converted_value = float(select_num / 60) / 100000
					return converted_value
				elif s_value == "kilometer per second" and s_c_value == "centimeter per minute": 
					converted_value = float(select_num * 60) * 100000
					return converted_value
				elif s_value == "centimeter per minute" and s_c_value == "meter per hour": 
					converted_value = float(select_num * 60) / 100
					return converted_value
				elif s_value == "meter per hour" and s_c_value == "centimeter per minute": 
					converted_value = float(select_num / 60) * 100
					return converted_value
				elif s_value == "centimeter per minute" and s_c_value == "meter per minute": 
					converted_value = float(select_num / 1) / 100
					return converted_value
				elif s_value == "meter per minute" and s_c_value == "centimeter per minute": 
					converted_value = float(select_num / 1) * 100
					return converted_value
				elif s_value == "centimeter per minute" and s_c_value == "mile per hour": 
					converted_value = float(select_num * 60) * 0.00000621371
					return converted_value
				elif s_value == "mile per hour" and s_c_value == "centimeter per minute": 
					converted_value = float(select_num / 60) / 0.00000621371
					return converted_value
				elif s_value == "centimeter per minute" and s_c_value == "mile per minute": 
					converted_value = float(select_num / 1) * 0.00000621371
					return converted_value
				elif s_value == "mile per minute" and s_c_value == "centimeter per minute": 
					converted_value = float(select_num / 1) / 0.00000621371
					return converted_value
				elif s_value == "centimeter per minute" and s_c_value == "mile per second": 
					converted_value = float(select_num / 60) * 0.00000621371
					return converted_value
				elif s_value == "mile per second" and s_c_value == "centimeter per minute": 
					converted_value = float(select_num * 60) / 0.00000621371
					return converted_value
				elif s_value == "centimeter per minute" and s_c_value == "nautical mile per hour": 
					converted_value = float(select_num * 60) * 0.0000053996
					return converted_value
				elif s_value == "nautical mile per hour" and s_c_value == "centimeter per minute": 
					converted_value = float(select_num / 60) / 0.0000053996
					return converted_value
				elif s_value == "centimeter per minute" and s_c_value == "nautical mile per minute": 
					converted_value = float(select_num / 1) * 0.0000053996
					return converted_value
				elif s_value == "nautical mile per minute" and s_c_value == "centimeter per minute": 
					converted_value = float(select_num / 1) / 0.0000053996
					return converted_value
				elif s_value == "centimeter per minute" and s_c_value == "nautical mile per second": 
					converted_value = float(select_num / 60) * 0.0000053996
					return converted_value
				elif s_value == "nautical mile per second" and s_c_value == "centimeter per minute": 
					converted_value = float(select_num * 60) / 0.0000053996
					return converted_value
				elif s_value == "centimeter per second" and s_c_value == "foot per hour": 
					converted_value = float(select_num * 3600) / 30.48
					return converted_value
				elif s_value == "foot per hour" and s_c_value == "centimeter per second": 
					converted_value = float(select_num / 3600) * 30.48
					return converted_value
				elif s_value == "centimeter per second" and s_c_value == "foot per minute": 
					converted_value = float(select_num * 60) / 30.48
					return converted_value
				elif s_value == "foot per minute" and s_c_value == "centimeter per second": 
					converted_value = float(select_num / 60) * 30.48
					return converted_value
				elif s_value == "centimeter per second" and s_c_value == "foot per second": 
					converted_value = float(select_num / 1) / 30.48
					return converted_value
				elif s_value == "foot per second" and s_c_value == "centimeter per second": 
					converted_value = float(select_num / 1) * 30.48
					return converted_value
				elif s_value == "centimeter per second" and s_c_value == "kilometer per hour": 
					converted_value = float(select_num * 3600) / 100000
					return converted_value
				elif s_value == "kilometer per hour" and s_c_value == "centimeter per second": 
					converted_value = float(select_num / 3600) * 100000
					return converted_value
				elif s_value == "centimeter per second" and s_c_value == "kilometer per minute": 
					converted_value = float(select_num * 60) / 100000
					return converted_value
				elif s_value == "kilometer per minute" and s_c_value == "centimeter per second": 
					converted_value = float(select_num / 60) * 100000
					return converted_value
				elif s_value == "centimeter per second" and s_c_value == "kilometer per second": 
					converted_value = float(select_num / 1) / 100000
					return converted_value
				elif s_value == "kilometer per second" and s_c_value == "centimeter per second": 
					converted_value = float(select_num / 1) * 100000
					return converted_value
				elif s_value == "centimeter per second" and s_c_value == "meter per hour": 
					converted_value = float(select_num * 3600) / 100
					return converted_value
				elif s_value == "meter per hour" and s_c_value == "centimeter per second": 
					converted_value = float(select_num / 3600) * 100
					return converted_value
				elif s_value == "centimeter per second" and s_c_value == "meter per minute": 
					converted_value = float(select_num * 60) / 100
					return converted_value
				elif s_value == "meter per minute" and s_c_value == "centimeter per second": 
					converted_value = float(select_num / 60) * 100
					return converted_value
				elif s_value == "centimeter per second" and s_c_value == "mile per hour": 
					converted_value = float(select_num * 3600) * 0.00000621371
					return converted_value
				elif s_value == "mile per hour" and s_c_value == "centimeter per second": 
					converted_value = float(select_num / 3600) / 0.00000621371
					return converted_value
				elif s_value == "centimeter per second" and s_c_value == "mile per minute": 
					converted_value = float(select_num * 60) * 0.00000621371
					return converted_value
				elif s_value == "mile per minute" and s_c_value == "centimeter per second": 
					converted_value = float(select_num / 60) / 0.00000621371
					return converted_value
				elif s_value == "centimeter per second" and s_c_value == "mile per second": 
					converted_value = float(select_num / 1) * 0.00000621371
					return converted_value
				elif s_value == "mile per second" and s_c_value == "centimeter per second": 
					converted_value = float(select_num / 1) / 0.00000621371
					return converted_value
				elif s_value == "centimeter per second" and s_c_value == "nautical mile per hour": 
					converted_value = float(select_num * 3600) * 0.0000053996
					return converted_value
				elif s_value == "nautical mile per hour" and s_c_value == "centimeter per second": 
					converted_value = float(select_num / 3600) / 0.0000053996
					return converted_value
				elif s_value == "centimeter per second" and s_c_value == "nautical mile per minute": 
					converted_value = float(select_num * 60) * 0.0000053996
					return converted_value
				elif s_value == "nautical mile per minute" and s_c_value == "centimeter per second": 
					converted_value = float(select_num / 60) / 0.0000053996
					return converted_value
				elif s_value == "centimeter per second" and s_c_value == "nautical mile per second": 
					converted_value = float(select_num / 1) * 0.0000053996
					return converted_value
				elif s_value == "nautical mile per second" and s_c_value == "centimeter per second": 
					converted_value = float(select_num / 1) / 0.0000053996
					return converted_value
				elif s_value == "foot per hour" and s_c_value == "foot per minute": 
					converted_value = float(select_num / 60) / 1
					return converted_value
				elif s_value == "foot per minute" and s_c_value == "foot per hour": 
					converted_value = float(select_num * 60) / 1
					return converted_value
				elif s_value == "foot per hour" and s_c_value == "foot per second": 
					converted_value = float(select_num / 3600) / 1
					return converted_value
				elif s_value == "foot per second" and s_c_value == "foot per hour": 
					converted_value = float(select_num * 3600) / 1
					return converted_value
				elif s_value == "foot per hour" and s_c_value == "kilometer per hour": 
					converted_value = float(select_num / 1) / 3280.8399
					return converted_value
				elif s_value == "kilometer per hour" and s_c_value == "foot per hour": 
					converted_value = float(select_num / 1) * 3280.8399
					return converted_value
				elif s_value == "foot per hour" and s_c_value == "kilometer per minute": 
					converted_value = float(select_num / 60) / 3280.8399
					return converted_value
				elif s_value == "kilometer per minute" and s_c_value == "foot per hour": 
					converted_value = float(select_num * 60) * 3280.8399
					return converted_value
				elif s_value == "foot per hour" and s_c_value == "kilometer per second": 
					converted_value = float(select_num / 3600) / 3280.8399
					return converted_value
				elif s_value == "kilometer per second" and s_c_value == "foot per hour": 
					converted_value = float(select_num * 3600) * 3280.8399
					return converted_value
				elif s_value == "foot per hour" and s_c_value == "meter per hour": 
					converted_value = float(select_num / 1) / 3.2808399
					return converted_value
				elif s_value == "meter per hour" and s_c_value == "foot per hour": 
					converted_value = float(select_num / 1) * 3.2808399
					return converted_value
				elif s_value == "foot per hour" and s_c_value == "meter per minute": 
					converted_value = float(select_num / 60) / 3.2808399
					return converted_value
				elif s_value == "meter per minute" and s_c_value == "foot per hour": 
					converted_value = float(select_num * 60) * 3.2808399
					return converted_value
				elif s_value == "foot per hour" and s_c_value == "mile per hour": 
					converted_value = float(select_num / 1) / 5280
					return converted_value
				elif s_value == "mile per hour" and s_c_value == "foot per hour": 
					converted_value = float(select_num / 1) * 5280
					return converted_value
				elif s_value == "foot per hour" and s_c_value == "mile per minute": 
					converted_value = float(select_num / 60) / 5280
					return converted_value
				elif s_value == "mile per minute" and s_c_value == "foot per hour": 
					converted_value = float(select_num * 60) * 5280
					return converted_value
				elif s_value == "foot per hour" and s_c_value == "mile per second": 
					converted_value = float(select_num / 3600) / 5280
					return converted_value
				elif s_value == "mile per second" and s_c_value == "foot per hour": 
					converted_value = float(select_num * 3600) * 5280
					return converted_value
				elif s_value == "foot per hour" and s_c_value == "nautical mile per hour": 
					converted_value = float(select_num / 1) * 0.000164578834
					return converted_value
				elif s_value == "nautical mile per hour" and s_c_value == "foot per hour": 
					converted_value = float(select_num / 1) / 0.000164578834
					return converted_value
				elif s_value == "foot per hour" and s_c_value == "nautical mile per minute": 
					converted_value = float(select_num / 60) * 0.000164578834
					return converted_value
				elif s_value == "nautical mile per minute" and s_c_value == "foot per hour": 
					converted_value = float(select_num * 60) / 0.000164578834
					return converted_value
				elif s_value == "foot per hour" and s_c_value == "nautical mile per second": 
					converted_value = float(select_num / 3600) * 0.000164578834
					return converted_value
				elif s_value == "nautical mile per second" and s_c_value == "foot per hour": 
					converted_value = float(select_num * 3600) / 0.000164578834
					return converted_value
				elif s_value == "foot per minute" and s_c_value == "foot per second": 
					converted_value = float(select_num / 60) / 1 
					return converted_value
				elif s_value == "foot per second" and s_c_value == "foot per minute": 
					converted_value = float(select_num * 60) / 1 
					return converted_value
				elif s_value == "foot per minute" and s_c_value == "kilometer per hour": 
					converted_value = float(select_num * 60) / 3280.8399
					return converted_value
				elif s_value == "kilometer per hour" and s_c_value == "foot per minute": 
					converted_value = float(select_num / 60) * 3280.8399
					return converted_value
				elif s_value == "foot per minute" and s_c_value == "kilometer per minute": 
					converted_value = float(select_num / 1) / 3280.8399
					return converted_value
				elif s_value == "kilometer per minute" and s_c_value ==  "foot per minute": 
					converted_value = float(select_num / 1) * 3280.8399
					return converted_value
				elif s_value == "foot per minute" and s_c_value == "kilometer per second": 
					converted_value = float(select_num / 60) / 3280.8399
					return converted_value
				elif s_value == "kilometer per second" and s_c_value == "foot per minute": 
					converted_value = float(select_num * 60) * 3280.8399
					return converted_value
				elif s_value == "foot per minute" and s_c_value == "meter per hour": 
					converted_value = float(select_num * 60)  / 3.2808399
					return converted_value
				elif s_value == "meter per hour" and s_c_value == "foot per minute": 
					converted_value = float(select_num / 60)  * 3.2808399
					return converted_value
				elif s_value == "foot per minute" and s_c_value == "meter per minute": 
					converted_value = float(select_num / 1)  / 3.2808399
					return converted_value
				elif s_value == "meter per minute" and s_c_value == "foot per minute": 
					converted_value = float(select_num / 1)  * 3.2808399
					return converted_value
				elif s_value == "foot per minute" and s_c_value == "mile per hour": 
					converted_value = float(select_num * 60)  / 5280
					return converted_value
				elif s_value == "mile per hour" and s_c_value == "foot per minute": 
					converted_value = float(select_num / 60)  * 5280
					return converted_value
				elif s_value == "foot per minute" and s_c_value == "mile per minute": 
					converted_value = float(select_num / 1)  / 5280
					return converted_value
				elif s_value == "mile per minute" and s_c_value == "foot per minute": 
					converted_value = float(select_num / 1)  * 5280
					return converted_value
				elif s_value == "foot per minute" and s_c_value == "mile per second": 
					converted_value = float(select_num / 60)  / 5280
					return converted_value
				elif s_value == "mile per second" and s_c_value == "foot per minute": 
					converted_value = float(select_num * 60)  * 5280
					return converted_value
				elif s_value == "foot per minute" and s_c_value == "nautical mile per hour": 
					converted_value = float(select_num * 60)  * 0.000164578834
					return converted_value
				elif s_value == "nautical mile per hour" and s_c_value == "foot per minute": 
					converted_value = float(select_num / 60)  / 0.000164578834
					return converted_value
				elif s_value == "foot per minute" and s_c_value == "nautical mile per minute": 
					converted_value = float(select_num / 1 )  * 0.000164578834
					return converted_value
				elif s_value == "nautical mile per minute" and s_c_value == "foot per minute": 
					converted_value = float(select_num / 1 )  / 0.000164578834
					return converted_value
				elif s_value == "foot per minute" and s_c_value == "nautical mile per second": 
					converted_value = float(select_num / 60 )  * 0.000164578834
					return converted_value
				elif s_value == "nautical mile per second" and s_c_value == "foot per minute": 
					converted_value = float(select_num * 60 )  / 0.000164578834
					return converted_value
				elif s_value == "foot per second" and s_c_value == "kilometer per hour": 
					converted_value = float(select_num * 3600 )  / 3280.8399
					return converted_value
				elif s_value == "kilometer per hour" and s_c_value == "foot per second": 
					converted_value = float(select_num / 3600 )  * 3280.8399
					return converted_value
				elif s_value == "foot per second" and s_c_value == "kilometer per minute": 
					converted_value = float(select_num * 60 )  / 3280.8399
					return converted_value
				elif s_value == "kilometer per minute" and s_c_value == "foot per second": 
					converted_value = float(select_num / 60 )  * 3280.8399
					return converted_value
				elif s_value == "foot per second" and s_c_value == "kilometer per second": 
					converted_value = float(select_num / 1 )  / 3280.8399
					return converted_value
				elif s_value == "kilometer per second" and s_c_value == "foot per second": 
					converted_value = float(select_num / 1 )  * 3280.8399
					return converted_value
				elif s_value == "foot per second" and s_c_value == "meter per hour": 
					converted_value = float(select_num * 3600 )  / 3.2808399
					return converted_value
				elif s_value == "meter per hour" and s_c_value == "foot per second": 
					converted_value = float(select_num / 3600 )  * 3.2808399
					return converted_value
				elif s_value == "foot per second" and s_c_value == "meter per minute": 
					converted_value = float(select_num * 60 )  / 3.2808399
					return converted_value
				elif s_value == "meter per minute" and s_c_value == "foot per second": 
					converted_value = float(select_num / 60 )  * 3.2808399
					return converted_value
				elif s_value == "foot per second" and s_c_value == "mile per hour": 
					converted_value = float(select_num * 3600 )  / 5280
					return converted_value
				elif s_value == "mile per hour" and s_c_value == "foot per second": 
					converted_value = float(select_num / 3600 )  * 5280
					return converted_value
				elif s_value == "foot per second" and s_c_value == "mile per minute": 
					converted_value = float(select_num * 60 )  / 5280
					return converted_value
				elif s_value == "mile per minute" and s_c_value == "foot per second": 
					converted_value = float(select_num / 60 )  * 5280
					return converted_value
				elif s_value == "foot per second" and s_c_value == "mile per second": 
					converted_value = float(select_num / 1 )  / 5280
					return converted_value
				elif s_value == "mile per second" and s_c_value == "foot per second": 
					converted_value = float(select_num / 1 )  * 5280
					return converted_value
				elif s_value == "foot per second" and s_c_value == "nautical mile per hour": 
					converted_value = float(select_num * 3600 ) * 0.000164578834
					return converted_value
				elif s_value == "nautical mile per hour" and s_c_value == "foot per second": 
					converted_value = float(select_num / 3600 ) / 0.000164578834
					return converted_value
				elif s_value == "foot per second" and s_c_value == "nautical mile per minute": 
					converted_value = float(select_num * 60 ) * 0.000164578834
					return converted_value
				elif s_value == "nautical mile per minute" and s_c_value == "foot per second": 
					converted_value = float(select_num / 60 ) / 0.000164578834
					return converted_value
				elif s_value == "foot per second" and s_c_value == "nautical mile per second": 
					converted_value = float(select_num / 1 ) * 0.000164578834
					return converted_value
				elif s_value == "nautical mile per second" and s_c_value == "foot per second": 
					converted_value = float(select_num / 1 ) / 0.000164578834
					return converted_value
				elif s_value == "kilometer per hour" and s_c_value == "kilometer per minute": 
					converted_value = float(select_num / 60 ) / 1
					return converted_value
				elif s_value == "kilometer per minute" and s_c_value == "kilometer per hour": 
					converted_value = float(select_num * 60 ) / 1
					return converted_value
				elif s_value == "kilometer per hour" and s_c_value == "kilometer per second": 
					converted_value = float(select_num / 3600 ) / 1
					return converted_value
				elif s_value == "kilometer per second" and s_c_value == "kilometer per hour": 
					converted_value = float(select_num * 3600 ) / 1
					return converted_value
				elif s_value == "kilometer per hour" and s_c_value == "meter per hour": 
					converted_value = float(select_num / 1 ) * 1000
					return converted_value
				elif s_value == "meter per hour" and s_c_value == "kilometer per hour": 
					converted_value = float(select_num / 1 ) / 1000
					return converted_value
				elif s_value == "kilometer per hour" and s_c_value == "meter per minute": 
					converted_value = float(select_num / 60 ) * 1000
					return converted_value
				elif s_value == "meter per minute" and s_c_value == "kilometer per hour": 
					converted_value = float(select_num * 60 ) / 1000
					return converted_value
				elif s_value == "kilometer per hour" and s_c_value == "mile per hour": 
					converted_value = float(select_num / 1 ) * 0.621371192
					return converted_value
				elif s_value == "mile per hour" and s_c_value == "kilometer per hour": 
					converted_value = float(select_num / 1 ) / 0.621371192
					return converted_value
				elif s_value == "kilometer per hour" and s_c_value == "mile per minute": 
					converted_value = float(select_num / 60 ) * 0.621371192
					return converted_value
				elif s_value == "mile per minute" and s_c_value == "kilometer per hour": 
					converted_value = float(select_num * 60 ) / 0.621371192
					return converted_value
				elif s_value == "kilometer per hour" and s_c_value == "mile per second": 
					converted_value = float(select_num / 3600 ) * 0.621371192
					return converted_value
				elif s_value == "mile per second" and s_c_value == "kilometer per hour": 
					converted_value = float(select_num * 3600 ) / 0.621371192
					return converted_value
				elif s_value == "kilometer per hour" and s_c_value == "nautical mile per hour": 
					converted_value = float(select_num / 1 ) * 0.539956803
					return converted_value
				elif s_value == "nautical mile per hour" and s_c_value == "kilometer per hour": 
					converted_value = float(select_num / 1 ) / 0.539956803
					return converted_value
				elif s_value == "kilometer per hour" and s_c_value == "nautical mile per minute": 
					converted_value = float(select_num / 60 ) * 0.539956803
					return converted_value
				elif s_value == "nautical mile per minute" and s_c_value == "kilometer per hour": 
					converted_value = float(select_num * 60 ) / 0.539956803
					return converted_value
				elif s_value == "kilometer per hour" and s_c_value == "nautical mile per second": 
					converted_value = float(select_num / 3600 ) * 0.539956803
					return converted_value
				elif s_value == "nautical mile per second" and s_c_value == "kilometer per hour": 
					converted_value = float(select_num * 3600 ) / 0.539956803
					return converted_value
				elif s_value == "kilometer per minute" and s_c_value == "kilometer per second": 
					converted_value = float(select_num / 60 ) / 1
					return converted_value
				elif s_value == "kilometer per second" and s_c_value == "kilometer per minute": 
					converted_value = float(select_num * 60 ) / 1
					return converted_value
				elif s_value == "kilometer per minute" and s_c_value == "meter per hour": 
					converted_value = float(select_num * 60 ) * 1000
					return converted_value
				elif s_value == "meter per hour" and s_c_value == "kilometer per minute": 
					converted_value = float(select_num / 60 ) / 1000
					return converted_value
				elif s_value == "kilometer per minute" and s_c_value == "meter per minute": 
					converted_value = float(select_num / 1 ) * 1000
					return converted_value
				elif s_value == "meter per minute" and s_c_value == "kilometer per minute": 
					converted_value = float(select_num / 1 ) / 1000
					return converted_value
				elif s_value == "kilometer per minute" and s_c_value == "mile per hour": 
					converted_value = float(select_num * 60 ) * 0.621371192
					return converted_value
				elif s_value == "mile per hour" and s_c_value == "kilometer per minute": 
					converted_value = float(select_num / 60 ) / 0.621371192
					return converted_value
				elif s_value == "kilometer per minute" and s_c_value == "mile per minute": 
					converted_value = float(select_num / 1 ) * 0.621371192
					return converted_value
				elif s_value == "mile per minute" and s_c_value == "kilometer per minute": 
					converted_value = float(select_num / 1 ) / 0.621371192
					return converted_value
				elif s_value == "kilometer per minute" and s_c_value == "mile per second": 
					converted_value = float(select_num / 60 ) * 0.621371192
					return converted_value
				elif s_value == "mile per second" and s_c_value == "kilometer per minute": 
					converted_value = float(select_num * 60 ) / 0.621371192
					return converted_value
				elif s_value == "kilometer per minute" and s_c_value == "nautical mile per hour": 
					converted_value = float(select_num * 60 ) * 0.539956803
					return converted_value
				elif s_value == "nautical mile per hour" and s_c_value == "kilometer per minute": 
					converted_value = float(select_num / 60 ) / 0.539956803
					return converted_value
				elif s_value == "kilometer per minute" and s_c_value == "nautical mile per minute": 
					converted_value = float(select_num / 1 ) * 0.539956803
					return converted_value
				elif s_value == "nautical mile per minute" and s_c_value == "kilometer per minute": 
					converted_value = float(select_num / 1 ) / 0.539956803
					return converted_value
				elif s_value == "kilometer per minute" and s_c_value == "nautical mile per second": 
					converted_value = float(select_num / 60 ) * 0.539956803
					return converted_value
				elif s_value == "nautical mile per second" and s_c_value == "kilometer per minute": 
					converted_value = float(select_num * 60 ) / 0.539956803
					return converted_value
				elif s_value == "kilometer per second" and s_c_value == "meter per hour": 
					converted_value = float(select_num * 3600 ) * 1000
					return converted_value
				elif s_value == "meter per hour" and s_c_value == "kilometer per second": 
					converted_value = float(select_num / 3600 ) / 1000
					return converted_value
				elif s_value == "kilometer per second" and s_c_value == "meter per minute": 
					converted_value = float(select_num * 60 ) * 1000
					return converted_value
				elif s_value == "meter per minute" and s_c_value == "kilometer per second": 
					converted_value = float(select_num / 60 ) / 1000
					return converted_value
				elif s_value == "kilometer per second" and s_c_value == "mile per hour": 
					converted_value = float(select_num * 3600 ) * 0.621371192
					return converted_value
				elif s_value == "mile per hour" and s_c_value == "kilometer per second": 
					converted_value = float(select_num / 3600 ) / 0.621371192
					return converted_value
				elif s_value == "kilometer per second" and s_c_value == "mile per minute": 
					converted_value = float(select_num * 60 ) * 0.621371192
					return converted_value
				elif s_value == "mile per minute" and s_c_value == "kilometer per second": 
					converted_value = float(select_num / 60 ) / 0.621371192
					return converted_value
				elif s_value == "kilometer per second" and s_c_value == "mile per second": 
					converted_value = float(select_num / 1 ) * 0.621371192
					return converted_value
				elif s_value == "mile per second" and s_c_value == "kilometer per second": 
					converted_value = float(select_num / 1 ) / 0.621371192
					return converted_value
				elif s_value == "kilometer per second" and s_c_value == "nautical mile per hour": 
					converted_value = float(select_num * 3600 ) * 0.539956803
					return converted_value
				elif s_value == "nautical mile per hour" and s_c_value == "kilometer per second": 
					converted_value = float(select_num / 3600 ) / 0.539956803
					return converted_value
				elif s_value == "kilometer per second" and s_c_value == "nautical mile per minute": 
					converted_value = float(select_num * 60 ) * 0.539956803
					return converted_value
				elif s_value == "nautical mile per minute" and s_c_value == "kilometer per second": 
					converted_value = float(select_num / 60 ) / 0.539956803
					return converted_value
				elif s_value == "kilometer per second" and s_c_value == "nautical mile per second": 
					converted_value = float(select_num / 1 ) * 0.539956803
					return converted_value
				elif s_value == "nautical mile per second" and s_c_value == "kilometer per second": 
					converted_value = float(select_num / 1 ) / 0.539956803
					return converted_value
				elif s_value == "meter per hour" and s_c_value == "meter per minute": 
					converted_value = float(select_num / 60 ) / 1
					return converted_value
				elif s_value == "meter per minute" and s_c_value == "meter per hour": 
					converted_value = float(select_num * 60 ) / 1
					return converted_value
				elif s_value == "meter per hour" and s_c_value == "mile per hour": 
					converted_value = float(select_num / 1 ) * 0.000621371192
					return converted_value
				elif s_value == "mile per hour" and s_c_value == "meter per hour": 
					converted_value = float(select_num / 1 ) / 0.000621371192
					return converted_value
				elif s_value == "meter per hour" and s_c_value == "mile per minute": 
					converted_value = float(select_num / 60 ) * 0.000621371192
					return converted_value
				elif s_value == "mile per minute" and s_c_value == "meter per hour": 
					converted_value = float(select_num * 60 ) / 0.000621371192
					return converted_value
				elif s_value == "meter per hour" and s_c_value == "mile per second": 
					converted_value = float(select_num / 3600 ) * 0.000621371192
					return converted_value
				elif s_value == "mile per second" and s_c_value == "meter per hour": 
					converted_value = float(select_num * 3600 ) / 0.000621371192
					return converted_value
				elif s_value == "meter per hour" and s_c_value == "nautical mile per hour": 
					converted_value = float(select_num / 1 ) / 1852
					return converted_value
				elif s_value == "nautical mile per hour" and s_c_value == "meter per hour": 
					converted_value = float(select_num / 1 ) * 1852
					return converted_value
				elif s_value == "meter per hour" and s_c_value == "nautical mile per minute": 
					converted_value = float(select_num / 60 ) / 1852
					return converted_value
				elif s_value == "nautical mile per minute" and s_c_value == "meter per hour": 
					converted_value = float(select_num * 60 ) * 1852
					return converted_value
				elif s_value == "meter per hour" and s_c_value == "nautical mile per second": 
					converted_value = float(select_num / 3600 ) / 1852
					return converted_value
				elif s_value == "nautical mile per second" and s_c_value == "meter per hour": 
					converted_value = float(select_num * 3600 ) * 1852
					return converted_value
				elif s_value == "meter per minute" and s_c_value == "mile per hour": 
					converted_value = float(select_num * 60 ) * 0.000621371192
					return converted_value
				elif s_value == "mile per hour" and s_c_value == "meter per minute": 
					converted_value = float(select_num / 60 ) / 0.000621371192
					return converted_value
				elif s_value == "meter per minute" and s_c_value == "mile per minute": 
					converted_value = float(select_num / 1 ) * 0.000621371192
					return converted_value
				elif s_value == "mile per minute" and s_c_value == "meter per minute": 
					converted_value = float(select_num / 1 ) / 0.000621371192
					return converted_value
				elif s_value == "meter per minute" and s_c_value == "mile per second": 
					converted_value = float(select_num / 60 ) * 0.000621371192
					return converted_value
				elif s_value == "mile per second" and s_c_value == "meter per minute": 
					converted_value = float(select_num * 60 ) / 0.000621371192
					return converted_value
				elif s_value == "meter per minute" and s_c_value == "nautical mile per hour": 
					converted_value = float(select_num * 60 ) / 1852
					return converted_value
				elif s_value == "nautical mile per hour" and s_c_value == "meter per minute": 
					converted_value = float(select_num / 60 ) * 1852
					return converted_value
				elif s_value == "meter per minute" and s_c_value == "nautical mile per minute": 
					converted_value = float(select_num / 1 ) / 1852
					return converted_value
				elif s_value == "nautical mile per minute" and s_c_value == "meter per minute": 
					converted_value = float(select_num / 1 ) * 1852
					return converted_value
				elif s_value == "meter per minute" and s_c_value == "nautical mile per second": 
					converted_value = float(select_num / 60 ) / 1852
					return converted_value
				elif s_value == "nautical mile per second" and s_c_value == "meter per minute": 
					converted_value = float(select_num * 60 ) * 1852
					return converted_value
				elif s_value == "mile per hour" and s_c_value == "mile per minute": 
					converted_value = float(select_num / 60 ) / 1
					return converted_value
				elif s_value == "mile per minute" and s_c_value == "mile per hour": 
					converted_value = float(select_num * 60 ) / 1
					return converted_value
				elif s_value == "mile per hour" and s_c_value == "mile per second": 
					converted_value = float(select_num / 3600 ) / 1
					return converted_value
				elif s_value == "mile per second" and s_c_value == "mile per hour": 
					converted_value = float(select_num * 3600 ) / 1
					return converted_value
				elif s_value == "mile per hour" and s_c_value == "nautical mile per hour": 
					converted_value = float(select_num / 1 ) * 0.868976242
					return converted_value
				elif s_value == "nautical mile per hour" and s_c_value == "mile per hour": 
					converted_value = float(select_num / 1 ) / 0.868976242
					return converted_value
				elif s_value == "mile per hour" and s_c_value == "nautical mile per minute": 
					converted_value = float(select_num / 60 ) * 0.868976242
					return converted_value
				elif s_value == "nautical mile per minute" and s_c_value == "mile per hour": 
					converted_value = float(select_num * 60 ) / 0.868976242
					return converted_value
				elif s_value == "mile per hour" and s_c_value == "nautical mile per second": 
					converted_value = float(select_num / 3600 ) * 0.868976242
					return converted_value
				elif s_value == "nautical mile per second" and s_c_value == "mile per hour": 
					converted_value = float(select_num * 3600 ) / 0.868976242
					return converted_value
				elif s_value == "mile per minute" and s_c_value == "mile per second": 
					converted_value = float(select_num / 60 ) / 1
					return converted_value
				elif s_value == "mile per second" and s_c_value == "mile per minute": 
					converted_value = float(select_num * 60 ) / 1
					return converted_value
				elif s_value == "mile per minute" and s_c_value == "nautical mile per hour": 
					converted_value = float(select_num * 60 ) * 0.868976242
					return converted_value
				elif s_value == "nautical mile per hour" and s_c_value == "mile per minute": 
					converted_value = float(select_num / 60 ) / 0.868976242
					return converted_value
				elif s_value == "mile per minute" and s_c_value == "nautical mile per minute": 
					converted_value = float(select_num / 1 ) * 0.868976242
					return converted_value
				elif s_value == "nautical mile per minute" and s_c_value == "mile per minute": 
					converted_value = float(select_num / 1 ) / 0.868976242
					return converted_value
				elif s_value == "mile per minute" and s_c_value == "nautical mile per second": 
					converted_value = float(select_num / 60 ) * 0.868976242
					return converted_value
				elif s_value == "nautical mile per second" and s_c_value == "mile per minute": 
					converted_value = float(select_num * 60 ) / 0.868976242
					return converted_value
				elif s_value == "mile per second" and s_c_value == "nautical mile per hour": 
					converted_value = float(select_num * 3600 ) * 0.868976242
					return converted_value
				elif s_value == "nautical mile per hour" and s_c_value == "mile per second": 
					converted_value = float(select_num / 3600 ) / 0.868976242
					return converted_value
				elif s_value == "mile per second" and s_c_value == "nautical mile per minute": 
					converted_value = float(select_num * 60 ) * 0.868976242
					return converted_value
				elif s_value == "nautical mile per minute" and s_c_value == "mile per second": 
					converted_value = float(select_num / 60 ) / 0.868976242
					return converted_value
				elif s_value == "mile per second" and s_c_value == "nautical mile per second": 
					converted_value = float(select_num / 1 ) * 0.868976242
					return converted_value
				elif s_value == "nautical mile per second" and s_c_value == "mile per second": 
					converted_value = float(select_num / 1 ) / 0.868976242
					return converted_value
				elif s_value == "nautical mile per hour" and s_c_value == "nautical mile per minute": 
					converted_value = float(select_num / 60 ) / 1
					return converted_value
				elif s_value == "nautical mile per minute" and s_c_value == "nautical mile per hour": 
					converted_value = float(select_num * 60 ) / 1
					return converted_value
				elif s_value == "nautical mile per hour" and s_c_value == "nautical mile per second": 
					converted_value = float(select_num / 3600 ) / 1
					return converted_value
				elif s_value == "nautical mile per second" and s_c_value == "nautical mile per hour": 
					converted_value = float(select_num * 3600 ) / 1
					return converted_value
				elif s_value == "nautical mile per minute" and s_c_value == "nautical mile per second": 
					converted_value = float(select_num / 60 ) / 1
					return converted_value
				elif s_value == "nautical mile per second" and s_c_value == "nautical mile per minute": 
					converted_value = float(select_num * 60 ) / 1
					return converted_value
				else: 
					print('It seems you have enetered a non-calculatable value, try again with these values:\n')
					print(speedUnits())
					print('\nNo value has been returned yet!')
					return False
			else:
				print('one or both value are not valid!\n Try again with these values: ')
				print(speedUnits())
				print('\nNo value has been returned yet!')
				return False
	except Exception: 
		print('There must be something wrong, try again:')
