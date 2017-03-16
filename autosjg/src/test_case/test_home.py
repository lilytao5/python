# coding:utf-8
# 从login模块导入Login类
import time
from autosjg.src.login import Login

# 这里用例直接继承了login.py中的类，继承过来后直接写case,也可以调用公共方法
class Testlogin(Login):

    def test_01(self):
        # 登录之后的case
        # 获取个人主页上的特征文字做验证对比
        text = self.driver.find_element_by_class_name("userguide").text
        print text
        self.assertEqual(text, u"使用引导")
        print "登录成功"

    def test_02(self):
        # 登录之后的case,还没想好
        pass

class Testcreatechart(Login):
    def test_01(self):
        pass
    def test_02(self):
        pass