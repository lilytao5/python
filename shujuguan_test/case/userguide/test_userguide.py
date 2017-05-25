#!/usr/bin/env python
# coding:utf-8
from selenium import webdriver
import unittest
from shujuguan_test.page.userguide_page import UserguidePage, userguide_url
from shujuguan_test.common.help_selenium import browser
import time


class UserguideTest(unittest.TestCase):
    u'''登录页面的case'''

    def setUp(self):
        self.driver_userguide = UserguidePage(browser())
        self.driver_userguide.open(userguide_url)

    def tearDown(self):
        self.driver_userguide.quit()

    def test_userguide_01(self):
        pass

if __name__ == "__main__":
    unittest.main()
