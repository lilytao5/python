# coding=utf-8
a = 6
b = 7
c = 8
t = 50
l = []

for i in range(t+1):
    s1 = a*i
    l.append(s1)
    for j in range(t+1):
        s2 = a*i + b*j
        l.append(s2)
        for k in range(t+1):
            s3 = a*i + b*j + c*k
            l.append(s3)
#排序
l.sort()
#去重
news = []
for i in l:
    if i not in news:
        news.append(i)
print ("组合生成最大的数是%s"%news[-1])

#提取不在列表中的数字
r = []
for i in range(6*t):
    if i in news:
        pass
    else:
        r.append(i)
print ("组合不能生成的数字%s"%r)
print ("不能生成的最大数字为%s"%r[-1])