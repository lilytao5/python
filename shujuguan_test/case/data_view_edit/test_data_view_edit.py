#!/usr/bin/env python
# coding:utf-8
from selenium import webdriver
import unittest
from shujuguan_test.page.data_view_edit_page import DataViewEditPage, data_view_edit_url
from shujuguan_test.common.help_selenium import browser
import time


class DataViewEditTest(unittest.TestCase):
    u'''登录页面的case'''

    def setUp(self):
        self.driver_data_view_edit = DataViewEditPage(browser())
        self.driver_data_view_edit.open(data_view_edit_url)

    def tearDown(self):
        self.driver_data_view_edit.quit()

    def test_data_view_edit_01(self):
        pass

if __name__ == "__main__":
    unittest.main()
