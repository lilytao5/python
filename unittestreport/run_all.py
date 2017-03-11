# coding:utf-8
import unittest

# test_dir = r"E:\python\unittestreport"
test_dir = "E:\\python\\unittestreport"
pattern = "test" \
          "*.py"
top_level_dir = None

def creatsuit(test_dir,pattern,top_level_dir):

    discover = unittest.defaultTestLoader.discover(test_dir,
                                                   pattern,
                                                   top_level_dir)

    # print discover
    testcase = unittest.TestSuite()
    for test_suite in discover:
        # print test_suite
        for test_case in test_suite:
            # print test_case
            testcase.addTests(test_case)
    print testcase
    return testcase

if __name__=="__main__":
    runner = unittest.TextTestRunner()
    runner.run(creatsuit(test_dir,pattern,top_level_dir))