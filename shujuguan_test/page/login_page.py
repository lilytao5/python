# coding:utf-8
from shujuguan_test.common.help_selenium import Help
login_url = "https://shujuguan.shujuguan.cn/"

class LoginPage(Help):
    # 定位器，定位页面元素
    username_loc = ('id', 'username')  # 输入账号
    password_loc = ('id', 'password')
    submit_loc = ('css', '.btn-submit')
    remember_loc = ('id', 'remember_me')
    retrieve_loc = ('link text', '找回')
    reset_loc = ('link text', '重置')
    register_loc = ('link text', '立即注册')
    feedback_loc = ('link text', '反馈问题')

    def input_username(self, username):
        '''输入账号框'''
        self.send_keys(self.username_loc, username)

    def input_password(self, password):
        '''输入密码框'''
        self.send_keys(self.password_loc, password)

    def click_submit(self):
        '''登录按钮'''
        self.click(self.submit_loc)

    def click_remember_live(self):
        '''下次记住登录'''
        self.click(self.remember_loc)

    def click_retrieve(self):
        '''找回密码'''
        self.click(self.retrieve_loc)

    def click_reset(self):
        '''重置密码'''
        self.click(self.reset_loc)

    def click_register(self):
        '''注册新账号'''
        self.click(self.register_loc)

    def click_feedback(self):
        '''反馈问题'''
        self.click(self.feedback_loc)

    def login(self, username, password):
        '''登录方法'''
        self.input_username(username)
        self.input_password(password)
        self.click_submit()

