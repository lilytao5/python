#!/usr/bin/env python
# coding:utf-8
# 从login模块导入Login类
from autosjg.index import Login

# 这里用例直接继承了login.py中的类，继承过来后直接写case,也可以调用公共方法
class Testlogin(Login):

    def test_01(self):
        # 登录之后的case
        title = self.driver.title
        print title
        self.assertEqual(title, u"数据观 - 所有人都能使用的数据分析工具")
        print "登录成功"

    def test_02(self):
        # 登录之后的case,还没想好
        pass

class Testcreatechart(Login):
    def test_01(self):
        pass
    def test_02(self):
        pass
