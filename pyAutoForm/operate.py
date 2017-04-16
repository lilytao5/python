# coding=utf-8
__author__ = 'maohuan'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from browserManage import BrowserManage
import datetime
import filecmp
import urllib2
import time
import os
def getErrInfo(xpath,op, value,errInfo):
    return "Xpath(%s),Operate(%s),Value(%s):%s" % (xpath,op,value,errInfo)


class Operate(object):
    def __init__(self, _webdriver):
        self.driver = _webdriver
        self.YES = "yes"
        self.NO = "no"
        self.SPLITMARK = "###"


    def operate(self, op, xpath, value):
        operateDic = {
            "get": self.get,
            "click": self.click,
            "selectornot": self.selectOrNot,
            "sendkeys": self.sendKeys,
            "selectbyvalue": self.selectByValue,
            "selectbytext": self.selectByText,
            "selectbyindex": self.selectByIndex,
            "textcontains": self.textContains,
            "executejs": self.executeJs,
            "mustexist": self.mustExist,
            "switchtoframe":self.switchToFrame,
            "switchtodefaultcontent":self.switchToDefaultContent,
            "textequals":self.textEquals,
            "valueequals":self.valueEquals,
            "isexist":self.isExist,
            "existinsecs":self.ExistInSecs,
            "isdisplayed":self.isDisplayed,
            "isselected":self.isSelected,
            "isenabled":self.isEnabled,
            "upload":self.upload,
            "moveoverelement":self.moveOverElement,
            "contextclick":self.contextClick,
            "sameaslocalfiles":self.sameAsLocalFile,
            "waitforsecs":self.waitForSecs,
            "execute":self.execute,
            "alertaccept":self.alertAccept,
            "alertdismiss":self.alertDismiss,
        }
        try:
            return operateDic.get(op.lower())(xpath, value)
        except  Exception as e:
            return {"state": False, "info": getErrInfo(xpath,op,value,str(e))}


    def get(self, xpath, value):
        result = {}
        try:
            self.driver.get(value)
            self.driver.implicitly_wait(1)
            result = {"state": True, "info": ""}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"get",value,str(e))}
        return result

    def click(self, xpath, value):
        result = {}
        try:
            self.driver.find_element_by_xpath(xpath).click()
            self.driver.implicitly_wait(3)
            result = {"state": True, "info": ""}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"click",value,str(e))}
        return result


    def selectOrNot(self, xpath, value):
        result = {}
        isYES = self.YES == value.lower()
        try:
            element = self.driver.find_element_by_xpath(xpath)
            if (not element.is_selected()):
                if (isYES):
                    element.click()
            else:
                if (not isYES):
                    element.click()
            result = {"state": True, "info": ""}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"selectOrNot",value,str(e))}
        return result

    def sendKeys(self, xpath, value):
        result = {}
        try:
            self.driver.find_element_by_xpath(xpath).clear()
            self.driver.find_element_by_xpath(xpath).send_keys(value)
            result = {"state": True, "info": ""}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"sendKeys",value,str(e))}
        return result

    def selectByValue(self, xpath, value):
        result = {}
        try:
            element = self.driver.find_element_by_xpath(xpath)
            BrowserManage.selectByValue(self.driver, element, value)
            result = {"state": True, "info": ""}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"selectByValue",value,str(e))}
        return result

    def selectByText(self, xpath, value):
        result = {}
        try:
            element = self.driver.find_element_by_xpath(xpath)
            BrowserManage.selectByText(self.driver, element, value)
            result = {"state": True, "info": ""}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"selectByText",value,str(e))}
        return result

    def selectByIndex(self, xpath, value):
        result = {}
        try:
            element = self.driver.find_element_by_xpath(xpath)
            BrowserManage.selectByIndex(self.driver, element, int(value))
            result = {"state": True, "info": ""}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"selectByIndex",value,str(e))}
        return result

    def textContains(self, xpath, value):
        result = {}
        try:
            t_text = self.driver.find_element_by_xpath(xpath).text
            if (t_text.__contains__(value)):
                result = {"state": True, "info": ""}
            else:
                result = {"state": False, "info": getErrInfo(xpath, "textContains",value,"don't contains " + value)}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"textContains",value,str(e))}
        return result

    def executeJs(self, xpath, value):
        result = {}
        try:
            if (value.__contains__("return ") and value.__contains__(self.SPLITMARK)):
                indx = value.find(self.SPLITMARK)
                jsStr = value[:indx]
                reVe = value[indx + self.SPLITMARK.__len__():]
                reVr = str(self.driver.execute_script(jsStr))
                self.driver.implicitly_wait(2)
                if (reVe == reVr):
                    result = {"state": True, "info": ""}
                else:
                    result = {"state": False,
                              "info": "js-%s- expectedValue-%s- is't same with realValue-%s-" % (jsStr, reVe, reVr)}
            else:
                self.driver.execute_script(value)
                self.driver.implicitly_wait(2)
                result = {"state": True, "info": ""}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"executeJs",value,str(e))}
        return result

    def mustExist(self,xpath, value):
        result = {}
        if(not BrowserManage.isElementPresent(self.driver,By.XPATH,xpath)):
            raise ValueError,getErrInfo(xpath,"mustExist",value,"is not Exist!")
        else:
            result = {"state": True, "info": ""}
        return result

    def switchToFrame(self,xpath,value):
        try:
            frameElement=self.driver.find_element_by_xpath(xpath)
            self.driver.switch_to.frame(frameElement)
            result = {"state": True, "info": ""}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"switchToFrame",value,str(e))}
        return result

    def switchToDefaultContent(self,xpath,value):
        try:
            self.driver.switch_to.default_content()
            result = {"state": True, "info": ""}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"switchToDefaultContent",value,str(e))}
        return result


    def textEquals(self,xpath,value):
        try:
            element = self.driver.find_element_by_xpath(xpath)
            disText=BrowserManage.slimmingString(element.text)
            if ( value.strip()==disText):
                result = {"state": True, "info": ""}
            else:
                result = {"state": False, "info": getErrInfo(xpath, "textEquals",value,"isn't same as realText:" \
                                                             + disText)}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"isDisplayed",value,str(e))}
        return result

    def valueEquals(self,xpath,value):
        try:
            element = self.driver.find_element_by_xpath(xpath)
            disValue=element.get_attribute("value")
            if (value==disValue):
                result = {"state": True, "info": ""}
            else:
                result = {"state": False, "info": getErrInfo(xpath, "valueEquals",value,"isn't same as realValue:" \
                                                             + disValue)}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"isDisplayed",value,str(e))}
        return result

    def isExist(self,xpath,value):
        try:
            disState=BrowserManage.isElementPresent(self.driver,By.XPATH,xpath)
            if (disState and value.lower()==self.YES):
                result = {"state": True, "info": ""}
            elif((not disState) and value.lower()==self.NO):
                result = {"state": True, "info": ""}
            else:
                result = {"state": False, "info": getErrInfo(xpath, "isExist",value,"isn't same as realState:" \
                                                             + disState)}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"isExist",value,str(e))}
        return result

    def ExistInSecs(self, xpath, value):
        try:
            t = 0
            disState = False
            while (t <= value):
                if (BrowserManage.isElementPresent(self.driver, By.XPATH, xpath)):
                    disState = True
                    break
                else:
                    time.sleep(0.25)
                    t = t + 0.25
            if (disState and value.lower() == self.YES):
                result = {"state": True, "info": ""}
            elif ((not disState) and value.lower() == self.NO):
                result = {"state": True, "info": ""}
            else:
                result = {"state": False, "info": getErrInfo(xpath, "isDisplayed", value, "isn't e:" \
                                                             + disState)}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath, "isDisplayed", value, str(e))}
        return result

    def isDisplayed(self,xpath,value):
        try:
            element = self.driver.find_element_by_xpath(xpath)
            disState=element.is_displayed()
            if (disState and value.lower()==self.YES):
                result = {"state": True, "info": ""}
            elif((not disState) and value.lower()==self.NO):
                result = {"state": True, "info": ""}
            else:
                result = {"state": False, "info": getErrInfo(xpath, "isDisplayed",value,"isn't same as realState:" \
                                                             + disState)}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"isDisplayed",value,str(e))}
        return result

    def isSelected(self,xpath,value):
        try:
            element = self.driver.find_element_by_xpath(xpath)
            disState=element.is_selected()
            if (disState and value.lower()==self.YES):
                result = {"state": True, "info": ""}
            elif((not disState) and value.lower()==self.NO):
                result = {"state": True, "info": ""}
            else:
                result = {"state": False, "info": getErrInfo(xpath, "isSelected",value,"isn't same as realState:" \
                                                             + disState)}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"isSelected",value,str(e))}
        return result

    def isEnabled(self,xpath,value):
        try:
            element = self.driver.find_element_by_xpath(xpath)
            disState=element.is_enabled()
            if (disState and value.lower()==self.YES):
                result = {"state": True, "info": ""}
            elif((not disState) and value.lower()==self.NO):
                result = {"state": True, "info": ""}
            else:
                result = {"state": False, "info": getErrInfo(xpath, "isEnabled",value,"isn't same as realState:" \
                                                             + disState)}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"isEnabled",value,str(e))}
        return result

    def moveOverElement(self,xpath,value):
        try:
            element = self.driver.find_element_by_xpath(xpath)
            BrowserManage.moveOverElement(self.driver,element)
            result = {"state": True, "info": ""}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"moveOverElement",value,str(e))}
        return result

    def contextClick(self,xpath,value):
        try:
            element = self.driver.find_element_by_xpath(xpath)
            BrowserManage.contextClick(self.driver,element)
            result = {"state": True, "info": ""}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"contextClick",value,str(e))}
        return result

    def waitForSecs(self,xpath,value):
        try:
            time.sleep(int(value))
            result = {"state": True, "info": ""}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"waitForSec",value,str(e))}
        return result

    def execute(self,xpath,value):
        try:
            valList=value.split(self.SPLITMARK)
            if(len(valList)>1):
                exec(valList[0])
                if(eval(valList[1])==True):
                    result = {"state": True, "info": ""}
                else:
                    result = {"state": False, "info": ""}
            else:
                exec(value)
                result = {"state": True, "info": ""}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"execute",value,str(e))}
        return result


    def upload(self,xpath,value):
        try:
            element = self.driver.find_element_by_xpath(xpath)
            BrowserManage.upload(self.driver,element,value)
            result = {"state": True, "info": ""}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"upload",value,str(e))}
        return result

    def alertAccept(self,xpath,value):
        try:
            alert=Alert(self.driver)
            alert.accept()
            result = {"state": True, "info": ""}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"closeAlert",value,str(e))}
        return result

    def alertDismiss(self,xpath,value):
        try:
            alert=Alert(self.driver)
            alert.dismiss()
            result = {"state": True, "info": ""}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"alertDismiss",value,str(e))}
        return result

    #下载网络文件与本地文件一致，仅限img标签与a标签;非WebDriver处理方法
    def sameAsLocalFile(self,xpath,value,proxy=""):
        try:
            element = self.driver.find_element_by_xpath(xpath)
            tagName=element.tag_name
            if(tagName.lower()=="img"):
                urlPath=element.get_attribute("0src")
            elif(tagName.lower()=="a"):
                urlPath=element.get_attribute("href")
            else:
                raise ValueError("the elemnet's tag is neither <img> nor <a>!")
            localFileDir=os.path.abspath(os.path.dirname(value))
            #检查是否存在下载临时文件夹及临时文件，没有的话，创建一个
            tempDir=os.path.join(localFileDir,"temp")
            if(not os.path.exists(tempDir)):
                os.makedirs(tempDir)
            tempFile=os.path.join(tempDir,"tmp"+datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

            if(os.path.exists(tempFile)):
                os.remove(tempFile)
            #下载文件到临时文件夹
            cookieStr=BrowserManage.getCookieString(self.driver)
            if(proxy=="" or proxy==None):
                opener = urllib2.build_opener()
            else:
                proxy_handler = urllib2.ProxyHandler({"http" : proxy})
                opener = urllib2.build_opener(proxy_handler)
            opener.addheaders.append(("Cookie", cookieStr))
            #print cookieStr
            f = opener.open(urlPath)
            with open(tempFile, "wb") as stream:
                stream.write(f.read())
            time.sleep(5)
            #比较
            rs=filecmp.cmp(tempFile, value, 1)
            if(rs):
                result = {"state": True, "info": ""}
            else:
                result = {"state": False, "info": getErrInfo(xpath,"sameAsLocalFile",value,"isn't same as localfile:"\
                        +value)}
            if(os.path.exists(tempDir)):
                import shutil
                shutil.rmtree(tempDir)
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"sameAsLocalFile",value,str(e))}
        return result
