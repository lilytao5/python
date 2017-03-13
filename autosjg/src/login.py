# coding:utf-8
from selenium import webdriver
import unittest
import time


# 这里写了一个登录的公共方法
class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.PhantomJS()

        url = "https://shujuguan.shujuguan.cn/signin"
        username = "liyan@gbase.cn"
        password = "111111"
        self.login(url,username, password)

    def tearDown(self):
        self.driver.quit()

    def login(self, url, username, psw):
        # 这里写了一个登录的函数,url,账号和密码参数化
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
