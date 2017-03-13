# coding:utf-8
# 从login模块导入Login类
import time

from lily.src.login import Login


# 这里用例直接继承了前面的类，继承过来后直接写case,也可以调用公共方法
class Test_home(Login):
    def test_01(self):
        # 个人主页博客地址测试
        self.login("liyan@gbase.cn", "111111")

        # 登录之后的case
        # 获取个人主页上的特征文字
        text = self.driver.find_element_by_class_name("userguide").text
        print text
        self.assertEqual(text, u"使用引导")

    # def test_02(self):
    #     self.login("liyan@gbase.cn", "111111")
    #     # 登录之后的case
    #     # 后面的case自由发挥吧