# coding=utf-8
from selenium import webdriver
import time

url = "https://shujuguan.shujuguan.cn"
# dr = webdriver.PhantomJS()
# dr = webdriver.Chrome()
dr = webdriver.Firefox()

dr.get(url)
time.sleep(10)

dr.find_element_by_name("username").send_keys("liyan@gbase.cn")
dr.find_element_by_name("password").send_keys("111111")
dr.find_element_by_class_name("first_button").click()
time.sleep(10)

dr.find_element_by_id("mydata").click()

# data = driver.title
print "111111"
dr.close()