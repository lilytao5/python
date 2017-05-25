#!/usr/bin/env python
# coding:utf-8
from selenium import webdriver
import unittest
from shujuguan_test.page.data_view_manage_page import DataViewManagePage, data_view_manage_url
from shujuguan_test.common.help_selenium import browser
import time


class DataViewManageTest(unittest.TestCase):
    u'''登录页面的case'''

    def setUp(self):
        self.driver_data_view_manage = DataViewManagePage(browser())
        self.driver_data_view_manage.open(data_view_manage_url)

    def tearDown(self):
        self.driver_data_view_manage.quit()

    def test_data_view_manage_01(self):
        pass

if __name__ == "__main__":
    unittest.main()
