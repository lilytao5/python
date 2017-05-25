#!/usr/bin/env python
# coding:utf-8
from selenium import webdriver
import unittest
from shujuguan_test.page.reset_page import ResetPage, reset_url
from shujuguan_test.common.help_selenium import browser
import time


class ResetTest(unittest.TestCase):
    u'''登录页面的case'''

    def setUp(self):
        self.driver_reset = ResetPage(browser())
        self.driver_reset.open(reset_url)

    def tearDown(self):
        self.driver_reset.quit()

    def test_reset_01(self):
        pass

if __name__ == "__main__":
    unittest.main()
