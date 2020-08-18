"""
Functions::
Perform Linear Least Squared LLS localization algorithm to find
1. estimated target location (theta, list[x, y, x^2+y^2])
2. location error (distance between real location and LLS estimated location)
3. the distance between the LLS estimated target location and each base station
"""


""" ======== import module <BEGIN> ======== """
import numpy
import math
import itertools # Find combination of the input
# from myMBREC import MBRE

""" ======== import module <END> ======== """

""" ======== import self module <BEGIN> ======== """
#Import module by two ways. Take the below link as reference
# ==> https://stackoverflow.com/questions/8718885/import-module-from-string-variable
try: #For internal testing in this module 
	import RadioPropagation_v2 as myRadioPropagation
except ModuleNotFoundError as err:
	pass
try: #For external use in the outside .py
	from self_pkg import RadioPropagation_v2 as myRadioPropagation
except ModuleNotFoundError as err:
	pass

err_1 = err_2 = str()
try: #For external use in the outside .py
	from self_pkg import CoordinateSystem_v2 as myCoordinateSystem
except ModuleNotFoundError as err:
    err_1 = str(err)
try: #For internal testing in this module 
	import CoordinateSystem_v2 as myCoordinateSystem
except ModuleNotFoundError as err:
    err_2 = str(err)
#Check whether the self-module imported successfully or not
if (err_1 and err_2):
	#unsuccessful, tell users if the self-module cannot be imported
    print("\nUnsuccessful to import self-module 'CoordinateSystem_v2.py'.")
    print("The file name or the path of the module may be changed.")
    print("\nError code: \t{0}\n\t\t{1}".format(err_1,err_2))
""" ======== import self module <END> ======== """


