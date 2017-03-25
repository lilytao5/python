from selenium import webdriver
# coding=utf-8
# dr = webdriver.Firefox()
dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
dr.close()
