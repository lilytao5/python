# coding=utf-8
import time
from selenium import webdriver
import unittest
class Testsjg(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://shujuguan.shujuguan.cn")
        time.sleep(3)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_01login(self):
        self.driver.find_element_by_name("username").send_keys("liyan@gbase.cn")
        self.driver.find_element_by_id("password").send_keys("111111")
        self.driver.find_element_by_class_name("btn-submit").click()
        title = self.driver.title
        print title
        self.assertEqual(title, u"登录-shujuguan")
        print "登录成功"