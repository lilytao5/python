# coding:utf-8
def add(a,b):
    c=a+b
    return c
print add(8,3)

class Test():
    def sub(self,a,b):
        c=a-b
        return c
    def chen(self,a,b):
        c=a*b
        return c
test = Test()
print test.sub(8,3)
print test.chen(8,3)

class Jisuan(Test):
    def chu(self,a,b):
        c=a/b
        return c
jisuan=Jisuan()
print __name__
# if __name__=="__t1__":
    print jisuan.chu(8,3)
