class Distance:
	def __init__(self, unit):
		self.unit = unit


	def defUnit(my_unit):
		unit = distanceUnits(my_unit)
		return unit 

	def calculateDistance(unit, speed, time):
		try:
			time_title = 'time'
			speed_title = 'speed'
			get_unit = distanceUnits(unit)
			if isinstance(time, int) or isinstance(time, float):
				if isinstance(speed, int) or isinstance(speed, float):
					if isinstance(get_unit, str):  		
						distance_calculation = float(time * speed)
						print_distance_claculation =  str(distance_calculation) + ' ' + get_unit
						print(f'Distance has been calculated and stored successfully: {print_distance_claculation} ')
						return print_distance_claculation
				else: 
					print(f"It seems you have entered unreal values: in '{speed_title}': {speed} value, try again!")
			else: 
				print(f"It seems you have entered unreal values in '{time_title}' : {time} value, try again!")
		except Exception:
			print('There must be something wrong, try again!')


def distanceUnits(select_value = 'none'):
	try:
		distance_units = {
			'm' : 'meter', 
		   'cm' : 'centimeter', 
		   'ft' : 'foot', 
		   'km' :  'kilometer', 
		   'mi' : 'mile', 
		   'nmi': 'nautical mile', 
				}

		if select_value != 'none': 
			return_value = distance_units.get(select_value, 'No value has been found in distance units')
			if return_value == 'No value has been found in distance units':
				print(return_value)
				print('Try again with these values: \n')
				distanceUnits()
				print('\nNo value has been returned yet!')
				return False
			else: 	
				return return_value
		elif select_value == 'none': 
			count = 1
			for i in distance_units:
				print(str(count) + ' : ' + "\u0332".join(i) + ' : ' + distance_units[i])
				count += 1
	except Exception: 
		print('There must be something wrong, try again!')

def distanceConvertor(select_value, select_convert_value, select_num):
	try:
		converted_value = '' 
		if select_value:
			s_value = select_value
			if select_convert_value: 
				s_c_value = select_convert_value
				if select_num <= 0:
					print(f'Your number {select_num} cannot be converted, try again')
					return False
				elif s_value == "meter" and s_c_value == "centimeter": 
					converted_value = float(select_num * 100)
					distanceUnits()
					return converted_value
				elif s_value == "centimeter" and s_c_value == "meter": 
					converted_value = float(select_num / 100)
					distanceUnits()
					return converted_value
				elif s_value == "foot" and s_c_value == "meter": 
					converted_value = float(select_num / 3.2808399)
					distanceUnits()
					return converted_value
				elif s_value == "meter" and s_c_value == "foot": 
					converted_value = float(select_num * 3.2808399)
					distanceUnits()
					return converted_value
				elif s_value == "foot" and s_c_value == "centimeter": 
					converted_value = float(select_num * 30.48)
					distanceUnits()
					return converted_value
				elif s_value == "centimeter" and s_c_value == "foot": 
					converted_value = float(select_num / 30.48)
					distanceUnits()
					return converted_value
				elif s_value == "foot" and s_c_value == "kilometer": 
					converted_value = float(select_num  / 3280.8399)
					distanceUnits()
					return converted_value
				elif s_value == "kilometer" and s_c_value == "foot": 
					converted_value = float(select_num  * 3280.8399)
					distanceUnits()
					return converted_value
				elif s_value == "foot" and s_c_value == "mile": 
					converted_value = float(select_num  / 5280)
					distanceUnits()
					return converted_value
				elif s_value == "mile" and s_c_value == "foot": 
					converted_value = float(select_num  * 5280)
					distanceUnits()
					return converted_value
				elif s_value == "foot" and s_c_value == "nautical mile": 
					converted_value = float(select_num  * 0.000164578834)
					distanceUnits()
					return converted_value
				elif s_value == "nautical mile" and s_c_value == "foot": 
					converted_value = float(select_num  / 0.000164578834)
					distanceUnits()
					return converted_value
				elif s_value == "meter" and s_c_value == "kilometer": 
					converted_value = float(select_num  / 1000)
					distanceUnits()
					return converted_value
				elif s_value == "kilometer" and s_c_value == "meter": 
					converted_value = float(select_num  * 1000)
					distanceUnits()
					return converted_value
				elif s_value == "meter" and s_c_value == "mile": 
					converted_value = float(select_num  * 0.000621371192)
					distanceUnits()
					return converted_value
				elif s_value ==  "mile" and s_c_value == "meter": 
					converted_value = float(select_num  / 0.000621371192)
					distanceUnits()
					return converted_value
				elif s_value == "meter" and s_c_value == "nautical mile": 
					converted_value = float(select_num  / 1852)
					distanceUnits()
					return converted_value
				elif s_value == "nautical mile" and s_c_value == "meter": 
					converted_value = float(select_num  * 1852)
					distanceUnits()
					return converted_value
				elif s_value == "centimeter" and s_c_value == "kilometer": 
					converted_value = float(select_num  / 100000)
					distanceUnits()
					return converted_value
				elif s_value == "kilometer" and s_c_value == "centimeter": 
					converted_value = float(select_num  * 100000)
					distanceUnits()
					return converted_value
				elif s_value == "centimeter" and s_c_value == "mile": 
					converted_value = float(select_num  * 0.00000621371)
					distanceUnits()
					return converted_value
				elif s_value == "mile" and s_c_value == "centimeter": 
					converted_value = float(select_num  / 0.00000621371)
					distanceUnits()
					return converted_value
				elif s_value == "centimeter" and s_c_value == "nautical mile": 
					converted_value = float(select_num  * 0.0000053996)
					distanceUnits()
					return converted_value
				elif s_value == "nautical mile" and s_c_value == "centimeter": 
					converted_value = float(select_num  / 0.0000053996)
					distanceUnits()
					return converted_value
				elif s_value == "kilometer" and s_c_value == "mile": 
					converted_value = float(select_num  * 0.621371192)
					distanceUnits()
					return converted_value
				elif s_value == "mile" and s_c_value == "kilometer": 
					converted_value = float(select_num  / 0.621371192)
					distanceUnits()
					return converted_value
				elif s_value == "kilometer" and s_c_value == "nautical mile": 
					converted_value = float(select_num  * 0.539956803)
					distanceUnits()
					return converted_value
				elif s_value == "nautical mile" and s_c_value == "kilometer": 
					converted_value = float(select_num  / 0.539956803)
					distanceUnits()
					return converted_value
				elif s_value == "mile" and s_c_value == "nautical mile": 
					converted_value = float(select_num  * 0.868976242)
					distanceUnits()
					return converted_value
				elif s_value == "nautical mile" and s_c_value == "mile": 
					converted_value = float(select_num  / 0.868976242)
					distanceUnits()
					return converted_value
				
				else: 
					print('It seems you have enetered a non-calculatable value, try again with these values:\n')
					print(distanceUnits())
					print('\nNo value has been returned yet!')
					return False
			else:
				print('one or both value are not valid!\n Try again with these values: ')
				print(distanceUnits())
				print('\nNo value has been returned yet!')
				return False
	except Exception: 
		print('There must be something wrong, try again:')

