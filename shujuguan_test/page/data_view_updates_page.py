#!/usr/bin/env python
# coding:utf-8
from shujuguan_test.common.help_selenium import Help
# 单数据更新页-data_view_updates_page
data_view_updates_url = "https://shujuguan.shujuguan.cn/#data/view/kc9a10708b4fd46eaa47f976e40b1e1b0/updates"


class DataViewUpdatesPage(Help):
    # 定位器，定位页面元素

    def input_username(self, username):
        '''输入账号框'''
        self.send_keys(self.username_loc, username)