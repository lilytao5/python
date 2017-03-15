# coding=utf-8
import unittest
import HTMLTestRunner
test_dir = "f:\\python\\07test_p\\case"
import time
c_time = time.strftime("%Y_%m_%d %H_%M_%S")
# print c_time
report_name = "f:\\python\\07test_p\\report"+"\\report"+c_time+"result.html"

def creatsuite(test_dir,pattern="test*.py",top_level_dir=None):

    discover = unittest.defaultTestLoader.discover(test_dir,pattern,top_level_dir)
    # print discover
    testcase = unittest.TestSuite()
    for test_suite in discover:
        # print test_suite
        for test_case in test_suite:
            # print test_case
            testcase.addTests(test_case)
    # print testcase
    return testcase

if __name__=="__main__":
    # creatsuite(test_dir) #加载出来用例
    # 方法一:生成自己的测试报告
    # runner = unittest.TextTestRunner()  # 返回类的实例，之后就可以用他里面的方法了
    #

    # 方法二:生成导入的测试报告
    fp = open(report_name,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"XXX项目测试报告",description=u"执行情况：")
    #

    runner.run(creatsuite(test_dir))
    fp.close()