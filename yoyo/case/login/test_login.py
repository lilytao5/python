# coding:utf-8
from selenium import webdriver
import unittest
import ddt
from blog.blog_login_page import LoginPage, login_url
from read_exl import read_excel

da = read_excel("testdata.xlsx", u'login')
test_li = da.read_dict()
print test_li

@ddt.ddt
class Login_test(unittest.TestCase):
    u'''登录页面的case'''
    def setUp(self):
        self.driver = LoginPage()
        self.driver.open(login_url)

    def login_case(self, username, psw, expect):
        '''登录用例的方法'''
        # 第1步：输入账号
        self.driver.input_username(username)
        # 第2步: 输入密码
        self.driver.input_password(psw)
        # 第3步：点登录按钮
        self.driver.click_submit()
        # 第4步：测试结果,判断是否登录成功
        result = self.driver.text_in_element(("id","lnk_current_user"),"上海-悠悠")
        # 第5步：期望结果
        if expect == "False": expect_result = False
        else: expect_result = True
        # 第6步：断言测试结果与期望结果一致
        self.assertEqual(result, expect_result)

    @ddt.data(*test_li)
    def test_login_01(self, data):
        '''登录成功按案例：输入正确账号密码'''
        print data["username"], data["psw"],data["expect"]
        self.login_case(data["username"], data["psw"],data["expect"])

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
