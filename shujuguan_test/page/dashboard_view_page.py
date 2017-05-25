#!/usr/bin/env python
# coding:utf-8
from shujuguan_test.common.help_selenium import Help
# 图集设计器-dashboard_view_page
dashboard_view_url = ""


class DashboardViewPage(Help):
    # 定位器，定位页面元素

    def input_username(self, username):
        '''输入账号框'''
        self.send_keys(self.username_loc, username)