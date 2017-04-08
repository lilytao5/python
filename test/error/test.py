# coding=utf-8
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class My(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_add(self):
        self.driver.get("https://www.baidu.com/")
        time.sleep(3)
        try:
            s = self.driver.find_element("xpath", "//*[@id='u1']/a[1]")
            s.click()
            title = self.driver.title
            print title
            self.assertIn(title,"百度新闻搜索")

        except NoSuchElementException as a:
            self.driver.get_screenshot_as_file("d:\\1.png")
            print (u"查找元素‘搜索设置’出现异常:%s"%a)

        except Exception as a:
            print (u"其他异常:%s"%a)
        else:
            assert (title,"百度新闻搜索")


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
