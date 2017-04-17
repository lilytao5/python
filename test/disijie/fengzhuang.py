#!/usr/bin/env python
# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC

class Lily_se():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get(self,url):
        self.driver.get(url)

    def find_element_new(self,locator,timeout=20):
        element = WebDriverWait(self.driver,timeout).until(lambda x: x.find_element(*locator))
        return element

    def send_keys_new(self,locator,text):
        self.find_element_new(locator).send_keys(text)

    def click_new(self,locator):
        self.find_element_new(locator).click()


driver = Lily_se()
# driver.get("https://www.baidu.com")
driver.get("http://www.cnblogs.com/yoyoketang/p/")

# search_loc = ("id","kw")
# driver.send_keys_new(search_loc,"lily")
# button_loc = ("id","su")
# driver.click_new(button_loc)

text_loc = ("id","blog_nav_newpost")
result = EC.text_to_be_present_in_element(text_loc,u"新随笔")(driver)
print result