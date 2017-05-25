#!/usr/bin/env python
# coding:utf-8
from shujuguan_test.common.help_selenium import Help
# 预分类-overview_category_test_page
overview_category_test_url = ""


class OverviewCategoryTestPage(Help):
    # 定位器，定位页面元素

    def input_username(self, username):
        '''输入账号框'''
        self.send_keys(self.username_loc, username)