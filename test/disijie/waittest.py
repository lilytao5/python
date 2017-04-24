#!/usr/bin/env python
# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
#
# element = WebDriverWait(driver,10).until(lambda x: x.find_element("id","kw"))
# element.send_keys("lily")
#
# button = WebDriverWait(driver,10).until(lambda x: x.find_element("id","su"))
# button.click()

driver.get("http://www.cnblogs.com/yoyoketang/p/")
text_loc = ("id","blog_nav_newpost")
result = EC.text_to_be_present_in_element(text_loc,u"新随笔")
# print result
r = WebDriverWait(driver,10).until(result)
print r
