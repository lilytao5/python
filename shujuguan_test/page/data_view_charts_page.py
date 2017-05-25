#!/usr/bin/env python
# coding:utf-8
from shujuguan_test.common.help_selenium import Help
# 单数据图表页-data_view_charts_page
data_view_charts_url = "https://shujuguan.shujuguan.cn/#data/view/u6a4885a0f0894054b7c6ee931479ac13/charts"


class DataViewChartsPage(Help):
    # 定位器，定位页面元素

    def input_username(self, username):
        '''输入账号框'''
        self.send_keys(self.username_loc, username)