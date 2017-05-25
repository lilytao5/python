#!/usr/bin/env python
# coding:utf-8
from shujuguan_test.common.help_selenium import Help
# 图表设计器-charts_view_page
charts_view_url = "https://shujuguan.shujuguan.cn/#charts/view/s8f031b07f478435b85a49fae365e41d2"


class ChartsViewPage(Help):
    # 定位器，定位页面元素

    def input_username(self, username):
        '''输入账号框'''
        self.send_keys(self.username_loc, username)