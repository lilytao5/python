#!/usr/bin/env python
# coding:utf-8
from selenium import webdriver
import unittest
from shujuguan_test.page.data_view_updates_page import DataViewUpdatesPage, data_view_updates_url
from shujuguan_test.common.help_selenium import browser
import time


class DataViewUpdatesTest(unittest.TestCase):
    u'''登录页面的case'''

    def setUp(self):
        self.driver_data_view_updates = DataViewUpdatesPage(browser())
        self.driver_data_view_updates.open(data_view_updates_url)

    def tearDown(self):
        self.driver_data_view_updates.quit()

    def test_data_view_updates_01(self):
        pass

if __name__ == "__main__":
    unittest.main()
