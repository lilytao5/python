#!/usr/bin/env python
# coding=utf-8
class People(object):
    def __init__(self, a="girl", b="live"):
        self.friend = a
        self.live = b
        print "start"

    def hand(self):
        h = "hand:%s and %s"%(self.friend, self.live)
        return h

    def foot(self):
        f = "foot:%s and %s"%(self.friend, self.live)
        return f

if __name__=="__main__":
    girl = People()
    print girl.hand()

    boy = People(a="boy")
    print boy.hand()

    woman = People(b="limb")
    print woman.hand()

    man = People(a="boy", b="limb")
    print man.hand()
