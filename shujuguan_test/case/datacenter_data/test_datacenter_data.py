#!/usr/bin/env python
# coding:utf-8
from selenium import webdriver
import unittest
from shujuguan_test.page.datacenter_data_page import DatacenterDataPage, datacenter_data_url
from shujuguan_test.common.help_selenium import browser
import time


class DatacenterDataTest(unittest.TestCase):
    u'''登录页面的case'''

    def setUp(self):
        self.driver_datacenter_data = DatacenterDataPage(browser())
        self.driver_datacenter_data.open(datacenter_data_url)

    def tearDown(self):
        self.driver_datacenter_data.quit()

    def test_datacenter_data_01(self):
        pass

if __name__ == "__main__":
    unittest.main()
