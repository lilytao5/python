#!/usr/bin/env python
# coding=utf-8
l = [1,3,5,7,9]

# print sum(l)
# print dir(__builtins__)
# print help(len)


def add(a=1,b=2,d=3): #默认值为 0，有传值就用传的值算，不给值就用默认值算
    '''这个函数是一个加法
    simple use:
            1+2+3
    '''
    c = a+b+d
    return c
a = add(1,2,3)
print a
print add() #直接用默认值计算
print add(1) #只有一个值的时候是默认给第一个参数变值
print add(b=3,d=4)#改变非第一个参数时需要写明要给那个参数变值
help(add)

class Test():

    def aaa(self,a,b):
        return a+b


    def acc(self,a,b):
        print "jianfa"
        return a-b

    def aee(self,a,b):
        return a*b

    def aff(self,a,b):
        return a/b

a = Test()
print a.aaa(1,2),a.acc(1,2),a.aee(1,2),a.aff(1,2)