# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import datetime
import json

from wangdiantong.api.base import BaseAPIEndpoint


class StocksAPI(BaseAPIEndpoint):
    """ Goods Stocks

    Docs:
        https://open.wangdian.cn/qyb/open/apidoc/doc
    """

    def change_query(self, shop_no, limit):
        """
        查询库存同步

        Docs:
            https://open.wangdian.cn/qyb/open/apidoc/doc?path=api_goods_stock_change_query.php

        :param str shop_no: varchar(20) required 店铺编号
        :param int limit: int(4) 最多返回条数
        :return:
        """
        data = dict(
            shop_no=shop_no,
            limit=limit
        )
        import json
        data_json = json.dumps(data)
        assert data_json
        return self._post("/openapi2/api_goods_stock_change_query.php", data=data)

    def sync_ack(self,  stock_sync_list):
        """
        平台货品库存同步状态回写

        Docs:
            https://open.wangdian.cn/qyb/open/apidoc/doc?path=api_goods_stock_change_ack.php

        :param list stock_sync_list: [dict(rec_id=1, sync_stoc=100, stock_change_count=5634245)]
        :return:
        """
        data = dict(
            stock_sync_list=json.dumps(stock_sync_list)
        )
        return self._post("/openapi2/api_goods_stock_change_ack.php", data=data)

    def item_for_ack(self, rec_id, sync_stock, stock_change_count):
        """
        sync_ack 请求参数 stock_sync_list的元素

        :param int rec_id: int(11) required Erp内平台货品表主键id
        :param int sync_stock: int(11) required 货品库存
        :param int stock_change_count: int(11) required 库存变化时自增
        :return:
        """
        return dict(
            rec_id=rec_id,
            sync_stock=sync_stock,
            stock_change_count=stock_change_count
        )

    def query(self, start_time, end_time,
              warehouse_no=None, spec_no=None,
              page_no=0, page_size=40): # type: (datetime.datetime, datetime.datetime, int, int, str, str)->dict
        """
        库存查询-分页查询
             openapi:  /openapi2/stock_query.php
            奇门云网关: wdt.stock.query

        Docs:
            https://open.wangdian.cn/qyb/open/apidoc/doc?path=stock_query.php

        :param datetime start_time: str datetime.strftime("%Y-%m-%d %H:%M:%S"), required
        :param datetime end_time: str datetime.strftime("%Y-%m-%d %H:%M:%S"), required
        :param str warehouse_no: str
        :param str spec_no: str
        :param int page_no: int, required
        :param int page_size: int, required
        :return: dict
        """
        data = dict(list(filter(lambda x: x[1] is not None, dict(
            warehouse_no=warehouse_no,
            spec_no=spec_no,
            start_time=start_time.strftime("%Y-%m-%d %H:%M:%S"),
            end_time=end_time.strftime("%Y-%m-%d %H:%M:%S"),
            page_no=page_no,
            page_size=page_size,
        ).items())))
        return self._post("/openapi2/stock_query.php", data=data)
