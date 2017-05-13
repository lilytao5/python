# coding:utf-8
from sjg.common.help import Help
data_url = "https://shujuguan.shujuguan.cn/#datacenter/data"


class LoginPage(Help):
    # 定位器，定位页面元素
    username_loc = ("css", '.selected>span')  # 输入账号
    password_loc = ("id", 'password')
    submit_loc = ("class name", 'btn-submit')
    remember_loc = ('id', 'remember')
    retrieve_loc = ('link text', '忘记密码')
    register_loc = ('class name', 'btn-gologin')

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
        '''记住我'''
        self.click(self.remember_loc)

    def click_retrieve(self):
        '''忘记密码'''
        self.click(self.retrieve_loc)

    def click_register(self):
        '''注册新账号'''
        self.click(self.register_loc)

    def login(self, username, password):
        '''登录方法'''
        self.input_username(username)
        self.input_password(password)
        self.click_submit()