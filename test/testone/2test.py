# coding=utf-8
arr = [2, 9, 8, 0, 3, 4, 7]
index = [0, 2, 4, 4, 5, 3, 5, 6, 1]
QQ = ""
for i in index:
    QQ += str(arr[i])
print("联系方式QQ："+QQ)

a='12'
b='23'
c=a+b
print c

l=[1,   4,  3,  9,  20,   12]
l.sort()
print l
l.remove(20)
print l
del l[2]
print l