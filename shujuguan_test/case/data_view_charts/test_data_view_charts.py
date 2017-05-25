#!/usr/bin/env python
# coding:utf-8
from selenium import webdriver
import unittest
from shujuguan_test.page.data_view_charts_page import DataViewChartsPage, data_view_charts_url
from shujuguan_test.common.help_selenium import browser
import time


class DataViewChartsTest(unittest.TestCase):
    u'''登录页面的case'''

    def setUp(self):
        self.driver_data_view_charts = DataViewChartsPage(browser())
        self.driver_data_view_charts.open(data_view_charts_url)

    def tearDown(self):
        self.driver_data_view_charts.quit()

    def test_data_view_charts_01(self):
        pass

if __name__ == "__main__":
    unittest.main()