class LLS(object):
	"""
	Just need to input either the GPS (bsCoordinateLat, bsCoordinateLng) OR x,y coordinate (bsCoordinateX, bsCoordinateY) of the BS.\n
	alpha: type `float`	\n
	Z0: type `float`	\n
	originLat: type `float`, default value = 22.167615. The GPS latitude of the origin. \
				Origin of X-Y coordinate system: GPS(22.167615, 113.908514), Tai a Chau Landing No. 2, 大鴉洲2號梯台	\n
	originLng: type `float`, default value = 113.908514. The GPS longitude of the origin. \
				Origin of X-Y coordinate system: GPS(22.167615, 113.908514), Tai a Chau Landing No. 2, 大鴉洲2號梯台	\n
	bsCoordinateX: type `list`, `float` inside. The x coordinates of the base stations. The sequence of the x coords must be same as the y coords.
	 e.g. bsCoordinateX 
	 \t= [uint(bs1_x_coordinate), uint(bs2_x_coordinate), ...] 
	 \t= [12322, 32424, 12312,...]
	bsCoordinateY: type `list`, `float` inside. The y coordinates of the base stations. The sequence of the x coords must be same as the y coords.
	 e.g. bsCoordinateY 
	 \t= [uint(bs1_y_coordinate), uint(bs2_y_coordinate), ...] 
	 \t= [6523, 2342, 5433,...]
	bsCoordinateLat: type `list`, `float` inside. The GPS latitude the base stations. The sequence of the x coords must be same as the y coords.
	 e.g. bsCoordinateLat 
	 \t= [uint(bs1_lat), uint(bs2_lat), ...] 
	 \t= [22.123, 22.5323, 22.765,...]
	bsCoordinateLng: type `list`, `float` inside. The GPS longitude of the base stations. The sequence of the x coords must be same as the y coords.
	 e.g. bsCoordinateLng 
	 \t= [uint(bs1_lng), uint(bs2_lng), ...] 
	 \t= [114.534, 114.234, 114.7567,...]
	measuredRssi: type `list`, `float` inside. The measured RSSI values of the base stations. The sequence of the RSSI values must be the same as the BS coordinates.
	 e.g. measuredRssi 
	 \t= [int(bs1_rssi), int(bs2_rssi), ...] 
	 \t= [-113, -98, -87, ...]
	targetRealCoordinate: type `list`, `float` inside. The converted (x,y) coordinate of the actual device location, based on GPS.
	 e.g. targetRealCoordinate 
	 \t= [float(target_x_coor), float(target_y_coor)] 
	 \t= [1231, 2343]
	targetRealGPS: type `list`, `float` inside. The GPS of the actual device location.
	 e.g. targetRealGPS 
	 \t= [float(target_lat), float(target_lng)] 
	 \t= [22.300567, 114.178874]
	"""
	alpha = float()	#path loss exponent, ideal_alpha = 2.449320295			## From Leung Ki Fung (2018-2019):/Sigfox localization/Final_Analysis/Analysis.py
	Z0 = float()	#reference RSSI, ideal_Reference_RSSI = -36.15657229	##
	originLat = 22.167615	#Origin of X-Y coordinate system: GPS(22.167615, 113.908514), Tai a Chau Landing No. 2, 大鴉洲2號梯台
	originLng = 113.908514	#
	bsCoordinateX = list()	#(x, y) coordinates of the base stations, which measure RSSI
	bsCoordinateY = list()	#
	measuredRssi = list()	#RSSI values measured by base stations
	targetRealCoordinate = list()  #the converted (x,y) coordinate of the actual device location, based on GPS

	#Origin of X-Y coordinate system: GPS(22.167615, 113.908514), Tai a Chau Landing No. 2, 大鴉洲2號梯台
	def __init__(self,alpha=2.5,Z0=-33.0,originLat=22.167615,originLng=113.908514,
				bsCoordinateX=None,bsCoordinateY=None,bsCoordinateLat=None,bsCoordinateLng=None,
				measuredRssi=list,targetRealCoordinate=None,targetRealGPS=None):
		self.alpha = alpha
		self.Z0 = Z0
		self.bsCoordinateX = bsCoordinateX
		self.bsCoordinateY = bsCoordinateY
		self.bsCoordinateLat = bsCoordinateLat
		self.bsCoordinateLng = bsCoordinateLng
		self.measuredRssi = measuredRssi
		self.targetRealCoordinate = targetRealCoordinate
		self.targetRealGPS = targetRealGPS

	def matrixA(self): #pass a list of coordinates to the matrix A
		bs_x = self.bsCoordinateX
		bs_y = self.bsCoordinateY
		a = []
		# sp_coor = []
		# sp_coor = bsCoordinate.split(";")  #["x1,y1"]--list ele1 ["x2,y2"]--list ele2...so on
		for i in range(len(bs_x)):
			# aa = []
			# splited = sp_coor[i]     #for i = 1 handle the 1st ele ,["x1,y1"]-->[x1]--list ele1 [x2]--list ele2
			# aa = splited.split(",")
			##By Ka Ho report, p.15, equation (2.16)
			aaa = []
			aaa.append(-2.0*float(bs_x[i]))
			aaa.append(-2.0*float(bs_y[i]))
			aaa.append(1)
			a.append(aaa)
		a = numpy.matrix(a)
		return a

	def matrixB(self):
		Z0 = self.Z0
		alpha = self.alpha
		m_rssi = self.measuredRssi
		bs_x = self.bsCoordinateX
		bs_y = self.bsCoordinateY
		# m_rssi = []
		# m_rssi = measuredRssi.split(",")
		# sp_coor = []
		# sp_coor = bsCoordinate.split(";")
		b = []
		for i in range(len(m_rssi)):
			# aa = []
			# splited = sp_coor[i]     #for i = 1 handle the 1st ele ,["x1,y1"]-->[x1]--list ele1 [x2]--list ele2
			# aa = splited.split(",")  # aa's length is the same as m_rssi[]
			temp = (2/(10*alpha))*(Z0-float(m_rssi[i])) #m_rssi = splited measured rssi in the form of [rssi1,rssi2...]
			temp = pow(10,temp)
			temp = temp - pow(float(bs_x[i]),2) - pow(float(bs_y[i]),2)
			b.append(temp)
		b = numpy.matrix(b).T
		return b

	def Agum(self):
		a = self.matrixA()
		aT = a.T		#By Ka Ho report, p.16, equation (2.21)
		temp = aT*a
		temp = temp.I
		aInv = temp*aT
		return aInv

	def theta(self):
		"""
		Return the LLS estimated target location in list(x_coor, y_coor, value of 'x^2+y^2')
		"""
		Agumm = self.Agum()
		b = self.matrixB()
		theta = Agumm * b
		# return {'x':theta.item(0), 'y':theta.item(1), 'x^2+y^2':theta.item(2)}
		return theta

	def locationError(self):#, targetRealCoordinate=list()):
		"""
		Find the distance between the real location and LLS estimated location
		"""
		theta = self.theta()
		estLocX = theta.item(0)
		estLocY = theta.item(1)
		#print(estLoc[0]) --> x of the estimated location
		# tar = targetRealCoordinate
		tar = self.targetRealCoordinate
		LEsqt = pow((float(estLocX)-float(tar[0])),2) + pow((float(estLocY)-float(tar[1])),2) #((x2-x1)^2+(y2-y1)^2)^1/2
		LLSErr = math.sqrt(LEsqt)
		return LLSErr

	def distToTarget(self):
		"""
		Find the distance between each base station and the LLS estimated target location
		"""

		tar = self.targetRealCoordinate
		bs_coor_x = self.bsCoordinateX
		bs_coor_y = self.bsCoordinateY
		# target1 = tar.split(",")
		# sp_coor = []
		# sp_coor = bsCoordinate.split(";")  #["x1,y1"]--list ele1 ["x2,y2"]--list ele2...so on
		for i in range(len(bs_coor_x)):
			# aa = []
			# splited = sp_coor[i]     #for i = 1 handle the 1st ele ,["x1,y1"]-->[x1]--list ele1 [x2]--list ele2
			# aa = splited.split(",")
			temp = pow(int(bs_coor_x[i])-int(tar[0]),2)+pow(int(bs_coor_y[i])-int(tar[1]),2)
			temp1 = math.sqrt(temp)
			print("The distance between BS "+str(i+1)+" and the target is: "+ str(temp1)+ " m ")
		return
	
	def allResults(self) -> dict:
		""" Use the input (x,y) coordinates of the BS, alpha, reference RSSI and measured RSSI to perform LLS to estimate the location of the target.
		Return a dict
		----------
		1. path loss exponent
		2. reference rssi
		3. estimated (x,y) coordinate by the LLS localization
		4. location error (distance) between the real and estimated location, based on (x,y)
		"""
		alpha = self.alpha			#Path loss exponent
		referenceRssi = self.Z0		#Reference RSSI
		theta = self.theta()		#The LLS estimated location (x,y)
		estLocX = theta.item(0)		#x coordinate
		estLocY = theta.item(1)		#y coordinate
		locError = self.locationError()	#The distance between the real and estimated location, based on (x,y)

		results = {'alpha':alpha, 'referenceRssi':referenceRssi, 'llsX':estLocX, 'llsY':estLocY, 'LE':locError}
		return results
		
	def allResultsGPS(self) -> dict:
		""" Use the input GPS(lat,lng) of the BS, alpha, reference RSSI and measured RSSI to perform LLS to estimate the location of the target.
		Return a dict
		----------
		1. path loss exponent
		2. reference rssi
		3. estimated (x,y) coordinate and GPS (lat,lng) by the LLS localization
		4. location error (distance) between the real and estimated location, based on (x,y)
		
		Illustration of this function
		----------
		1. Convert (1) BS GPS and (2) device GPS to (x,y) based on an origin
		2. Save the converted (x,y)
		3. Perform LLS by the converted BS (x,y) & device (x,y) and RSSI
		4. Get the LLS result & LE, and then convert the (x,y) back to GPS
		"""

		#Convert BS GPS to (x,y)
		coordsys = myCoordinateSystem.Location(originlat=self.originLat,originlng=self.originLng)
		self.bsCoordinateX = list()
		self.bsCoordinateY = list()
		for index in range(len(self.bsCoordinateLat)):
			xy = coordsys.convertGPS2XY_v2(lat=self.bsCoordinateLat[index],lng=self.bsCoordinateLng[index])
			self.bsCoordinateX.append(xy['x'])
			self.bsCoordinateY.append(xy['y'])
		#Convert the device GPS to (x,y)
		xy = coordsys.convertGPS2XY_v2(lat=self.targetRealGPS[0],lng=self.targetRealGPS[1])
		self.targetRealCoordinate = [xy['x'], xy['y']]
		##Perform LLS
		alpha = self.alpha			#Path loss exponent = the input
		referenceRssi = self.Z0		#Reference RSSI = the input
		theta = self.theta()		#The LLS estimated location (x,y)
		estLocX = theta.item(0)		#LLS estimated x coordinate
		estLocY = theta.item(1)		#LLS estimated y coordinate
		locError = self.locationError()	#The distance between the real and estimated location, based on (x,y)
		##Convert LLS (x,y) to GPS(lat,lng)
		gps = coordsys.convertXY2GPS(dX=estLocX,dY=estLocY)
		estLocLat = gps.latitude
		estLocLng = gps.longitude

		results = {'alpha':alpha, 'referenceRssi':referenceRssi, 'llsX':estLocX, 'llsY':estLocY, 
					'llsLat':estLocLat, 'llsLng':estLocLng, 'LE':locError}
		return results

	def allResultsGPS_nCr(self) -> dict:
		"""Perform LLS to estimate location of the target. Use the combination to find out the best path loss exponent (alpha) and reference RSSI (z0) before performing LLS\n
		i.e. the alpha and z0 give the lowest localization error.
		
		Return a dict
		----------
		1. the best path loss exponent
		2. the best reference rssi
		3. estimated (x,y) coordinate and GPS (lat,lng) by the LLS localization
		4. the lowest location error (distance between the real and estimated target location), based on (x,y)

		Algorithm
		----------
		1. Find the combination of the BS, i.e. nCr, where n = number of BS, r = 2 = because only two RSSI and two distances between target and BS are needed to find alpha and reference RSSI.
			i.e. two nCr RSSI and two nCr distances between BS and target
		2. Calculate the nCr alpha and nCr z0 by the combination of the BS.
		3. Perform LLS to find the localization error (distance bewteen tagert real location and LLS estimated target location) by the nCr alpha and nCr z0.
		4. Find the best alpha and the best reference RSSI by comparing the localization error, lowest LE gives the best alpha and z0.
		"""

		#1. 
		#Find the combinations of the BS, nCr, n=number of bs, r=2
		bs_index = [i for i in range(len(self.bsCoordinateLat))]
		comb = itertools.combinations(bs_index, 2)	#find the combinations, nCr
		nCr_bs_index = list(comb)					#= [(BS0,BS1),(BS0,BS2),...,(BS0,BSn),(BS1,BS2),(BS1,BS3),...]
		# print(nCr_bs_index)

		#2.
		#Calculate the path loss exponent (alpha) and reference RSSI (z0) from the combinations of BS
		nCr_alpha = list()
		nCr_z0 = list()
		coordsys = myCoordinateSystem.Location(originlat=self.originLat,originlng=self.originLng)
		print("Finding nCr alpha and nCr reference RSSI. nCr = (numb of BS)C(2) = ({})C(2) = {} ".format(len(bs_index),len(nCr_bs_index)))
		# print("\tnCr = (numb of BS)C(2) = ({})C(2) = {} ".format(len(bs_index),len(nCr_bs_index)), end="")
		for bs_index in nCr_bs_index: #In each combination of the BS, find the relavant alpha and reference RSSI
			# print(".",end="")
			# print(bs_index, end =" ")	#e.g. bs_index = tuple(BS2,BS14)
			target_lat = self.targetRealGPS[0]
			target_lng = self.targetRealGPS[1]
			bs1_lat = self.bsCoordinateLat[bs_index[0]]
			bs1_lng = self.bsCoordinateLng[bs_index[0]]
			bs1_rssi = self.measuredRssi[bs_index[0]]
			bs2_lat = self.bsCoordinateLat[bs_index[1]]
			bs2_lng = self.bsCoordinateLng[bs_index[1]]
			bs2_rssi = self.measuredRssi[bs_index[1]]
			dist_target_to_bs1 = coordsys.distance_btw2gps(lat1=bs1_lat,lng1=bs1_lng, lat2=target_lat,lng2=target_lng)
			dist_target_to_bs2 = coordsys.distance_btw2gps(lat1=bs2_lat,lng1=bs2_lng, lat2=target_lat,lng2=target_lng)
			bs1_expected_rssi = myRadioPropagation.log_Normal_RSSI_With_Distance(distance=dist_target_to_bs1)
			bs2_expected_rssi = myRadioPropagation.log_Normal_RSSI_With_Distance(distance=dist_target_to_bs2)
			# print("real: {},{}".format(target_lat,target_lng))
			# print("bs1: {},{}; rssi={}; cal rssi={}; dist(target & BS1)={}".format(bs1_lat,bs1_lng,bs1_rssi,bs1_expected_rssi,dist_target_to_bs1))
			# print("bs2: {},{}; rssi={}; cal rssi={}; dist(target & BS2)={}".format(bs2_lat,bs2_lng,bs2_rssi,bs2_expected_rssi,dist_target_to_bs2))
			
			alpha = myRadioPropagation.findAlpha(rssi1=bs1_rssi,rssi2=bs2_rssi,distance1=dist_target_to_bs1,distance2=dist_target_to_bs2)
			z0 = myRadioPropagation.findRefRSSI(alpha,dist_target_to_bs1,bs1_rssi)
			if (z0 < 0 and alpha>2 and alpha<10):
				nCr_alpha.append(alpha)
				nCr_z0.append(z0)

		#3.
		#Perfrom LLS. Find the best alpha and reference RSSI by the lowest LE.
		lls_result_list = list()
		loc_err_list = list()
		##The combinations of the alpha and reference RSSI
		##= list(tuple(a,b),tuple(a,c),...) = [(A0,Z0_0),(A0,Z0_1),...,(A0,Z0_m),(A1,Z0_0),(A1,Z0_1),...,(An,Z0_m)]
		nCr_alpha_z0 = list(itertools.product(nCr_alpha, nCr_z0))
		print("Finding the best alpha and reference RSSI. nCr = ({})C({}) = {} ".format(len(nCr_alpha),len(nCr_z0),len(nCr_alpha_z0)))
		for index in range(len(nCr_alpha_z0)): #in each combination of the alpha and reference RSSI, perform LLS
			a_alpha = nCr_alpha_z0[index][0]
			a_z0 = nCr_alpha_z0[index][1]
			performLLS = LLS(alpha = a_alpha, Z0=a_z0, bsCoordinateLat=self.bsCoordinateLat, bsCoordinateLng=self.bsCoordinateLng,
						measuredRssi=self.measuredRssi, targetRealGPS=[self.targetRealGPS[0],self.targetRealGPS[1]])
			lls_result_list.append(performLLS.allResultsGPS())	#the function returns a dict, store the LLS result (dict) into a list
			loc_err_list.append(performLLS.allResultsGPS()['LE']) 	#store the LE (float) into a list
			# print((index+1)%20, end=" ")
			if ((index)%20 >= 19):
				print(".",end="")
			# print(index, end =" ")
			# print(a_alpha)
			# print(a_z0)
		print()
		# print(type(nCr_alpha_z0))	#type: list
		# print(type(nCr_alpha_z0[0])) #type: tuple
		# print(len(nCr_alpha))
		# print(len(nCr_z0))
		lowest_LE = min(loc_err_list)
		highest_LE = max(loc_err_list)
		worst_lls_result = lls_result_list[loc_err_list.index(highest_LE)]
		index_best_lls_result = loc_err_list.index(lowest_LE)
		best_lls_result = lls_result_list[index_best_lls_result] #type: dict
		best_alpha = best_lls_result['alpha']
		best_z0 = best_lls_result['referenceRssi']
		best_estLocX = best_lls_result['llsX']
		best_estLocY = best_lls_result['llsY']
		best_estLocLat = best_lls_result['llsLat']
		best_estLocLng = best_lls_result['llsLng']

		result = {'alpha':best_alpha, 'referenceRssi':best_z0, 'llsX':best_estLocX, 'llsY':best_estLocY, 
					'llsLat':best_estLocLat, 'llsLng':best_estLocLng, 'LE':lowest_LE, 'worstLLS':worst_lls_result}
		print("Finished. Best alpha {} z0 {} LE {}".format(best_alpha,best_z0,lowest_LE))
		return result

