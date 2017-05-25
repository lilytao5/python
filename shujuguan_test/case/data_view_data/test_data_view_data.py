#!/usr/bin/env python
# coding:utf-8
from selenium import webdriver
import unittest
from shujuguan_test.page.data_view_data_page import DataViewDataPage, data_view_data_url
from shujuguan_test.common.help_selenium import browser
import time


class DataViewDataTest(unittest.TestCase):
    u'''登录页面的case'''

    def setUp(self):
        self.driver_data_view_data = DataViewDataPage(browser())
        self.driver_data_view_data.open(data_view_data_url)

    def tearDown(self):
        self.driver_data_view_data.quit()

    def test_data_view_data_01(self):
        pass

if __name__ == "__main__":
    unittest.main()
