# encoding: utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import unittest,time,xlrd
#import xdrlib ,sys
def open_excel(file= 'yoyo-login.xlsx'):
        try:
                data = xlrd.open_workbook(file) #打开exl文件读取数据
                return data
        except Exception,e:
                print str(e)
        #根据索引获取Excel表格中的数据 参数:file：Excel文件路径 colnameindex：表头列名所在行的索引 ，by_index：表的索引
def excel_table_byindex(file= 'yoyo-login.xlsx',colnameindex=0,by_index=0):
        data = open_excel(file)
        table = data.sheets()[by_index] #通过索引顺序获取一个工作表
        nrows = table.nrows #行数
        colnames = table.row_values(colnameindex) #某一行数据
        list =[]
        for rownum in range(1,nrows):
                row = table.row_values(rownum)
                if row:
                        app = {}
                        for i in range(len(colnames)):
                                app[colnames[i]] = row[i]
                        list.append(app)
        return list
def Login():
        listdata = excel_table_byindex("d:\login.xlsx" , 0)
        if (len(listdata) <= 0 ):
                assert 0 , u"Excel数据异常"
        for i in range(0 , len(listdata) ):
                driver = webdriver.Chrome()
                driver.get("https://workyun.0com/")
                #点击登录按钮

                # driver.find_element("xpath","html/body/div[2]/section[1]/div/div[2]/header/nav/div[3]/ul/li[1]/a").click()
                # time.sleep(1)
                # driver.find_element("id","passname").send_keys()

                driver.find_element_by_xpath("html/body/div[2]/section[1]/div/div[2]/header/nav/div[3]/ul/li[1]/a").click()
                time.sleep(1)
                driver.find_element(listdata[i]['way'],listdata[i]['element']).send_keys(listdata[i]['passname'])
                driver.find_element_by_id('password').send_keys(listdata[i]['password'])
                driver.find_element("class name","ee-btn-ok").click()
                time.sleep(2)
                try:
                        elem = driver.find_element_by_xpath("//div[3]/div/div[1]/div[1]/a/img")
                except NoSuchElementException:
                        assert 0 , u"登录失败，找不到左上角头像"
                driver.close()
if __name__ == '__main__':
    Login()