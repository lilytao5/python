#!/usr/bin/env python
# coding:utf-8
from shujuguan_test.common.help_selenium import Help
# 数据中心etl页-datacenter_etl_page
datacenter_etl_url = "https://shujuguan.shujuguan.cn/#datacenter/etl"


class DatacenterEtlPage(Help):
    # 定位器，定位页面元素

    def input_username(self, username):
        '''输入账号框'''
        self.send_keys(self.username_loc, username)