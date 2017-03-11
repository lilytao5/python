# coding:utf-8
# 从login模块导入Blog类
from login import Bolg
import time

# 这里用例直接继承了前面的类，继承过来后直接写case,也可以调用公共方法
class Newblog(Bolg):
    def test_01(self):
        # 个人主页博客地址测试
        self.login(u"上海-悠悠", u"xxxx")
        # 登录之后的case
        self.driver.find_element_by_id("lnk_current_user").click() # 个人主页
        time.sleep(2)
        # 获取个人主页上的主页地址
        url = self.driver.find_element_by_class_name("gray").text
        print url
        self.assertEqual(url, "http://www.cnblogs.com/yoyoketang/")

    def test_02(self):
        self.login(u"上海-悠悠", u"xxxx")
        # 登录之后的case
        # 后面的case自由发挥吧