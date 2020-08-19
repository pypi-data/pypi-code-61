# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import copy
import inspect
import logging
import time

import requests

from wangdiantong.settings import API_BASE_URL
from wangdiantong.api.base import BaseAPIEndpoint
from wangdiantong.utils import calculate_signature

logger = logging.getLogger(__name__)


def _is_api_endpoint(obj):
    return isinstance(obj, BaseAPIEndpoint)


class Code(object):
    SUCCESS = 0


class Signer(object):

    def __init__(self, sid, appkey, appsecret):
        self.sid = sid
        self.appkey = appkey
        self.appsecret = appsecret

    def sign_data(self, request, timestamp=None):
        timestamp = timestamp or int(time.time())
        params = copy.deepcopy(request)
        params.update(
            sid=self.sid,
            appkey=self.appkey,
            timestamp=timestamp,
        )
        return calculate_signature(params, appsecret=self.appsecret), params

    def sign_request(self, request=None, timestamp=None):
        request = request or dict()
        signed_str, request = self.sign_data(request, timestamp)
        request.update(
            sign=signed_str
        )
        return request


class BaseAPIClient(object):
    logger = logger

    API_BASE_URL = API_BASE_URL

    CODE = Code

    NOW = None

    SIGNER_CLASS = Signer

    def __new__(cls, *args, **kwargs):
        self = super(BaseAPIClient, cls).__new__(cls)
        api_endpoints = inspect.getmembers(self, _is_api_endpoint)
        for name, _api in api_endpoints:
            api_cls = type(_api)
            _api = api_cls(self)
            setattr(self, name, _api)
        return self

    def __init__(self, sid, appkey, appsecret):
        self.signer = self.SIGNER_CLASS(sid=sid,
                                        appkey=appkey,
                                        appsecret=appsecret)

    def _sign_request(self, data):
        return self.signer.sign_request(request=data, timestamp=self.NOW)

    def _request(self, method, url_or_endpoint, data=None, headers=None,
                 **kwargs):
        if not url_or_endpoint.startswith(('http://', 'https://')):
            api_base_url = kwargs.pop('api_base_url', self.API_BASE_URL)
            uri = '{base}{endpoint}'.format(
                base=api_base_url,
                endpoint=url_or_endpoint
            )
        else:
            uri = url_or_endpoint

        headers = headers or {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        reqdata = self._sign_request(data=data)
        method = getattr(requests, method.lower())
        resp = method(uri, data=reqdata, headers=headers)

        try:
            data = resp.json()
        except:
            logger.debug('result parsing error', exc_info=True)
            raise
        data['code'] = int(data['code'])
        return data

    def get(self, url, **kwargs):
        return self._request(
            method='get',
            url_or_endpoint=url,
            **kwargs
        )

    def post(self, url, **kwargs):
        return self._request(
            method='post',
            url_or_endpoint=url,
            **kwargs
        )
