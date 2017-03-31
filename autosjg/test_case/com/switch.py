#!/usr/bin/env python
# coding=utf-8
import time
from selenium.webdriver.common.by import By

def home(driver):
    driver.find_element(By.ID,"userguide").click()
    time.sleep(3)

def data(driver):
    driver.find_element(By.ID,"mydata").click()
    time.sleep(3)

