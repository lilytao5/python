# coding:utf-8
from selenium import webdriver
import test01
import time

class Bolg(test01.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def login(self, username, psw):
        # 这里写了一个登录的函数,账号和密码参数化
        url = "https://passport.cnblogs.0com/user/signin"
        self.driver.get(url)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("input1").send_keys(username)
        self.driver.find_element_by_id("input2").send_keys(psw)
        self.driver.find_element_by_id("signin").click()
        time.sleep(3)

    def test_01(self):
        # 登录案例参考:账号，密码自己设置
        self.login(u"上海-悠悠", u"xxxx")  # 调用登录函数
        # 获取登录后的账号名称
        text = self.driver.find_element_by_id("lnk_current_user").text
        print text
        # 断言实际结果与期望结果一致
        self.assertEqual(text, u"上海-悠悠")

    def test_02(self):
        # 登录案例参考:账号，密码自己设置
        self.login(u"上海-悠悠", u"oooo") # 调用登录函数
        # 获取登录后的账号名称
        text = self.driver.find_element_by_id("lnk_current_user").text
        self.driver.get_screenshot_as_file()
        print text
        # 断言实际结果与期望结果一致
        self.assertEqual(text, u"上海-悠悠")

if __name__ == "__main__":
    test01.main()



