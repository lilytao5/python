#!/usr/bin/env python
# coding=utf-8
# --------------3IndexError-------------
# l = [1, "12", "23"]
# print l[3] #超出范围
# s = len(l)
# print s
# a = 3
# if a >= s:
#     print u"超出范围"
# else:
#     print 1[3]

# --------------4KeyError------------
# d = {"username": "lily",
#      "password": 111111}
# print d["username"]
# print d["password"]
# print d["password1"]

# --------------5TypeError------------
# l =["111","222","aaa"]
# d = {"username": "lily",
#      "password": 111111}
# print d["username"]
# print d["password"]
# print l["111"]

# --------------6ValueError数据类型错误“要的数值给传成字符串”------------
# def add(a,b):
#     return int(a+b)
#
# print add("a","b")

# --------------7AttributeError------------
# class Count():
#     def add(self,a,b):
#         return int(a+b)
# a = Count()
# print a.ad(1,2) #把add方法错写成ad方法就会报AttributeError
# print Count().add(1,2)

# --------------8IOError------------
# f = open("d:\\a.txt","r") #这个地址不存在，如果在此目录加上此文件就能解决了