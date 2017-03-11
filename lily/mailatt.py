# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = "pgvh@163.com"
receiver = "23908092@qq.com"
smtpserver = "smtp.163.com"
username = "pgvh@163.com"
password = "lilytao520"
subject = "含附件发送邮件"

msg = MIMEMultipart()
msg['form'] = sender
msg['to'] = receiver
msg['subject'] = subject

mail_body = "<pre><h1>测试报告00000000<h1><pre>"
body = MIMEText(mail_body, 'html', 'utf-8')
msg.attach(body)

# reportpath = "D:\\Python\\README.txt"
# mail_body = open(reportpath).read()
# att = MIMEText(mail_body,'base64','utf-8')
att = MIMEText(open('F:\\python\\lily\\att\\test.txt').read(),'base64','utf-8') #上面三句是抽成参数化写的
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename="report.txt"'
msg.attach(att)

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()