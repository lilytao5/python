#!/usr/bin/env python
# coding=utf-8
import time


def home(driver):
    driver.find_element("id","userguide").click()
    time.sleep(2)


def data(driver):
    driver.find_element("id","mydata").click()
    time.sleep(1)

