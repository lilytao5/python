# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os, sys, time
reload(sys)
sys.setdefaultencoding('utf-8')

class Help(object):
    """
    基于原生的selenium框架做了二次封装.
    """
    def __init__(self, browser='chrome'):
        """
        启动浏览器参数化，默认启动firefox.
        """
        try:
            if browser == "firefox" or browser == "ff":
                self.driver = webdriver.Firefox()
            elif browser == "chrome" or browser == "gc":
                self.driver = webdriver.Chrome()
            elif browser == "ie":
                self.driver = webdriver.Ie()
            elif browser == "phantomjs" or browser == "pj":
                self.driver = webdriver.PhantomJS()
        except Exception:
            raise NameError("Not found this browser,You can use 'firefox', 'chrome', 'ie' or 'phantomjs'.")

    def open(self, url, t='', timeout=30):
        '''
        使用get打开url后，最大化窗口，判断title符合预期
        '''
        self.driver.get(url)
        self.driver.maximize_window()
        try:
            WebDriverWait(self.driver, timeout, 5).until(EC.title_contains(t))
        except TimeoutException:
            print("open %s title error" % url)
        except Exception as msg:
            print("Error:%s" % msg)

    def find_element(self, locator, timeout=30):
        '''
        定位元素，参数locator是元祖类型
        Usage:
        locator = ("id","xxx")
        driver.find_element(*locator)
        '''
        element = WebDriverWait(self.driver, timeout, 1).until(lambda x: x.find_element(*locator))
        return element

    def click(self, locator):
        '''
        点击操作
        Usage:
        locator = ("id","xxx")
        driver.click(*locator)
        '''
        try:
            element = self.find_element(locator)
        except TimeoutException:
            print("element not found:%s" % locator)
        else:
            element.click()

    def send_keys(self, locator, text):
        '''
        发送文本
        Usage:
        locator = ("id","xxx")
        driver.send_keys(*locator)
        '''
        try:
            element = self.find_element(locator)
        except TimeoutException:
            print("element not found:%s" % locator)
        else:
            element.clear()
            element.send_keys(text)

    def text_in_element(self, locator, text, timeout=10):
        '''判断文本在元素里'''
        try:
            WebDriverWait(self.driver, timeout, 1).until(EC.text_to_be_present_in_element(locator, text))
            return True
        except TimeoutException:
            return False

    def move_to_element(self, locator):
        '''
        鼠标悬停操作
        Usage:
        locator = ("id","xxx")
        driver.move_to_element("id","xxx")
        '''
        try:
            element = self.find_element(locator)
        except TimeoutException:
            print("element not found:%s" % locator)
        else:
            ActionChains(self.driver).move_to_element(element).perform()

    def back(self):
        """
        Back to old window.

        Usage:
        driver.back()
        """
        self.driver.back()

    def forward(self):
        """
        Forward to old window.

        Usage:
        driver.forward()
        """
        self.driver.forward()

    def close(self):
        """
        Close the windows.

        Usage:
        driver.close()
        """
        self.driver.close()

    def quit(self):
        """
        Quit the driver and close all the windows.

        Usage:
        driver.quit()
        """
        self.driver.quit()


if __name__ == '__main__':
    driver = Yoyo("ff")  # 调用浏览器，支持 'firefox', 'chrome', 'ie' or 'phantomjs'
    driver.open("http://www.baidu.com", "百度")
    # locator = ("id", "kw")
    # driver.find_element(locator).send_keys("kkk")
    print driver.text_in_element(("name", "tj_trmap"), "地图")
