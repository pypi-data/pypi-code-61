import hashlib
import json
import requests
# import yaml


class NacosClient:
    """
    设置的时候将namespce的名字和namespace id设置成相同
    """
    def __init__(self, server_addr, namespace='public'):
        self._addr = server_addr
        self._ns = namespace
        self._url = f"http://{server_addr}:8848"
        self._ns = namespace
        self.BOOLEAN_DICT = {
            'true': True,
            'false': False
        }

    def conf_get(self, data_id, group):
        url = self._url + '/nacos/v1/cs/configs'
        params = {
            "dataId": data_id,
            "group": group,
            "tenant": self._ns
        }
        res = requests.get(url, params=params)
        if res.ok:
            return res.text

    def _get_md5(self, content):
        h = hashlib.md5()
        h.update(content.encode(encoding='utf-8'))
        return h.hexdigest()

    def conf_listen(self, data_id, group, content=None):
        url = self._url + '/nacos/v1/cs/configs/listener'
        char_1 = chr(1)
        char_2 = chr(2)
        if content is None:
            content_md5 = ''
        else:
            content_md5 = self._get_md5(content)
        para = f"{data_id}{char_2}{group}{char_2}{content_md5}{char_1}"
        params = {"Listening-Configs": para}
        headers = {"Long-Pulling-Timeout": "30000"}
        res = requests.post(url, params=params, headers=headers)
        if res.ok:
            return res.text

    def conf_publish(self, data_id, group, content):
        """
        设置配置，成功返回True，失败返回False
        """
        url = self._url + '/nacos/v1/cs/configs'
        params = {
            "dataId": data_id,
            "group": group,
            "content": content,
            "tenant": self._ns
        }
        res = requests.post(url, params=params)
        if res.ok:
            return self.BOOLEAN_DICT[res.text]

    def conf_delete(self, data_id, group):
        url = self._url + '/nacos/v1/cs/configs'
        params = {
            "dataId": data_id,
            "group": group,
            "tenant": self._ns
        }
        res = requests.delete(url, params=params)
        if res.ok:
            return self.BOOLEAN_DICT[res.text]

    def instance_sign_in(self, ip: str, port: int, service_name: str,
                         weight=None, enabled=None, healthy=None,
                         groupname=None, metadata=None):
        """
        注册实例: 注册一个实例到服务
        ip: 服务实例ip
        port: 服务实例port
        service_name: 服务名
        weight: 权重(浮点数)
        enabled: 是否上线(布尔)
        healthy: 是否健康(布尔)
        groupname: 分组名
        """
        url = self._url + '/nacos/v1/ns/instance'
        params = {
            "ip": ip,
            "port": port,
            "serviceName": service_name,
            "namespaceId": self._ns
        }
        if weight is not None:
            params["weight"] = weight
        if enabled is not None:
            params["enabled"] = enabled
        if healthy is not None:
            params["healthy"] = healthy
        if groupname is not None:
            params["groupname"] = groupname
        if metadata is not None:
            params["metadata"] = groupname
        res = requests.post(url, params=params)
        if res.ok:
            return res.text

    def instance_log_out(self, ip: str, port: int, service_name: str,
                         groupname=None):
        """
        注销实例: 删除服务下的一个实例
        """
        url = self._url + '/nacos/v1/ns/instance'
        params = {
            "ip": ip,
            "port": port,
            "serviceName": service_name,
            "namespaceId": self._ns
        }
        if groupname is not None:
            params["groupname"] = groupname
        res = requests.delete(url, params=params)
        if res.ok:
            return res.text

    def instance_list(self, service_name: str):
        """
        查询实例列表
        """
        url = self._url + '/nacos/v1/ns/instance/list'
        params = {
            "serviceName": service_name,
            "namespaceId": self._ns
        }
        res = requests.get(url, params=params)
        if res.ok:
            return res.json()

    def instance_get(self, ip: str, port: int, service_name: str):
        """
        查询实例详情
        """
        url = self._url + '/nacos/v1/ns/instance'
        params = {
            "serviceName": service_name,
            "ip": ip,
            "port": port,
            "namespaceId": self._ns
        }
        res = requests.get(url, params=params)
        if res.ok:
            return res.json()

    def instance_beat(self, service_name, beat):
        """
        发送实例心跳
        beat:实例内容的json字符串
        """
        url = self._url + '/nacos/v1/ns/instance/beat'
        params = {
            "serviceName": service_name,
            "beat": json.dumps(beat),
            "namespaceId": self._ns
        }
        res = requests.put(url, params=params)
        if res.ok:
            return res.text

    def service_add(self, service_name, protect_threshold=0.4):
        """
        创建服务
        protect_threshold: 阈值0-1
        """
        url = self._url + '/nacos/v1/ns/service'
        params = {
            "serviceName": service_name,
            "namespaceId": self._ns,
            "protectThreshold": protect_threshold
        }
        res = requests.post(url, params=params)
        if res.ok:
            return res.text

    def service_delete(self, service_name):
        """
        删除服务
        """
        url = self._url + '/nacos/v1/ns/service'
        params = {
            "serviceName": service_name,
            "namespaceId": self._ns
        }
        res = requests.delete(url, params=params)
        if res.ok:
            return res.text

    def service_get(self, service_name):
        """
        查询服务，若没查到返回None(实际上是500)
        """
        url = self._url + '/nacos/v1/ns/service'
        params = {
            "serviceName": service_name,
            "namespaceId": self._ns
        }
        res = requests.get(url, params=params)
        if res.ok:
            return res.json()

    def service_list(self, page_no, page_size):
        """
        服务列表
        """
        url = self._url + '/nacos/v1/ns/service/list'
        params = {
            "pageNo": page_no,
            "pageSize": page_size,
            "namespaceId": self._ns
        }
        res = requests.get(url, params=params)
        print(res.text)
        if res.ok:
            return res.json()


if __name__ == '__main__':
    data_id = 'nacos.cfg.dataId'
    group = 'test'
    # client = NacosClient("127.0.0.1", "zhr_test")
    client = NacosClient("127.0.0.1", "zhr_osp")
    res = client.conf_get('API', 'MCMDB')
    print(res)
    # print(yaml.load(res, Loader=yaml.FullLoader))
    # client.conf_listen(data_id, group, 'HelloWorld')
    client.conf_publish('nacos.cfg.dataId', 'test', 'helloabc')
    client.conf_delete('nacos.cfg.dataId', 'test')
    client.instance_sign_in("8.8.8.8", 80, "cmdb", enabled=True)
    client.instance_sign_in("8.8.8.9", 80, "cmdb", enabled=True)
    # client.instance_log_out("8.8.8.8", 80, "cmdb")
    res = client.instance_list("cmdb")
    res = client.instance_get('8.8.8.8', 80, "cmdb")
    # while True:
    #     client.instance_beat('cmdb', res)
    #     time.sleep(10)
    res = client.service_add("cmdb2")
    print(res)
    res = client.service_list(0, 10)
    print(res)
    res = client.service_get("cmdb2")
    print(res)
    res = client.service_delete("cmdb2")
    print(res)
