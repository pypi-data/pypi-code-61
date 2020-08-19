# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from wangdiantong.api.goods import GoodsAPI
from wangdiantong.api.logistics import LogisticsAPI
from wangdiantong.api.order import OrderAPI
from wangdiantong.api.stocks import StocksAPI
from wangdiantong.client.base import BaseAPIClient
from wangdiantong import settings


class OpenApiClient(BaseAPIClient):
    """ OpenApi 客户端

    """

    API_BASE_URL = settings.API_BASE_URL

    logistics = LogisticsAPI()

    stocks = StocksAPI()

    orders = OrderAPI()

    goods = GoodsAPI()