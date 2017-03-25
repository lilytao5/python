#!/usr/bin/env python
# coding:utf-8
from selenium import webdriver
import unittest
import time
import ConfigParser
import os

# 这里写了一个登录的公共方法
class Login(unittest.TestCase):

    def setUp(self):
        #读取相关配置
        # conf_name = "base_url,username,password"
        # conf_list = conf_name.split(",")

        conf = ConfigParser.ConfigParser()
        path = "f:\\python\\autosjg\\config.conf"
        conf.read(path)

        self.Browser("chrome") #ie/firefox/chrome/phantom/htmlunit是纯java写的，python不能直接启动它。
        self.base_url = conf.get("test","base_url")
        username = conf.get("test","username")
        password = conf.get("test","password")

        self.driver.implicitly_wait(30)
        self.login(self.base_url,username, password)
        self.verificationErrors = [] #?
        self.accept_next_alert = True #?

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors) #?

    # def test_01(self):
    #     title = self.driver.title
    #     print title
    #     self.assertEqual(title, u"数据观 - 所有人都能使用的数据分析工具")
    #     print "登录成功"

    def login(self, base_url, username, password):
        # 这里写了一个登录的函数,url,账号和密码参数化
        self.driver.get(self.base_url + "/")
        time.sleep(3)
        self.driver.maximize_window()

        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_class_name("btn-submit").click()
        time.sleep(10)

    def Browser(self, br):
        if br == "ie":
            self.driver = webdriver.Ie()
        elif br == "firefox":
            self.driver = webdriver.Firefox()
        elif br == "chrome":
            self.driver = webdriver.Chrome()
        elif br == "phantom":
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()

if __name__ == "__main__":
    unittest.main()
