"""
Functions of this program::
1) Set an origin of the x-y coordinate system map, inputs are the GPS (lat, lng)
2) Convertion between GPS (lat, lng) and x-y coordinate (x,y) based on the origin
"""

import math
		
class Location:
	"""
	Initialize this class also set the origin of the coordinate system at the same time.
	
	Example:
	----------
	# Set the origin
	> origin = this_file_name.Location(origin_lat, origin_lng)
	"""
	# Assign object attributes
    # ------------------------
	D2R = (math.pi / 180.0)	#Degree to radians
	R = 6367000				#Earth radius in meters
	x = float
	y = float

	"""
	 originlat - y ; originlng - x
	 originlat	equivalent to Y
	 originlng 	equivalent to X
	"""

	def __init__(self,originlat=float,originlng=float):
		self.longitude = originlng
		self.latitude = originlat
	
	def convertXY2GPS(self, dX=float, dY=float):
		"""
		Convert the (x,y) to GPS. Returns the object attributes .x and .y in this class.
		
		Must set the  origin first.
		
		Example: Set the origin and convert (x,y) coordinate to GPS.
		----------
		1st	# Set the origin
			origin = this_file_name.Location(origin_lat, origin_lng) 

		2nd	# Converts (x,y) to GPS
			gps = origin.convertXY2GPS(x,y)
			
		3rd	# Get the converted result
			lat = gps.latitude
			lat = gos.longitude
		"""

		c = dY/self.R
		g = math.pow(math.tan(c/2.0), 2.0)
		
		a = g/(1+g)
		dlat = math.asin(math.sqrt(a))*2.0
		
		lat = (dlat/self.D2R) + self.latitude
		
		c = dX/self.R
		g = math.pow(math.tan(c/2.0), 2)
		
		a = g/(1+g)
		F = math.cos(self.latitude*self.D2R)*math.cos(self.latitude*self.D2R)
		if(F < 0):
			# print("convertXY2GPS: F<0")
			return Location(0,0)
		if(a/F < -1):
			# print("error, convertXY2GPS: a/F < -1, arcsin(a/F) cannot find")
			return Location(0,0)
		if(a/F > 1):
			# print("error, convertXY2GPS: a/F > 1, arcsin(a/F) cannot find")
			return Location(0,0)
		dlon = 2.0*math.asin(math.sqrt(a/F))
		
		lng = (dlon/self.D2R) + self.longitude
		
		return Location(lat,lng)
		
	# def __repr__(self):
	# 	return ("Lat:%11.6f Lng:%10.6f\n  X:%11.6f   Y:%10.6f" % (latitude,longitude,x,y) )

	def distanceX(self, lat=float, lng=float):
		"""
		unit: meter(s), type: float, Calculate horizontal distance from origin based on GPS (lat, lng)
		OR Calculate x coordinate of the GPS based on given origin.
		Returns the distance.

		Must set the  origin first.
		
		Example: Set the origin and convert (x,y) coordinate to GPS.
		----------
		1st	# Set the origin
			origin = this_file_name.Location(origin_lat, origin_lng)
		
		2nd	# Return the distance in float
			xdistance = origin.distanceX_v2(lat=lat_val, lng=lng_val)
		"""

		dlong = (self.longitude - lng) *self.D2R
		dlat = (self.latitude - self.latitude) *self.D2R
		a = math.pow(math.sin(dlat/2.0), 2.0) + math.cos(self.latitude*self.D2R) * math.cos(self.latitude*self.D2R) * math.pow(math.sin(dlong/2.0), 2.0)
		c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0-a))
		d =self.R * c
		return d

	def distanceY(self, lat=float, lng=float):
		"""
		unit: meter(s), type: float, Calculate the vertical distance (y coordinate) from origin based on GPS (lat, lng)
		OR Calculate y coordinate of the GPS based on given origin.
		Returns the distance.

		Must set the  origin first.
		
		Example: Set the origin and convert (x,y) coordinate to GPS.
		----------
		1st	# Set the origin
			origin = this_file_name.Location(origin_lat, origin_lng)
		
		2nd	# Return the distance in float
			ydistance = origin.distancey_v2(lat=lat_val, lng=lng_val)
		"""

		dlong = (self.longitude - self.longitude) *self.D2R
		dlat = (self.latitude - lat) *self.D2R
		a = math.pow(math.sin(dlat/2.0), 2.0) + math.cos(lat*self.D2R) * math.cos(self.latitude*self.D2R) * math.pow(math.sin(dlong/2.0), 2.0)
		c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
		d =self.R * c
		return d

	def distance_btw2xy(self, x1=float, y1=float, x2=float, y2=float):
		"""
		unit: meter(s), type: float, Calculate the distance between two (x,y) points.
		Returns the distance.

		Must set the  origin first.
		
		Example: Set the origin and convert (x,y) coordinate to GPS.
		----------
		1st	# Set the origin
			origin = this_file_name.Location(origin_lat, origin_lng)
		
		2nd	# Return the distance in float
			distance = origin.distance_btw2xy(lat=lat_val, lng=lng_val)
		"""
		d = math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2, 2))
		return d

	def convertGPS2XY(self, lat=float, lng=float) -> dict:
		"""
		Convert GPS (latitude, longitude) to (x,y) based on origin. Returns (x,y) as a dict.
		
		Example
		----------
		1st	# Set the origin
			origin = this_file_name.Location(origin_lat, origin_lng)

		2nd	# Converts GPS to (x,y)
			xy = origin.convertGPS2XY_v2(lat,lng)

		3rd	# Get the converted result
			# xy = dict {'x': x, 'y': y}
		"""
		self.x = self.distanceX_v2(lat, lng)
		self.y = self.distanceY_v2(lat,lng)
		return {'x': self.x, 'y': self.y}

	def convertGPSlist2XYlist(self, latList=list, lngList=list) -> dict:
		"""Convert a list of GPS (latitude, longitude) to a list of (x,y) based on origin. Returns a list of (x,y) as a dict.

		Example
		----------
		1st	# Set the origin
			origin = this_file_name.Location(origin_lat, origin_lng)

		2nd	# Converts a list of GPS to a list of (x,y)
			xy = origin.convertGPSlist2XYlist(lat_list,lng_list)

		3rd	# Get the converted result
			# xy = dict {'x': x_list, 'y': y_list}
		"""
		x_coord_list = list()
		y_coord_list = list()
		for index in range(len(latList)):
			xy = self.convertGPS2XY_v2(latList[index],lngList[index])
			x_coord_list.append(xy['x'])
			y_coord_list.append(xy['y'])
		return {'x': x_coord_list, 'y': y_coord_list}

	def distance_btw2gps(self, lat1=float, lng1=float, lat2=float, lng2=float):
		"""
		Calculate the distance bewteen two GPS locations.
		
		unit: meter(s), type: float. Return a float.
		
		Must set the  origin first.

		Function illustration
		----------
		1st Convert two GPS to (x,y) coordinates based on the origin set before.
		2nd Calculate the distance bewteeb two (x,y).
		3rd Return the distance (float).

		Example
		----------
		1st	# Set the origin
			origin = this_file_name.Location(origin_lat, origin_lng)
		2nd	distance = distance_btw2gps(lat1=lat_val1, lng1=lng_val1, lat2=lat_val2, lng2=lng_val2)
		"""

		#1st Convert GPS to (x,y)
		xy1 = self.convertGPS2XY_v2(lat1, lng1)
		xy2 = self.convertGPS2XY_v2(lat2, lng2)
		
		#2nd Find distance between two points
		distance = self.distance_btw2xy(x1=xy1['x'], y1=xy1['y'], x2=xy2['x'], y2=xy2['y'])
		
		return distance


