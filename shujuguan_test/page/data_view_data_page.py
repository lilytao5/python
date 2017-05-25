#!/usr/bin/env python
# coding:utf-8
from shujuguan_test.common.help_selenium import Help
# 单数据数据页-data_view_data_page
data_view_data_url = "https://shujuguan.shujuguan.cn/#data/view/s65eb6d05e3ee4af5a8cd37cce4d1d9cd/data"


class DataViewDataPage(Help):
    # 定位器，定位页面元素

    def input_username(self, username):
        '''输入账号框'''
        self.send_keys(self.username_loc, username)