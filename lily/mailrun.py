# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import os
import unittest
import HTMLTestRunner

# 定义发送邮件
def send_mail(report_file):
    sender = "pgvh@163.com"
    receiver = "23908092@qq.com"
    smtpserver = "smtp.163.com"
    username = "pgvh@163.com"
    password = "lilytao520"
    subject = "自动化测试报告"

    with open(report_file,"rb") as f:
        mail_body = f.read()

    msg = MIMEMultipart()
    body = MIMEText(mail_body,_subtype="html",_charset='utf-8')
    msg['from'] = sender
    msg['to'] = receiver
    msg['subject'] = subject
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    msg.attach(body)

    att = MIMEText(open(report_file).read(),"base64","utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= "report.html"'
    msg.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    print "test report email has send out !"

#发送最新测试报告
def send_report():
    result_dir = "F:\\python\\lily\\report"
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn:os.path.getmtime(result_dir+"\\"+fn))
    print (u'最新测试生成的报告:'+lists[-1])
    #找到最新生成的报告文件
    report_file = os.path.join(result_dir,lists[-1])
    print report_file
    #调用发邮件函数
    send_mail(report_file)

#将用例添加到套件
def creatsuite():
    testunit = unittest.TestSuite()
    #定义文件查找目录
    test_dir = "F:\\python\\lily\\test_case"
    #定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(test_dir,
                                                   pattern="test*.py",
                                                   top_level_dir=None)
    #discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print testunit
    return testunit

if __name__== "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = "F:\\python\\lily\\report\\"+now+"result.html"
    fp = open(filename,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告',
                                           description=u'用例执行情况')
    runner.run(creatsuite())
    fp.close()
    send_report()