# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from datetime import datetime
from wangdiantong.api.base import BaseAPIEndpoint


class GoodsAPI(BaseAPIEndpoint):

    def goods_push_platfrom(self, shop_no, platform_id, goods_list):
        """
        Docs: https://open.wangdian.cn/qyb/open/apidoc/doc?path=api_goodsspec_push.php
            OpenApi:   /openapi2/api_goodsspec_push.php
            奇门云网官: method=wdt.api.goodsspec.push
            只支持创建自有平台的平台货品，货品明细一次不能超过2000行
            此接口用不到, 一般来说是系统商品已经建好, 下订单匹配商家编码就有平台货品了

        :param str shop_no: varchar(40), required	店铺编号		店铺编号
        :param int platform_id: int(4), required  平台id
        :param array goods_list[]: Array, required  平台货品列表
            :param int status: int(4), required 状态 0删除 1在架 2下架
            :param str goods_id: varchar(40), required 外部系统货品主键,外部系统货品主键
            :param str goods_no: varchar(40), optional 货品商家编码
            :param str goods_name: varchar(256), optional 货品名称
            :param str spec_id: varchar(40), required 规格ID 外部系统货品规格id
            :param str spec_no: varchar(40), required 规格编码 外部系统规格商家编码
            :param str spec_code: varchar(40), optional 平台规格码 外部系统规格编码
            :param str spec_name: varchar(100), optional 规格名称 外部系统规格名称
            :param str pic_url: varchar(255), optional 图片url 外部系统图片url
            :param decimal price: decimal(19, 4), optional 商品价格
            :param decimal stock_num: decimal(19, 4), optional 平台库存
            :param str cid: varchar(40), optional 平台类目
        :return:


        """
        data = {
            "api_goods_info": json.dumps(
                dict(
                    shop_no=shop_no,
                    platform_id=platform_id,
                    goods_list=goods_list
                )
            )

        }

        return self._post("/openapi2/api_goodsspec_push.php", data=data)


    def query(self, start_time, end_time,
                    spec_no=None, goods_no=None,
                    page_no=0, page_size=40, **kwargs):
        """
        查询货品档案

        Docs: https://open.wangdian.cn/qyb/open/apidoc/doc?path=goods_query.php
            OpenApi:   /openapi2/goods_query.php
            奇门云网官: method=wdt.goods.query

        :param datetime start_time: str datetime.strftime("%Y-%m-%d %H:%M:%S"), required 最后更新时间，开始日期
        :param datetime end_time: str datetime.strftime("%Y-%m-%d %H:%M:%S"), required  最后更新时间，结束日期
        :param int page_no: int(10), required 页号,默认0，从0页开始
        :param int page_size: int(10), required 分页大小（最大不超过40条，默认返回40条）

        :param str spec_no: varchar(40) 商家编码（如果不传时间，则spec_no和goods_no必须传一个）
        :param str goods_no: varchar(4) 货品编号
        :param str brand_no: varchar(32) 品牌编号

        ::kwargs
        :param str class_name: varchar(32) 分类名称
        :param str barcode: varchar(64) 条码

        :return:
        """
        if start_time is None:
            assert goods_no or spec_no

        query = dict(
            start_time=start_time.strftime("%Y-%m-%d %H:%M:%S"),
            end_time=end_time.strftime("%Y-%m-%d %H:%M:%S"),
            page_no=page_no,
            spec_no=spec_no,
            goods_no=goods_no,
            page_size=page_size,
        )
        query.update(**kwargs)
        data = dict(list(filter(lambda x: x[1] is not None, query.items())))
        return self._post("/openapi2/goods_query.php", data=data)

    def suites_query(self, start_time, end_time,
                     suite_no, page_no=0, page_size=40, **kwargs):
        """

        :param datetime start_time: str datetime.strftime("%Y-%m-%d %H:%M:%S"), required 最后更新时间，开始日期
        :param datetime end_time: str datetime.strftime("%Y-%m-%d %H:%M:%S"), required  最后更新时间，结束日期
        :param suite_no: str  required 代表组合装商品所有属性的唯一编码，用于系统组合装商品数据的获取;如果按照组合装商家编码查询，可以不传送开始时间和结束时间
        :param int page_no: int(10), required 页号,默认0，从0页开始
        :param int page_size: int(10), required 分页大小（最大不超过40条，默认返回40条）

        ::kwargs
        :param str class_name: varchar(32) 分类名称
        :param str brand_name: varchar(32) 品牌名称
        :return:

            {
                'total_count': 1,
                'message': '',
                'code': 0,
                'suites': [
                    {
                        'unit_name': '',
                        'barcode_count': '0',
                        'weight': '0.8230',
                        'class_name': '无',
                        'wholesale_price': '0.0000',
                        'member_price': '0.0000',
                        'brand_name': '无',
                        'unit_aux_name': '',
                        'flag_name': '',
                        'short_name': 'xxxx',
                        'barcode': '',
                        'market_price': '0.0000',
                        'suite_name': 'xxxx',
                        'retail_price': '0.0000',
                        'remark': '',
                        'created': '0000-00-00 00:00:00',
                        'suite_no': 'xxxxxx',
                        'modified': '2020-04-20 10:36:11',
                        'prop4': '',
                        'specs_list': [{
                            'fixed_price': '355.0000',
                            'ratio': '0.6906',
                            'goods_name': 'xxxxx',
                            'created': '0000-00-00 00:00:00',
                            'barcode': 'xxxxxx',
                            'modified': '2020-04-20 10:36:11',
                            'num': '1.0000',
                            'spec_name': 'xxxxx',
                            'suite_id': '686',
                            'spec_code': '0',
                            'goods_no': 'xxxxx',
                            'spec_no': 'xxxx',
                            'is_fixed_price': '0'
                        }, {
                            'fixed_price': '1590.0000',
                            'ratio': '0.3094',
                            'goods_name': 'xxxxx',
                            'created': '0000-00-00 00:00:00',
                            'barcode': 'xxxxxxx',
                            'modified': '2020-04-20 10:36:11',
                            'num': '1.0000',
                            'spec_name': 'xxxxx',
                            'suite_id': '686',
                            'spec_code': '0',
                            'goods_no': 'xxxxxx',
                            'spec_no': 'xxxxxxx',
                            'is_fixed_price': '0'
                        }],
                        'prop1': '',
                        'prop2': '',
                        'prop3': '',
                        'suite_id': 'xxxx',
                        'large_split': '0'
                    }
                ]
            }
        """

        if suite_no:
            query = dict(
                page_no=page_no,
                suite_no=suite_no,
                page_size=page_size,
            )
        else:
            query = dict(
                start_time=start_time.strftime("%Y-%m-%d %H:%M:%S"),
                end_time=end_time.strftime("%Y-%m-%d %H:%M:%S"),
                page_no=page_no,
                page_size=page_size,
            )
        query.update(**kwargs)
        data = dict(list(filter(lambda x: x[1] is not None, query.items())))
        return self._post("/openapi2/suites_query.php", data=data)


