#!/usr/bin/env python
# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
import ConfigParser

# 这里写了一个登录的公共方法
class Login(unittest.TestCase):

    def setUp(self):
        #读取相关配置
        # conf_name = "base_url,username,password"
        # conf_list = conf_name.split(",")

        conf = ConfigParser.ConfigParser()
        path = "f:\\python\\autosjg\\config.conf"
        conf.read(path)

        browser = conf.get("test","browser")
        self.browser(browser)

        self.base_url = conf.get("test","base_url")
        self.driver.implicitly_wait(30)

        username = conf.get("test","username")
        password = conf.get("test","password")
        self.login(self.base_url,username, password)

        self.verificationErrors = [] #?
        self.accept_next_alert = True #?

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors) #?

    #这是一段测试代码，运行时需要注释掉
    # def test_01(self):
    #     print "进入测试"
    #     self.driver.find_element(By.ID,"mydata").click()
    #     time.sleep(3)
    #     print "点击数据中心"
    #     title = self.driver.title
    #     print title
    #     self.assertEqual(title, u"数据观 - 所有人都能使用的数据分析工具")
    #     print "登录成功"

    def browser(self, browser):
        if browser == "ie":
            self.driver = webdriver.Ie()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "phantom":
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()

    def login(self, username, password):
        # 这里写了一个登录的函数,url,账号和密码参数化
        self.driver.get(self.base_url + "/")
        time.sleep(3)
        self.driver.maximize_window()

        self.driver.find_element(By.ID,"username").clear()
        self.driver.find_element(By.ID,"username").send_keys(username)
        self.driver.find_element(By.ID,"password").clear()
        self.driver.find_element(By.ID,"password").send_keys(password)
        self.driver.find_element(By.CLASS_NAME,"btn-submit").click()
        time.sleep(15)

if __name__ == "__main__":
    unittest.main()
