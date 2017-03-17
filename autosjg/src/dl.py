# coding:utf-8
from selenium import webdriver
import unittest
import time
import ConfigParser



# 这里写了一个登录的公共方法
class Login(unittest.TestCase):

    def setUp(self):
        #读取相关配置
        conf_name = "base_url,username,password"
        conf_list = conf_name.split(",")

        conf = ConfigParser.ConfigParser()
        path = "f:\\python\\autosjg\\config.conf"
        conf.read(path)

        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.PhantomJS()

        # self.base_url = "https://shujuguan.shujuguan.cn/signin"
        # username = "liyan@gbase.cn"
        # password = "111111"

        self.base_url = conf.get("test","base_url")
        username = conf.get("test","username")
        password = conf.get("test","password")
        # self.base_url = "http://ls.chart2.com/signin"
        # username = "lily@lily.com"
        # password = "111111"

        self.login(self.base_url,username, password)

        self.verificationErrors = [] #?
        self.accept_next_alert = True #?

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors) #?

    def test_01(self):
        text = self.driver.find_element_by_class_name("userguide").text
        print text
        self.assertEqual(text, u"使用引导")
        print "登录成功"

    def login(self, base_url, username, password):
        # 这里写了一个登录的函数,url,账号和密码参数化
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_class_name("btn-submit").click()
        time.sleep(10)

if __name__ == "__main__":
    unittest.main()
