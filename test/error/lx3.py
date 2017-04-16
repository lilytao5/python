#!/usr/bin/env python
# coding=utf-8
a=56
if a>5:
    raise MyselfdefError

print "后面就不执行了"


class MyselfdefError(Exception):
    pass