#!/usr/bin/env python
# coding=utf-8
import xlrd


def find_ele(elepath,r):
    dict = {} #字典
    list = [] #list
    lin = [0,2,3] #所取列数
    data = xlrd.open_workbook(elepath) # 打开xls文件
    table = data.sheets()[0] # 打开第一张表
    for num in lin: 
        if num != 0:
            list.append(table.cell(r,num).value)
        else:
            id = table.cell(r,num).value
    dict[id] = list
    return dict

# if __name__ == "__main__":
#     elepath = "F:\\python\\autosjg\\test_data\\element.xls"
#     table = find_ele(elepath, 1)
#     print table['EL91001'][0]