#!/usr/bin/env python
# coding:utf-8
from selenium import webdriver
import unittest
from shujuguan_test.page.charts_view_page import ChartsViewPage, charts_view_url
from shujuguan_test.common.help_selenium import browser
import time


class ChartsViewTest(unittest.TestCase):
    u'''登录页面的case'''

    def setUp(self):
        self.driver_charts_view = ChartsViewPage(browser())
        self.driver_charts_view.open(charts_view_url)

    def tearDown(self):
        self.driver_charts_view.quit()

    def test_charts_view_01(self):
        pass

if __name__ == "__main__":
    unittest.main()
