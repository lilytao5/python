#!/usr/bin/env python
# coding=utf-8
from selenium import webdriver
import time


class Login():

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, pwd):
        u"""这里写了一个登录的方法，账号和密码参数化"""
        self.driver.find_element("id","sf").send_keys(username)
        self.driver.find_element("id","w").send_keys(pwd)
        self.driver.find_element("xpath","sdf").click()
        time.sleep(3)

if __name__=="__main__":
    home = Login()
    home.l