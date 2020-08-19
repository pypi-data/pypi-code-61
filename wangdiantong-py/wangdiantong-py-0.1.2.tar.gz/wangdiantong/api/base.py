# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class BaseAPIEndpoint(object):

    def __init__(self,
                 client=None):  # type: (wangdiantong.client.base.BaseAPIClient) -> None
        self._client = client

    def _get(self, url, **kwargs):
        if getattr(self, 'API_BASE_URL', None):
            kwargs['api_base_url'] = self.API_BASE_URL
        return self._client.get(url, **kwargs)

    def _post(self, url, **kwargs):
        if getattr(self, 'API_BASE_URL', None):
            kwargs['api_base_url'] = self.API_BASE_URL
        return self._client.post(url, **kwargs)

    @property
    def appkey(self):
        return self._client.signer.appkey

    @property
    def sid(self):
        return self._client.signer.sid

    @property
    def appsecret(self):
        return self._client.signer.appsecret
