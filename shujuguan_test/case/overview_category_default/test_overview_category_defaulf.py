#!/usr/bin/env python
# coding:utf-8
from selenium import webdriver
import unittest
from shujuguan_test.page.overview_category_default_page import OverviewCategoryDefaulfPage, overview_category_defaulf_url
from shujuguan_test.common.help_selenium import browser
import time


class OverviewCategoryDefaulfTest(unittest.TestCase):
    u'''登录页面的case'''

    def setUp(self):
        self.driver_overview_category_defaulf = OverviewCategoryDefaulfPage(browser())
        self.driver_overview_category_defaulf.open(overview_category_defaulf_url)

    def tearDown(self):
        self.driver_overview_category_defaulf.quit()

    def test_overview_category_defaulf_01(self):
        pass

if __name__ == "__main__":
    unittest.main()
