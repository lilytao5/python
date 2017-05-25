#!/usr/bin/env python
# coding:utf-8
from selenium import webdriver
import unittest
from shujuguan_test.page.dashboard_view_page import DashboardViewPage, dashboard_view_url
from shujuguan_test.common.help_selenium import browser
import time


class DashboardViewTest(unittest.TestCase):
    u'''登录页面的case'''

    def setUp(self):
        self.driver_dashboard_view = DashboardViewPage(browser())
        self.driver_dashboard_view.open(dashboard_view_url)

    def tearDown(self):
        self.driver_dashboard_view.quit()

    def test_dashboard_view_01(self):
        pass

if __name__ == "__main__":
    unittest.main()
