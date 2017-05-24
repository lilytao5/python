# coding:utf-8
from selenium import webdriver
import unittest
from shujuguan_test.page.login_page import LoginPage, login_url
from shujuguan_test.common.help_selenium import browser

class Login_test(unittest.TestCase):
    u'''登录页面的case'''
    def setUp(self):
        self.driver = browser()
        self.driver.open(login_url)

    def test_login_01(self):
        '''登录成功按案例：输入正确账号密码'''
        # 第1步：输入账号
        self.driver.input_username("liyan@gbase.cn")
        # 第2步: 输入密码
        self.driver.input_password("111111")
        # 第3步：点登录按钮
        self.driver.click_submit()
        # 第4步：测试结果,判断是否登录成功
        result = self.driver.is_text_in_element(("id","userguide"),u"使用引导")
        # 第5步：期望结果
        expect_result = True
        # 第6步：断言测试结果与期望结果一致
        self.assertEqual(result, expect_result)

    def test_login_02(self):
        '''登录失败案例：输入错误账号密码'''
        # 第1步：输入账号
        self.driver.input_username("liyan@gbase.cn")
        # 第2步: 输入密码
        self.driver.input_password("123123")
        # 第3步：点登录按钮
        self.driver.click_submit()
        # 第4步：测试结果,判断是否登录成功
        result = self.driver.is_text_in_value(("css",".text-error"),u"用户名或密码错误")
        # 第5步：期望结果
        expect_result = True
        # 第6步：断言测试结果与期望结果一致
        self.assertEqual(result, expect_result)

    def test_login_03(self):
        '''登录页面其它的case'''
        pass


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()