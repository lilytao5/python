# coding=utf-8
def t1(a,b):
    c=a+b
    return c
if __name__=="__main__":
    print t1(6,2)

class Jisuan():
    def sub(self,a,b):
        c=a-b
        return c
test1 = Jisuan()
if __name__=="__main__":
    print test1.sub(6,2)

class Jisuan2(Jisuan):
    def chen(self,a,b):
        c=a*b
        return c
test = Jisuan2()
if __name__=="__main__":
    print test.chen(6,2)