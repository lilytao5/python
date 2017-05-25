# coding:utf-8
from selenium import webdriver
import unittest
from sjg.page.datacenter_data_page import DatacenterDataPage, data_url
from shujuguan_test.common.help_selenium import browser


class DatacenterDataTest(unittest.TestCase):
    u'''登录页面的case'''
    def setUp(self):
        self.driver_datacenterdata = DatacenterDataPage(browser())
        self.driver_datacenterdata.open(data_url)

    def tearDown(self):
            self.driver_datacenterdata.quit()

    def test_datacenterdata_01(self):
        '''登录成功按案例：输入正确账号密码'''
        # 第1步：输入账号
        self.driver.input_username("liyan@gbase.cn")
        # 第2步: 输入密码
        self.driver.input_password("111111")
        # 第3步：点登录按钮
        self.driver.click_submit()
        # 第4步：测试结果,判断是否登录成功
        result = self.driver.text_in_element(("id", "userguide"), "使用引导")
        # 第5步：期望结果
        expect_result = True
        # 第6步：断言测试结果与期望结果一致
        self.assertEqual(result, expect_result)

    if __name__ == "__main__":
        unittest.main()