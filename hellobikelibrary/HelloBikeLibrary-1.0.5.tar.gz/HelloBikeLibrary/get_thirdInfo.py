# -*- coding: utf-8 -*-
# @Author: yongfanmao
# @Date:   2020-08-19 16:30:39
# @E-mail: maoyongfan@163.com
# @Last Modified by:   yongfanmao
# @Last Modified time: 2020-08-19 20:13:54

from robot.api import logger
from HelloBikeLibrary.request import Request
from HelloBikeLibrary.con_mysql import UseMysql
import json


"""
采集第三方信息
"""

class ThirdInfo(object):

	def get_container_ip(self,service_name,env="uat",tag="group1"):

		"""
			获取指定服务容器的对应IP地址
			env 不传默认为uat
			tag 不传默认为group1
			
			返回内容为:
				

			例:
			|$(ip) |get container ip | AppHellobikeOpenlockService | env="uat" | tag="group1"
		"""
		try:
			if env == "fat":
				groupsUrl = "https://gaia.hellobike.cn/container-business-service/api/v1/apps/groups/appname/{}/env/6".format(service_name)
				containerUrl = "https://gaia.hellobike.cn/container-business-service/api/v1/apps/pods/appname/{service_name}/env/6/group/{tag}".format(
				service_name=service_name,tag=tag)
			else:
				groupsUrl = "https://gaia.hellobike.cn/container-business-service/api/v1/apps/groups/appname/{}/env/2".format(service_name)
				containerUrl = "https://gaia.hellobike.cn/container-business-service/api/v1/apps/pods/appname/{service_name}/env/2/group/{tag}".format(
				service_name=service_name,tag=tag)
			print(groupsUrl)
			us = UseMysql()
			headerInfos = us.getTokenInfos()
			headers = {"token": headerInfos[0],"user-agent":headerInfos[1]}
			grRep = Request().request_client(url=groupsUrl,method='get',headers=headers)
			if grRep[0] == 200:
				groupList = grRep[1].get('data').get('groupList',[])
				for group in groupList:
					if group == tag:
						break
				else:
					return  False#("没有容器信息,请联系管理员")


			

			print(containerUrl)

			cnRep = Request().request_client(url=containerUrl,method='get',headers=headers)
			print (cnRep)

			if cnRep[0] == 200:
				ip = cnRep[1].get('data').get('appPodList',[])[0].get("ipAddress")
				print(ip)
				return ip

			return False
		except Exception as e:
			raise Exception("请联系管理员")





if __name__ == '__main__':
	td = ThirdInfo()
	td.get_container_ip("AppHelloVenusApi",env="fat")




