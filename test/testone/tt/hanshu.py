# coding=utf-8
# 普通实现
# a = 1
# b = 9
# c = a+b
# print c

# 函数实现
def add(a,b): #定义函数
    c=a+b
    return c

d=add(1,9) #调用函数
if __name__=="__main__":
    print d

class Test():
    def add(self, a,b):
        c = a+b
        return c

    def sub(self, a,b):
        c = a-b
        return c

class Case(Test):
    def chen(self,a,b):
        c=a*b
        return c

test = Test()
if __name__=="__main__":
    print test.add(9,1)
    print test.sub(9,1)
#
test =Case()
if __name__=="__main__":
    print test.chen(9,1)
