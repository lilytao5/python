#!/usr/bin/env python
# coding=utf-8
from newautosjg.com.Login import Login
from selenium import webdriver
import unittest, time


class Home(unittest.TestCase):
    """登录home页面"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        url = "https://shujuguan.shujuguan.cn"
        self.driver.get(url)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_home(self):
        Login(self.driver).login()
