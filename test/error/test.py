# coding=utf-8
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class My(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.0com/")
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

    def test_01_exception(self):
        self.driver.find_element("id", "//*[@id='u1']/a[1]").click()
        title = self.driver.title

        try:
            self.assertIn(u"百度新闻搜索", title)

        except NoSuchElementException as msg:
            self.driver.get_screenshot_as_file("d:\\1.png")
            print (u"查找元素‘新闻’出现异常:%s"%msg)

        except Exception as msg:
            self.driver.get_screenshot_as_file("d:\\1.png")
            print (u"其他异常:%s"%msg)

        else:
            print u"操作成功"


if __name__ == '__main__':
    unittest.main()
