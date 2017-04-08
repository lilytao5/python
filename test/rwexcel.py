#!/usr/bin/env python
# coding=utf-8
import xlrd


def open_excel(file = 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

def find_ele(elepath,r):
    data = open_excel(elepath) # 打开xls文件
    table = data.sheets()[0] # 打开第一张表
    way = table.cell(r,3).value #by方式
    content = table.cell(r,2).value #by内容
    return way, content
    # return content
    # return {'way': way,
    #         'content': content}

    # nrows = table.nrows # 获取表的行数
    # for i in range(nrows): # 循环逐行打印
    #     if i == 0: # 跳过第一行
    #         continue
    #     print table.row_values(i)[:2] # 取前三列
    #
    # cell00 = table.cell(0,0).value
    # print cell00

if __name__ == "__main__":
    elepath = "F:\\python\\autosjg\\test_data\\element.xls"
    table = ele(elepath, 1)
    print table