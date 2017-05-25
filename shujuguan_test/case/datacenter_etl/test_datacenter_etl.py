#!/usr/bin/env python
# coding:utf-8
from selenium import webdriver
import unittest
from shujuguan_test.page.datacenter_etl_page import DatacenterEtlPage, datacenter_etl_url
from shujuguan_test.common.help_selenium import browser
import time


class DatacenterEtlTest(unittest.TestCase):
    u'''登录页面的case'''

    def setUp(self):
        self.driver_datacenter_etl = DatacenterEtlPage(browser())
        self.driver_datacenter_etl.open(datacenter_etl_url)

    def tearDown(self):
        self.driver_datacenter_etl.quit()

    def test_datacenter_etl_01(self):
        pass

if __name__ == "__main__":
    unittest.main()
