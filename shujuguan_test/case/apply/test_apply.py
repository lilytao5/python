#!/usr/bin/env python
# coding:utf-8
from selenium import webdriver
import unittest
from shujuguan_test.page.apply_page import ApplyPage, apply_url
from shujuguan_test.common.help_selenium import browser
import time


class ApplyTest(unittest.TestCase):
    u'''登录页面的case'''

    def setUp(self):
        self.driver_apply = ApplyPage(browser())
        self.driver_apply.open(apply_url)

    def tearDown(self):
        self.driver_apply.quit()

    def test_apply_01(self):
        pass

if __name__ == "__main__":
    unittest.main()