def get_test_data():
	received_data_testlist = [
		['DateRecorded', 'TimeRecorded', 'seqNumber', 'station', 'rssi', 'snr', 'data', 'avgSnr', 'duplicate', 'time', 'lat', 'lng', 'device', 'BaseStationLat', 'BaseStationLng', 'BaseStationHeight', 'BaseStationRegion', 'SubDistrict', 'BaseStationX', 'BaseStationY', 'OriginGPSLat', 'OriginGPSLng'], 
		['2020/03/01', '17:26:16', 1292, '8042id', -96, 6.06, '01542b0406ce238800000000', 10.28, False, 1581932606, 22, 114, '3E81CB', 22.279137, 114.179943, 75, 'Hong Kong Island', 'Wan Chai', 27933.0776, 12392.8949, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '79CDid', -115, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.310727, 114.171904, 24, 'Kowloon', 'xxx', 27105.7749, 15903.3372, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '8142id', -120, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.242992, 114.156972, 110, 'Hong Kong Island', 'Ap Lei Chau', 25569.1055, 8376.27768, 22.167615, 113.908514],
		['2020/03/01', '17:29:44', 1292, '7A06id', -114, 6.47, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.317657, 114.177256, 38, 'Kowloon', 'xxx', 27656.5554, 16673.4343, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '8117id', -97, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.286144, 114.192657, 83, 'Hong Kong Island', 'Fortress Hill', 29241.4899, 13171.5486, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '7C86id', -108, 6.34, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.312852, 114.189953, 28, 'Kowloon', 'xxx', 28963.2182, 16139.4781, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '6E12id', -113, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.322607, 114.163759, 50, 'Kowloon', 'xxx', 26267.5635, 17223.5036, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '79BFid', -98, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.316259, 114.170827, 83, 'Kowloon', 'xxx', 26994.9396, 16518.0814, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '7F1Fid', -99, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.277171, 114.176302, 71, 'Hong Kong Island', 'Wan Chai', 27558.3781, 12174.4229, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '7C4Bid', -111, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.33574, 114.177952, 34, 'Kowloon', 'xxx', 27728.1815, 18682.9097, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '7B21id', -94, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.315007, 114.168829, 80, 'Kowloon', 'xxx', 26789.3231, 16378.9527, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '80C7id', -98, 6.77, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.292768, 114.206999, 77, 'Hong Kong Island', 'North Point', 30717.4415, 13907.6413, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '6DEBid', -82, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.286528, 114.151484, 87, 'Hong Kong Island', 'Sheung Wan', 25004.3291, 13214.2206, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '7C43id', -90, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.297508, 114.170744, 53, 'Kowloon', 'xxx', 26986.3979, 14434.3744, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '7F0Fid', -117, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.307672, 114.182495, 27, 'Kowloon', 'xxx', 28195.7069, 15563.85, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '810Fid', -99, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.309703, 114.188485, 45, 'Kowloon', 'xxx', 28812.1446, 15789.5451, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '7C52id', -115, 6.09, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.319801, 114.182988, 34, 'Kowloon', 'xxx', 28246.4421, 16911.6865, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '8041id', -98, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.286859, 114.149116, 75, 'Hong Kong Island', 'Sheung Wan', 24760.6355, 13251.003, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '790Cid', -100, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.291644, 114.20396, 84, 'Hong Kong Island', 'North Point', 30404.6946, 13782.7367, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '814Eid', -125, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.35271, 114.127076, 22, 'New Territories', 'xxx', 22492.4735, 20568.7029, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '8141id', -104, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.330951, 114.172098, 26, 'Kowloon', 'xxx', 27125.7396, 18150.7315, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '7F10id', -102, 6.19, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.33037, 114.205824, 108, 'Kowloon', 'xxx', 30596.521, 18086.1678, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '8112id', -109, 6.12, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.350155, 114.110168, 56, 'New Territories', 'xxx', 20752.4515, 20284.7782, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '7A4Eid', -80, 6.12, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.278494, 114.160487, 193, 'Hong Kong Island', 'Central', 25930.8383, 12321.4415, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '8043id', -102, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.315538, 114.216895, 36, 'Kowloon', 'xxx', 31735.8502, 16437.9602, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '6BFEid', -123, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.362571, 114.134226, 90, 'New Territories', 'xxx', 23228.2883, 21664.5076, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '7A65id', -114, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.337558, 114.200459, 78, 'Kowloon', 'xxx', 30044.4027, 18884.9352, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '8114id', -111, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.353631, 114.107478, 93, 'New Territories', 'xxx', 20475.6205, 20671.0491, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '7F27id', -89, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.300567, 114.178874, 39, 'Kowloon', 'xxx', 27823.0656, 14774.3061, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '7C54id', -75, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.288257, 114.190804, 126, 'Hong Kong Island', 'Fortress Hill', 29050.7956, 13406.3559, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '6C6Bid', -99, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.308348, 114.234173, 102, 'Kowloon', 'xxx', 33513.9487, 15638.9706, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '7C59id', -113, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.284465, 114.138754, 38, 'Hong Kong Island', 'Sai Ying Pun', 23694.2701, 12984.9695, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '6DEDid', -116, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.323885, 114.254535, 132, 'New Territories', 'xxx', 35609.4251, 17365.5215, 22.167615, 113.908514], 
		['2020/03/01', '17:29:44', 1292, '7C6Bid', -110, 6, '01542b0406ce238800000000', 11.92, True, 1581932606, 22, 114, '3E81CB', 22.330934, 114.222528, 24, 'Kowloon', 'xxx', 32315.5486, 18148.8424, 22.167615, 113.908514]
		]
	return received_data_testlist

