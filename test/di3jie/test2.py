#!/usr/bin/env python
# coding=utf-8
a = 1 #全局

class T():

    b = 2 #整个类有效

    def __init__(self):
        self.c = 2 #加了self就等于整个类有效了
        d = 3 #本方法有效
        print d

        self.addd = self.add() #将方法变为熟悉

    def add(self):
        e = 5
        self.f = 6
        return e+self.f

    def aee(self):
        g = 7
        h = a+self.b+self.c+self.f+g
        print h

if __name__=="__main__":
    s=T()
    print s.add()
    print s.addd
    s.aee()