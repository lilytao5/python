# coding:utf-8
from selenium import webdriver
import time
dr = webdriver.Firefox()
dr.implicitly_wait(30)
dr.get("https://www.baidu.0com")
time.sleep(3)

# dr.find_element_by_xpath("//*[@id='kw']").sen
# d_keys("aaa")

dr.find_element_by_xpath(".//a[contains(text(),'搜索设置')]").click()
dr.