def test_xy_version():
	import pandas as pd
	test_data_list = get_test_data()
	col_names = test_data_list.pop(0)
	df = pd.DataFrame(test_data_list,columns=col_names)
	bs_coor_x = df['BaseStationX']
	bs_coor_y = df['BaseStationY']
	measured_rssi = df['rssi']
	device_real_x = 1 #a fake value
	device_real_y = 1 #a fake value
	performLLS = LLS(alpha = 2.5, Z0=-33, bsCoordinateX=bs_coor_x, bsCoordinateY=bs_coor_y,
						measuredRssi=measured_rssi, targetRealCoordinate=[device_real_x,device_real_y])
	llsResults = performLLS.allResults()
	print()
	print(llsResults)
	print()

def test_gps_version():
	import pandas as pd
	test_data_list = get_test_data()
	col_names = test_data_list.pop(0)
	df = pd.DataFrame(test_data_list,columns=col_names)
	bs_coor_lat = df['BaseStationLat']
	bs_coor_lng = df['BaseStationLng']
	measured_rssi = df['rssi']
	device_gps_lat = 22.293210 #true value
	device_gps_lng = 114.172877 #true value
	performLLS = LLS(alpha = 2.5, Z0=-33, bsCoordinateLat=bs_coor_lat, bsCoordinateLng=bs_coor_lng,
						measuredRssi=measured_rssi, targetRealGPS=[device_gps_lat,device_gps_lng])
	llsResults = performLLS.allResultsGPS()
	print()
	print(llsResults)
	print()

def test_getResultGPS_nCr():
	import pandas as pd
	test_data_list = get_test_data()
	col_names = test_data_list.pop(0)
	df = pd.DataFrame(test_data_list,columns=col_names)
	bs_coor_lat = df['BaseStationLat']
	bs_coor_lng = df['BaseStationLng']
	measured_rssi = df['rssi']
	device_gps_lat = 22.293210 #true value
	device_gps_lng = 114.172877 #true value
	performLLS = LLS(alpha = 2.5, Z0=-33, bsCoordinateLat=bs_coor_lat, bsCoordinateLng=bs_coor_lng,
						measuredRssi=measured_rssi, targetRealGPS=[device_gps_lat,device_gps_lng])
	llsResults = performLLS.allResultsGPS_nCr()
	print()
	print(llsResults)
	print()

""" Test """
# print('\n=== xy version =======')
# test_xy_version()
# print('\n=== GPS lat lng version =======')
# test_gps_version()
# print('\n=== nCr find the best alpha and reference RSSI =======')
# test_getResultGPS_nCr()