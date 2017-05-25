#!/usr/bin/env python
# coding:utf-8
from shujuguan_test.common.help_selenium import Help
# 注册-apply_page
apply_url = "https://app.shujuguan.cn/apply"


class ApplyPage(Help):
    # 定位器，定位页面元素
    username_loc = ("id", "username")  # 输入账号

    def input_username(self, username):
        '''输入账号框'''
        self.send_keys(self.username_loc, username)
