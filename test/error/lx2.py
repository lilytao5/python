#!/usr/bin/env python
# coding=utf-8
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# # 没有网络了
# driver.find_element("id","kw1").click()


try:
    print "开始4"
    f = open("d:\\test.txt","r")
    print u"打开文件"
    f.read()
    print u"读取文件"
except IOError:
    print u"读取文件时出现异常"
else:
    print u"执行成功"