def convertCentimeterMillimeter(select_num):
	millimeter = 'millimeter/s' 
	try:
		if select_num == '' or select_num == ' ': 
			print(f"You must enter a full value to convert, try again!")
			return False
		elif isinstance(select_num, str):
			print(f"You must enter a number, looks not like: '{select_num}', try again!")
			return False
		elif select_num <= 0:
			print(f'Your number {select_num} cannot be converted, try again')
			return False
		elif isinstance(select_num, int) or isinstance(select_num, float):
			 centimeter_to_millimeter = float(select_num * 10) 
			 print_centimeter_to_millimeter = str(centimeter_to_millimeter) + ' ' + millimeter 
			 print(f'Distance has been calculated and stored successfully: {print_centimeter_to_millimeter} ')
			 return print_centimeter_to_millimeter
		else: 
			print('There must be something wrong, no data has been stored yet, try again!')
			return False
	except Exception:
			print('There must be something wrong')
			return False

def convertMeterYard(select_num):
	yard = 'yard/s' 
	try:
		if select_num == '' or select_num == ' ': 
			print(f"You must enter a full value to convert, try again!")
			return False
		elif isinstance(select_num, str):
			print(f"You must enter a number, looks not like: '{select_num}', try again!")
			return False
		elif select_num <= 0:
			print(f'Your number {select_num} cannot be converted, try again')
			return False
		elif isinstance(select_num, int) or isinstance(select_num, float):
			 meter_to_yard = float(select_num * 1.0936133) 
			 print_meter_to_yard = str(meter_to_yard) + ' ' + yard 
			 print(f'Distance has been calculated and stored successfully: {print_meter_to_yard} ')
			 return  print_meter_to_yard
		else: 
			print('There must be something wrong, no data has been stored yet, try again!')
			return False
	except Exception:
			print('There must be something wrong')
			return False

def convertMillimeterInches(select_num):
	inch = 'inch/s' 
	try:
		if select_num == '' or select_num == ' ': 
			print(f"You must enter a full value to convert, try again!")
			return False
		elif isinstance(select_num, str):
			print(f"You must enter a number, looks not like: '{select_num}', try again!")
			return False
		elif select_num <= 0:
			print(f'Your number {select_num} cannot be converted, try again')
			return False
		elif isinstance(select_num, int) or isinstance(select_num, float):
			 millimeter_to_inches = float(select_num * 0.0393700787) 
			 print_millimeter_to_inches = str(millimeter_to_inches) + ' ' + inch
			 print(f'Distance has been calculated and stored successfully: {print_millimeter_to_inches} ')
			 return  print_millimeter_to_inches
		else: 
			print('There must be something wrong, no data has been stored yet, try again!')
			return False
	except Exception:
			print('There must be something wrong')
			return False

def convertCentimeterMicron(select_num):
	micron = 'micron/s' 
	try:
		if select_num == '' or select_num == ' ': 
			print(f"You must enter a full value to convert, try again!")
			return False
		elif isinstance(select_num, str):
			print(f"You must enter a number, looks not like: '{select_num}', try again!")
			return False
		elif select_num <= 0:
			print(f'Your number {select_num} cannot be converted, try again')
			return False
		elif isinstance(select_num, int) or isinstance(select_num, float):
			 centimeter_to_micron = float(select_num * 10000) 
			 print_centimeter_to_micron = str(centimeter_to_micron) + ' ' + micron
			 print(f'Distance has been calculated and stored successfully: {print_centimeter_to_micron} ')
			 return  print_centimeter_to_micron
		else: 
			print('There must be something wrong, no data has been stored yet, try again!')
			return False
	except Exception:
			print('There must be something wrong')
			return False


