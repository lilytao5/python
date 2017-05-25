#!/usr/bin/env python
# coding:utf-8
from shujuguan_test.common.help_selenium import Help
# 单数据编辑页-data_view_edit_page
data_view_edit_url = "https://shujuguan.shujuguan.cn/#data/view/r0554ec27e9444131ae80e7e26831a5c8/edit"


class DataViewEditPage(Help):
    # 定位器，定位页面元素

    def input_username(self, username):
        '''输入账号框'''
        self.send_keys(self.username_loc, username)