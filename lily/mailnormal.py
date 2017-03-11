# coding=utf-8
import smtplib
from email.mime.text import MIMEText

sender = "pgvh@163.com" #发送邮箱账号
receiver = "23908092@qq.com" #接收邮箱账号
smtpserver = "smtp.163.com" #发送邮箱服务器
username = "pgvh@163.com" #邮箱账号
password = "lilytao520" #邮箱密码
subject = "this is a no att mail" #邮件主题

# body = "<pre><h1>我是一封无附件的测试邮件</pre></h1>" #邮件正文
report_file = "D:\\Python\\README.txt" #以下三行是按照指定文件内容发送正文，“rb是以二进制读模式打开”，
with open(report_file,"rb")as f:
    body = f.read()

#制定模板容器
msg = MIMEText(body,'html','utf-8')
# print type(msg)
msg['from'] = sender
msg['to'] = receiver
msg['subject'] = subject

#定义一个邮件实例
smtp = smtplib.SMTP()
smtp.connect(smtpserver) #链接服务器
smtp.login(username,password) #登录
smtp.sendmail(sender,receiver,msg.as_string()) #发送邮件
smtp.quit() #退出