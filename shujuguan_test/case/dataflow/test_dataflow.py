#!/usr/bin/env python
# coding:utf-8
from selenium import webdriver
import unittest
from shujuguan_test.page.dataflow_page import DataflowPage, dataflow_url
from shujuguan_test.common.help_selenium import browser
import time


class DatacenterEtlTest(unittest.TestCase):
    u'''登录页面的case'''

    def setUp(self):
        self.driver_dataflow = DataflowPage(browser())
        self.driver_dataflow.open(dataflow_url)

    def tearDown(self):
        self.driver_dataflow.quit()

    def test_dataflow_01(self):
        pass

if __name__ == "__main__":
    unittest.main()