""" ######## By Sing <BEGIN> ######## """
def demo_xy2gps(originlat=float, originlng=float, x=float, y=float):
	xy = Location(originlat,originlng).convertXY2GPS(x,y)
	print(xy.latitude)
	print(xy.longitude)

def test_sing():
	origin_lat = 22.167615
	origin_lng = 113.908514
	lat = 22.289666
	lng = 114.145099
	print('\n====== Sing - GPS (lat,lng) to (x,y) ======')
	#1st way to convert GPS to xy coordinate
	x = Location(originlat=origin_lat, originlng=origin_lng).distanceX_v2(lat=22.289666,lng=114.145099)
	y = Location(origin_lat, origin_lng).distanceY_v2(22.289666,114.145099)
	#2nd way to convert GPS to xy coordinate
	xy = Location(originlng=origin_lat, originlat=origin_lng).convertGPS2XY_v2(lat=22.289666,lng=114.145099)
	print('GPS lat:\t{0:f}'.format(lat))
	print('GPS lng:\t{0:f}'.format(lng))
	print('converted x:\t{0:f}'.format(x))
	print('converted y:\t{0:f}'.format(y))
	print('converted xy:\t{0}'.format(xy))

	print('\n====== Sing - Distance between two xy/GPS ======')
	coordsys = Location(22.167615, 113.908514)
	xy1 = {'x':0,'y':0}
	xy2 = {'x':1,'y':1}
	xy_distance = coordsys.distance_btw2xy(x1=xy1['x'],y1=xy1['y'], x2=xy2['x'],y2=xy2['y'])

	print('xy1:\t\t{0},{1}'.format(xy1['x'],xy1['y']))
	print('xy2:\t\t{0},{1}'.format(xy2['x'],xy2['y']))
	print('xy dist:\t{0}'.format(xy_distance))

	gps1 = {'lat':22.293210, 'lng':114.172877}
	gps2 = {'lat':22.293025, 'lng':114.173606}
	gps_distance = coordsys.distance_btw2gps(lat1=gps1['lat'], lng1=gps1['lng'], lat2=gps2['lat'], lng2=gps2['lng'])
	print()
	print('gps1:\t\t{0:f}, {1:f}'.format(gps1['lat'], gps1['lng']))
	print('gps2:\t\t{0:f}, {1:f}'.format(gps2['lat'], gps2['lng']))
	print('gps dist:\t{0}'.format(gps_distance))
	print()


""" Testing """
# test_sing()
# demo_xy2gps(originlat=22.167615, originlng=113.908514, x=24347.241376, y=13562.931225)
