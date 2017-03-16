#! /usr/bin/env python
#coding=utf-8
import xlrd ,codecs ,sys ,os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re


class Find_object(unittest.TestCase):
    def setUp(self):
#        self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://shujuguan.shujuguan.cn/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.path = sys.path[0] + '/result/'
        self.dict_url = {}

    def test_search(self):

        self.driver.get(self.base_url)
        self.driver.find_element_by_name('username').send_keys('liyan@gbase.cn')
        self.driver.find_element_by_name('password').send_keys('111111')
        self.driver.find_element_by_class_name('first_button').click()
        time.sleep(10)
        self.driver.find_element_by_id('mydata').click()
        time.sleep(30)


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()