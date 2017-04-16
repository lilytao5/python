#!/usr/bin/env python
# coding=utf-8
class People(object):

    def __init__(self, a="girl", b="live"):
        self.friend = a
        self.live = b
        print "start"

    def hand(self):
        h = "手:%s and %s"%(self.friend, self.live)
        return h

    def foot(self):
        f = "脚:%s and %s"%(self.friend, self.live)
        return f

if __name__=="__main__":
    a = People()
    b = People("boy")
    c = People(b="limb")

    print a.hand()
    print b.hand()
    print c.hand()