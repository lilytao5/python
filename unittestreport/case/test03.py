# coding:utf-8
import time
print time.time()
# print time.strftime(%Y_)

f = open("D:\\baidu.txt","r")
fp = f.read()
# for i in fp:
#     print i
#     i.split(",")
#     print i[0]
print fp
f.close()

f = open("d:\\123.txt","wb")
f.write("hello world")
f.close()
print "写入完成"

