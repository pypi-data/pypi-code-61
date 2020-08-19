class Time:
	def __init__(self, unit):
		self.unit = unit

	def defUnit(my_unit):
		unit = timeUnits(my_unit)
		return unit 

	def calculateTime(unit, distance, speed):
		try:
			distance_title = 'distance'
			speed_title = 'speed'
			get_unit = timeUnits(unit)
			if isinstance(distance, int) or isinstance(distance, float):
				if isinstance(speed, int) or isinstance(speed, float):
					if isinstance(get_unit, str):  		
						time_calculation = float(distance / speed)
						print_time_claculation =  str(time_calculation) + ' ' + get_unit
						print(f'Time has been calculated and stored successfully: {print_time_claculation} ')
						return print_time_claculation
				else: 
					print(f"It seems you have entered unreal values: in '{speed_title}': {speed} value, try again!")
			else: 
				print(f"It seems you have entered unreal values in '{distance_title}' : {distance} value, try again!")
		except Exception:
			print('There must be something wrong, try again!')

def timeUnits(select_value = 'none'):
	try:
		time_units = {
			's' : 'second', 
		  'min' : 'minute', 
		   'hr' : 'hour', 
				}

		if select_value != 'none': 
			return_value = time_units.get(select_value, 'No value has been found in time units')
			if return_value == 'No value has been found in time units':
				print(return_value)
				print('Try again with these values: \n')
				timeUnits()
				print('\nNo value has been returned yet!')
				return False
			else: 	
				return return_value
		elif select_value == 'none': 
			count = 1
			for i in time_units:
				print(str(count) + ' : ' + "\u0332".join(i) + ' : ' + time_units[i])
				count += 1
	except Exception: 
		print('There must be something wrong, try again!')

def timeConvertor(select_value, select_convert_value, select_num):
	try:
		converted_value = '' 
		if select_value:
			s_value = select_value
			if select_convert_value: 
				s_c_value = select_convert_value
				if select_num <= 0:
					print(f'Your number {select_num} cannot be converted, try again')
					return False
				elif s_value == "second" and s_c_value == "minute": 
					converted_value = float(select_num / 60)
					return converted_value
				elif s_value == "minute" and s_c_value == "second": 
					converted_value = float(select_num * 60)
					return converted_value
				elif s_value == "second" and s_c_value == "hour": 
					converted_value = float(select_num / 3600)
					return converted_value
				elif s_value == "hour" and s_c_value == "second": 
					converted_value = float(select_num * 3600)
					return converted_value
				elif s_value == "minute" and s_c_value == "hour": 
					converted_value = float(select_num / 60)
					return converted_value
				elif s_value == "hour" and s_c_value == "minute": 
					converted_value = float(select_num * 60)
					return converted_value

				else: 
					print('It seems you have enetered a non-calculatable value, try again with these values:\n')
					print(timeUnits())
					print('\nNo value has been returned yet!')
					return False
			else:
				print('one or both value are not valid!\n Try again with these values: ')
				print(timeUnits())
				print('\nNo value has been returned yet!')
				return False
	except Exception: 
		print('There must be something wrong, try again:')

def convertMinutesDays(select_num):
	day = 'day/s' 
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
			 minute_to_days = float(select_num * 0.000694444444) 
			 print_minute_to_days = str(minute_to_days) + ' ' + day 
			 print(f'Time has been calculated and stored successfully: {print_minute_to_days} ')
			 return print_minute_to_days
		else: 
			print('There must be something wrong, no data has been stored yet, try again!')
			return False
	except Exception:
			print('There must be something wrong')
			return False

def convertHoursDays(select_num):
	day = 'day/s' 
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
			 hour_to_days = float(select_num / 24) 
			 print_hour_to_days = str(hour_to_days) + ' ' + day 
			 print(f'Time has been calculated and stored successfully: {print_hour_to_days} ')
			 return print_hour_to_days
		else: 
			print('There must be something wrong, no data has been stored yet, try again!')
			return False
	except Exception:
			print('There must be something wrong')
			return False

def convertSecondsDays(select_num):
	day = 'day/s' 
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
			 second_to_days = float(select_num / 3600 ) / 24 
			 print_second_to_days = str(second_to_days) + ' ' + day 
			 print(f'Time has been calculated and stored successfully: {print_second_to_days} ')
			 return print_second_to_days
		else: 
			print('There must be something wrong, no data has been stored yet, try again!')
			return False
	except Exception:
			print('There must be something wrong')
			return False

def convertDaysWeeks(select_num):
	week = 'week/s' 
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
			 days_to_weeks = float(select_num / 7 )  
			 print_days_to_weeks = str(days_to_weeks) + ' ' + week 
			 print(f'Time has been calculated and stored successfully: {print_days_to_weeks} ')
			 return print_days_to_weeks
		else: 
			print('There must be something wrong, no data has been stored yet, try again!')
			return False
	except Exception:
			print('There must be something wrong')
			return False

def convertDaysYears(select_num):
	year = 'year/s' 
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
			 days_to_years = float(select_num / 365.24 )  
			 print_days_to_years = str(days_to_years) + ' ' + year
			 print(f'Time has been calculated and stored successfully: {print_days_to_years} ')
			 return print_days_to_years
		else: 
			print('There must be something wrong, no data has been stored yet, try again!')
			return False
	except Exception:
			print('There must be something wrong')
			return False

		
