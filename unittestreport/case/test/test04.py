# coding=utf-8
import unittest
test_dir = "E:\\python\\unittestreport\\case"
# report_dir = "E:\\python\\unittestreport\\report"

import time
c_time = time.strftime("%Y_%m_%d %H:%M:%S")
print c_time
report_name = "E:\\python\\unittestreport\\report"+c_time+"result.html"


def creatsuite(test_dir,patteeern="test*.py")
