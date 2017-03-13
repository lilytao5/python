# coding:utf-8
from selenium import webdriver
import unittest
import time


# 这里写了一个登录的公共方法
class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def login(self, username, psw):
        # 这里写了一个登录的函数,账号和密码参数化
        url = "https://shujuguan.shujuguan.cn/signin"
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(psw)
        self.driver.find_element_by_class_name("btn-submit").click()
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()
