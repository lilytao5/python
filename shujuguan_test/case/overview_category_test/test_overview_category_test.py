#!/usr/bin/env python
# coding:utf-8
from selenium import webdriver
import unittest
from shujuguan_test.page.overview_category_test_page import OverviewCategoryTestPage, overview_category_test_url
from shujuguan_test.common.help_selenium import browser
import time


class OverviewCategoryTestTest(unittest.TestCase):
    u'''登录页面的case'''

    def setUp(self):
        self.driver_overview_category_test = OverviewCategoryTestPage(browser())
        self.driver_overview_category_test.open(overview_category_test_url)

    def tearDown(self):
        self.driver_overview_category_test.quit()

    def test_overview_category_test_01(self):
        pass

if __name__ == "__main__":
    unittest.main()
