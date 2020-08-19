#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import traceback
import logging
import json
import datetime


class Apollo_Api(object):
    '''
    接口使用示例
    接口提供了增删改查
    from apolloapi.ApolloClass import Apollo_Api
    import config as my_cfg

    anji_api = Apollo_Api(apollo_url, user, pwd)
    其中 apollo_url 为 apollo 的 port地址；
    user 和 pwd 为用户名密码，用户名默认为 apollo
    另外需要创建配置文件，配置文件名自定义；
    内容为：

    # -*- coding: utf-8 -*-
    #saic
    apollo_api_saic = "http://10.191.0.39:9500"
    saic_user = "xxxxx"
    saic_pwd = "xxxx"
    可以定义多个配置
    '''

    def __init__(self, apollo_url, user, password):
        self.apollo_url = apollo_url
        self.headers = {'Content-Type': 'application/json;charset=UTF-8'}
        self.route = "/openapi/v1/envs"
        self.user = user
        self.session = self.apolloLogin(password)

    def apolloLogin(self, password):
        userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        header = {
        'User-Agent': userAgent,
        "Content-Type": "application/x-www-form-urlencoded"
        }
        postData = {
            "username": self.user,
            "password": password
        }
        url = "{url}/signin".format(
            url=self.apollo_url)
        session = requests.Session()
        res = session.post(url, data=postData, headers=header)
        if res.status_code == 200:
            return session
        else:
            print("Error message: Failed to login")
            exit(1)

    '''创建新项目'''
    def createApolloProject(self, appId, name, orgId, orgName, ownerName):
        # session = self.apolloLogin()
        createurl = "{url}/apps".format(
            url=self.apollo_url
            )
        create_data = dict(
            appId=appId,
            name=name,
            orgId=orgId,
            orgName=orgName,
            ownerName=ownerName
            )
        d = self.session.post(createurl, headers=self.headers, data=json.dumps(create_data)) #, cookies=cookies)
        if d.status_code == 200:
            print("{} 创建成功!".format(appId))
        else:
            print(d.status_code, "{} 创建失败!".format(appId))

    '''创建集群'''
    def createCluster(self, appId, env, clusterName):
        url = "{url}/apps/{appId}/envs/{env}/clusters".format(
            url=self.apollo_url,
            appId=appId,
            env=env.upper())
        cluster_data = dict(
            appId=appId,
            name=clusterName)
        print(url)
        res =  self.session.post(url, headers=self.headers, data=json.dumps(cluster_data))
        if res.status_code == 200:
            print("{appId}: 集群{clusterName}创建成功 {env}".format(
                appId=appId,
                clusterName=clusterName,
                env=env))
        else:
            print(res.status_code, res.text)


    def getAppidList(self):
        '''
        获取apollo所有appid列表
        '''
        applist = []
        #第一页
        oneUrl = "{url}/apps/by-owner?owner=apollo".format(url=self.apollo_url)
        data = self.session.get(oneUrl).json()
        for i in data:
            applist.append(i)

        #列出所有apollo项目列表
        page = 1
        while True:
            url = "{url}/apps/by-owner?owner=apollo&page={p}&size=10".format(
            url=self.apollo_url,
            p=str(page))
            res = self.session.get(url)
            if len(res.json()) == 0:
                break
            for i in res.json():
                if "feichenxue" not in i['appId']:
                    applist.append(i)
            page+=1
        return applist

    def findProject(self, appId):
        url = "{url}/apps/{appId}".format(
            url=self.apollo_url,
            appId=appId)
        try:
            res = self.session.get(url)
            if res.json():
                return res.json()
        except Exception as e:
            return False


    def findProject_info(self, appId, env, clusterName="default"):
        url = "{url}/apps/{appId}/envs/{env}/clusters/{clusterName}/namespaces".format(
            url=self.apollo_url,
            appId=appId,
            env=env.upper(),
            clusterName=clusterName)
        try:
            res = self.session.get(url)
            if res.json():
                return res.json()
        except Exception as e:
            return False

    def deleteCluster(self, appId, clusterName, env):
        url = "{url}/apps/{appId}/envs/{env}/clusters/{clusterName}".format(
            url=self.apollo_url,
            appId=appId,
            clusterName=clusterName,
            env=env.upper())
        res = self.session.delete(url)
        retcode = res.status_code
        if retcode == 404:
            print("{appId}: The {clusterName} cluster is not found, check to see if it exists".format(
                appId=appId,
                clusterName=clusterName))
        elif retcode == 200:
            print("{appId}: {clusterName} delete successd!")


    def deploy_appid_cfg(self, appid, app_env, comment, namespaceName="application", clustersName="default"):
        try:
            deploy_api_url = "{apollo_url}/apps/{appId}/envs/{env}/clusters/{clusterName}/namespaces/{namespaceName}/releases".format(
                apollo_url=self.apollo_url,
                appId=appid,
                env=app_env.upper(),
                clusterName=clustersName,
                namespaceName=namespaceName
                )

            #获取发布时间
            now = datetime.datetime.now()
            nowtime = now.strftime('%Y%m%d%H%M%S')
            releaseTitle = nowtime + "-release"

            deploy_data = dict(
                releaseTitle=releaseTitle,
                releaseComment=comment,
                releasedBy=self.user
                )
            deploy_info = self.session.post(deploy_api_url, headers=self.headers, data=json.dumps(deploy_data))
            if deploy_info.status_code == 200:
                print("发布成功: ", deploy_info.json())
                return True
        except Exception as e:
            print(e)
            return False

    def add_appid_cfg(self, appid, app_env, key, value, comment, namespaceName="application", clustersName="default"):
        addkeys = "create"
        add_api_url = "{apollo_url}/apps/{appId}/envs/{app_env}/clusters/{clusterName}/namespaces/{namespaceName}/item".format(
                apollo_url=self.apollo_url,
                app_env=app_env.upper(),
                appId=appid,
                clusterName=clustersName,
                namespaceName=namespaceName)

        #构建添加配置所需的数据
        add_data = dict(
                 key=key,
                 value=value,
                 comment=comment,
                 dataChangeCreatedBy=self.user,
                 addItemBtnDisabled=True,
                 tableViewOperType=addkeys)
        try:
            add_cfg = self.session.post(add_api_url, headers=self.headers, data=json.dumps(add_data))
            retcode = add_cfg.status_code
            result = add_cfg.json()
            if retcode == 200:
                print("添加成功!!!", result)
            elif result['message'] == 'item already exist':
                res = self.update_appid_cfg(appid, app_env, add_data, namespaceName, clustersName)
                if res:
                    print("update info: appId: {app}, key: {key}, value: {value}".format(
                        app=appid,
                        key=key,
                        value=value))
        except Exception as e:
            print(e)

    def update_appid_cfg(self, appid, app_env, add_data, namespaceName="application", clustersName="default"):
        try:
            data = self.findProject_info(appid, app_env, clustersName)
            for app in data[0]['items']:
                key = app['item']['key'] 
                if key == add_data["key"]:
                    add_data['id'] = app['item']['id']
                    add_data['namespaceId'] = app['item']['namespaceId']
                    add_data['lineNum'] = app['item']['lineNum']
                    add_data['dataChangeCreatedTime'] =  app['item']['dataChangeCreatedTime']
                    add_data['dataChangeLastModifiedTime'] = datetime.datetime.now()
                    add_data['tableViewOperType'] = "update"

            add_data["dataChangeLastModifiedBy"] = add_data["dataChangeCreatedBy"]
            add_data['dataChangeLastModifiedTime'] = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000+0800')

            update_appid_url = "{apollo_url}/apps/{appId}/envs/{env}/clusters/{clusterName}/namespaces/{namespaceName}/item".format(
                apollo_url=self.apollo_url,
                appId=appid,
                env=app_env.upper(),
                clusterName=clustersName,
                namespaceName=namespaceName)
            res = self.session.put(update_appid_url, headers=self.headers, data=json.dumps(add_data))
            if res.status_code:
                return True
        except Exception as e:
            return False

    def get_appid_cfg(self, appId, app_env, clusters="default", namespaces="application"):
        url = "{apollo_url}/apps/{appId}/envs/{env}/clusters/{clusterName}/namespaces/{namespaces}/releases/active?page=0&size=1".format(
            apollo_url=self.apollo_url,
            appId=appId,
            env=app_env.upper(),
            clusterName=clusters,
            namespaces=namespaces
            )
        res = self.session.get(url, headers=self.headers)
        if res.status_code == 200:
            return res.json()

    def del_appid_key(self, app, app_env, key, namespaceName="application", clustersName="default"):
        try:
            data = anji_api.findProject_info(app, app_env, clustersName)[0]['items']
            for keys in data:
                if key == keys['item']['key']:
                    apollo_id = keys['item']['id']
                    url = "{apollo_url}/apps/{appId}/envs/{env}/clusters/{clustersName}/namespaces/{namespaceName}/items/{apolloid}".format(
                        apollo_url=self.apollo_url,
                        appId=app,
                        env=app_env.upper(),
                        clustersName=clustersName,
                        namespaceName=namespaceName,
                        apolloid=apollo_id
                        )
                    res = self.session.delete(url, headers=self.headers)
                    if res.status_code == 200:
                        return True
        except Exception as e:
            print(e)
            return False

    def get_rollback_info(self, appId, env, cluster="default", namespaces="application"):
        #host+"/apps/"+app+"/envs/"+env+"/clusters/"+cluster+"/namespaces/"+namespaceName+"/releases/active?page=0&size=2";
        url = "{url}/apps/{app}/envs/{env}/clusters/{cluster}/namespaces/{namespaces}/releases/active?page=0&size=10".format(
            url=self.apollo_url,
            app=appId,
            env=env.upper(),
            cluster=cluster,
            namespaces=namespaces)
        res = self.session.get(url, headers=self.headers)
        if res.status_code == 200:
            return res.json()[0]['id']

    #回滚的还有些问题
    def rollback(self, appId, env, cluster="default", namespaces="application"):
        releaseId = self.get_rollback_info(appId, env, cluster, namespaces)
        print(releaseId)
        url = "{url}/envs/{env}/releases/{releaseId}/rollback".format(
            url=self.apollo_url,
            env=env.upper(),
            releaseId=releaseId)
        res = self.session.put(url, headers=self.headers)
        if res.status_code == 200:
            return True
        elif res.status_code == 400:
            print(res.json())
            return False