# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import datetime
import json

from wangdiantong.api.base import BaseAPIEndpoint


class OrderStatus(object):
    """
    0    所有订单
    5    已取消
    10   待付款
    15   等未付
    16   延时审核
    19   预订单前处理
    20   前处理
    21   委外前处理
    22   抢单前处理
    25   预订单
    27   待抢单
    30   待客审
    35   待财审
    40   待递交仓库
    45   递交仓库中
    50   已递交仓库
    53   未确认
    55   已审核
    95   已发货
    100  已签收
    105  部分打款
    110  已完成
    """


class OrderAPI(BaseAPIEndpoint):
    """
    Order

    Docs:
        https://open.wangdian.cn/qyb/open/apidoc/doc?path=trade_push.php
    """

    """
    接口名称	接口功能描述	接口简称	ERP功能界面的操作路径
    stockin_refund_push.php	创建ERP销售退货入库单	创建销售退货入库单	库存-》入库管理-》退货入库单管理界面
    stockin_order_query_refund.php	查询ERP中退换入库单信息	查询退换入库单	库存-》入库管理-》退货入库单管理界面
    trade_push.php	订单推送到ERP系统中；更新ERP原始订单信息	创建原始订单	订单-》原始订单界面）
    trade_query.php	查询ERP中系统订单	查询系统订单	订单-》订单管理界面
    logistics_sync_query.php	将erp中已发货的处于等待同步的订单抓取到进行物流同步	查询物流同步	订单-》物流同步界面
    logistics_sync_ack.php	将同步的结果回传到erp系统，系统会更新物流同步状态	物流同步状态回写	
    api_goods_stock_change_query.php	查询出ERP中库存发生了变化，此时平台和ERP的库存不一致的货品库存，然后去修改平台上的货品库存	查询库存同步	设置-》策略设置-》库存同步
    api_goods_stock_change_ack.php	将同步结果回传到ERP系统，这样下次再查询库存的时候，就不会再把这次已经库存同步了的货品查出来。	平台货品库存同步状态回写	
    sales_refund_push.php	已经发货的订单，如果退款或退货，需要调用该接口 创建原始退款单	创建原始退款单	订单-》原始退款单
    refund_query.php	查询ERP中退货或者换货的订单信息	查询退换管理	订单-》退换管理界面
    """

    def trade_query(self,
                    start_time, end_time, status=0,
                    page_no=0, page_size=10,
                    **kwargs): # type: (datetime.datetime, datetime.datetime, int, int, int)->dict
        """
        查询ERP中系统订单
              openapi:  /openapi2/trade_query.php
            奇门云网关:  method=wdt.trade.query

        Docs: https://open.wangdian.cn/qyb/open/apidoc/doc?path=trade_query.php

        :param datetime start_time: str datetime.strftime("%Y-%m-%d %H:%M:%S"), required 最后更新时间，开始日期
        :param datetime end_time: str datetime.strftime("%Y-%m-%d %H:%M:%S"), required  最后更新时间，结束日期
        :param int status: int(4), required 订单状态
        :param int page_no: int(10), required 页号,默认0，从0页开始
        :param int page_size: int(10), required 分页大小（最大不超过40条，默认返回40条）

        ::kwargs
        :param int img_url: int[0,1] 是否返回图片
        :param str trade_no: varchar(40) 订单编号
        :param str shop_no: varchar(40)	店铺编号		店铺编号
        :param str warehouse_no: varchar(40) 仓库编号
        :param int goodstax: int[0,1] 使用税率, 0 使用订单中的税率 1使用单品中的税率(默认0)
        :param int has_logistics_no: int[0,1] 物流单号限制, 0 没有任何限制(默认值) 1 物流单号不为空才返回 2 只返回物流单号为空的
        :param int src: int[0,1] 是否返回交易流水号, 1 返回订单的交易流水单号 0 不返回（默认值）
        :param str logistics_no: varchar(40) 物流单号

        :return:
        """
        query = dict(
            start_time=start_time.strftime("%Y-%m-%d %H:%M:%S"),
            end_time=end_time.strftime("%Y-%m-%d %H:%M:%S"),
            page_no=page_no,
            status=status,
            page_size=page_size,
        )
        query.update(**kwargs)
        data = dict(list(filter(lambda x: x[1] is not None, query.items())))
        return self._post("/openapi2/trade_query.php", data=data)

    def trade_push(self,
                   shop_no, trade_list, switch=1):
        """
        推送订单

        Docs: https://open.wangdian.cn/qyb/open/apidoc/doc?path=trade_push.php

        :param shop_no:
        :param trade_list:
        :param switch:
        :return:
        """
        data = {
            "shop_no": shop_no,
            "trade_list": json.dumps(trade_list),
            "switch": switch
        }
        return self._post("/openapi2/trade_push.php", data=data)
