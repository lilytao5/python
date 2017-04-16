# coding=utf-8
__author__ = 'maohuan'
import re
import os
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from operate import Operate
from browserManage import BrowserManage
from excelManage import ExcelManage

def getErrInfo(xpath, op,value,errInfo):
    return "Xpath(%s),Operate(%s),Value(%s):%s" % (xpath,op,value,errInfo)



class AutoForm(object):
    def __init__(self, bm):
        self.YES = "yes"
        self.NO = "no"
        self.SPLITMARK = "###"
        self.XPATHARG ="{@@}"
        self.driver = bm.getDriver()
        self.proxyIp= bm.getIp()
        self.proxyPort=bm.getPort()
        #self.driver = webdriver.Chrome()
        self.operate = Operate(self.driver)
        self.currentWindow = self.driver.current_window_handle
        self.defaultWindow = self.driver.current_window_handle


    def getCurrentWindow(self):
        return self.currentWindow

    def getDefaultWindow(self):
        return self.defaultWindow

    def setCurrentWindow(self, cWindow):
        self.currentWindow = cWindow

    def setDefaultWindow(self, dWindow):
        self.defaultWindow = dWindow

    def getDriver(self):
        return self.driver


    '''
    结合operate中操作，生成带窗口状态处理的新操作
    '''
    def doOperate(self, op, xpath, value):
        operateDic = {
            "closeotherwindows": self.closeOtherWindows,
            "switchtowindowbyclick": self.switchToWindowByClick,
            "switchtodefaultwindow": self.switchToDefaultWindow,
            "setcurrwinasdefault": self.setCurrWinAsDefault
        }
        try:
            if (operateDic.has_key(op.lower())):
                return operateDic.get(op.lower())(xpath, value)
            else:
                #处理非WebDriver处理的请求方法
                if(op.lower()=="sameaslocalfile"):
                    if (self.proxyIp <> "" and self.proxyIp <> None):
                        t_proxy=self.proxyIp+str(self.proxyPort)
                    else:
                        t_proxy=""
                    return self.operate.sameAsLocalFile(xpath, value,proxy=t_proxy)
                else:
                    return self.operate.operate(op.lower(), xpath, value)
        except  Exception as e:
            return {"state": False, "info": getErrInfo(xpath,op,value,str(e))}

    '''
    设置当前窗口作为默认窗口
    '''
    def setCurrWinAsDefault(self,xpath,value):
        result = {}
        try:
            self.setDefaultWindow(self.driver.current_window_handle)
            self.setCurrentWindow(self.driver.current_window_handle)
            result = {"state": True, "info": ""}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"setCurrWinAsDefault",value,str(e))}
        return result

    '''
    关闭当前窗口以外的窗口
    '''
    def closeOtherWindows(self, xpath, value):
        result = {}
        try:
            allWindows = self.driver.window_handles
            for i in range(0, allWindows.__len__()):
                tempWindow = allWindows.__getitem__(i)
                if (self.currentWindow <> tempWindow):
                    self.driver.switch_to.window(tempWindow)
                    self.driver.close()
                self.driver.switch_to.window(self.currentWindow)
                self.setDefaultWindow(self.driver.current_window_handle)
                self.setCurrentWindow(self.driver.current_window_handle)
                result = {"state": True, "info": ""}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"closeOtherWindows",value,str(e))}
        return result


    '''
    点击某个元素后，打开新窗口，并指向新窗口
    '''
    def switchToWindowByClick(self, xpath, value):
        result = {}
        try:
            oriWindows = self.driver.window_handles
            self.driver.find_element_by_xpath(xpath).click()
            self.driver.implicitly_wait(3)
            nowWindows = self.driver.window_handles
            newWindow = None
            for i in range(0, nowWindows.__len__()):
                t = nowWindows.__getitem__(i)
                try:
                    oriWindows.index(t)
                    continue
                except:
                    newWindow = t
                    break
            if (newWindow <> None):
                self.driver.switch_to.window(newWindow)
                self.setCurrentWindow(self.driver.current_window_handle)
                result = {"state": True, "info": ""}
            else:
                result = {"state": False, "info": getErrInfo(xpath,"switchToWindowByClick",value,"can't find new Window by click this element!")}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"switchToWindowByClick",value,str(e))}
        return result

    '''
    指向原窗口
    '''
    def switchToDefaultWindow(self, xpath, value):
        result = {}
        try:
            self.driver.switch_to.window(self.getDefaultWindow())
            self.setCurrentWindow(self.driver.current_window_handle)
            result = {"state": True, "info": ""}
        except Exception as e:
            result = {"state": False, "info": getErrInfo(xpath,"switchToDefaultWindow",value,str(e))}
        return result

    '''
    读取指定格式的datas，完成指定操作
    datas格式要求如下：
    datas=[
        {"xpath":"","op":"get","value":""},
        {"xpath":"//input[@id='logonInfo.logUserName']","op":"sendKeys","value":"dongfang"}
    ]
    '''
    def fixTheForm(self, title,datas,logDir=None,filePath=None,defaultParams=None):
        params={}
        if(defaultParams <> None and defaultParams.__len__()>0):
            for (k,v) in defaultParams.items():
                params.__setitem__(k,v)
                
        result = {"state": True, "info": self.getNowStrftime(),"title":">>>"+title}
        for i in range(datas.__len__()):
            tmp = datas.__getitem__(i)
            _op=tmp.get("op").lower()
            _xpath=tmp.get("xpath")
            _value=tmp.get("value")
            if(_op=="skip"):
                continue
            
            #处理保存参数操作,value是个有返回值的js语句
            pattern1=re.compile(r"\{@(\w+)@\}")
            m1=pattern1.match(_op)
            if(m1):
                try:
                    ret=str(self.driver.execute_script(_value))
                    self.driver.implicitly_wait(2)
                    params.__setitem__(m1.group(1),ret)
                    t_result = {"state": True, "info": ""}
                    result = self.mergeResult(result,t_result)
                    continue
                except Exception as e:
                    t_result = {"state": False, "info": getErrInfo(_xpath,"executeJs",_value,str(e))}
                    result = self.mergeResult(result,t_result)
                    continue

            #print params

            #处理带参数的xpath
            if (_xpath.__contains__(self.XPATHARG) and _value.__contains__(self.SPLITMARK)):
                indx = _value.find(self.SPLITMARK)
                xpathParm = _value[:indx]
                _xpath = _xpath.replace(self.XPATHARG,xpathParm)
                _value = _value[indx + self.SPLITMARK.__len__():]

            #处理value中含有参数
            pattern2=re.compile(r".*\{@(\w+)@\}.*")
            c=0
            while pattern2.match(_value) and c<100:  #防止无限循环
                m2=pattern2.match(_value)
                t_key=m2.group(1)
                c=c+1
                if(params.has_key(t_key)):
                    _value=_value.replace("{@"+t_key+"@}",params.get(t_key))
                else:
                    _value==_value.replace("{@"+t_key+"@}","{"+t_key+"}")

            #处理调用公共步骤
            if(_op=="call" and filePath<>None):
                dParams={}
                tValues=_value.split(self.SPLITMARK)
                if(tValues.__len__()>1):
                    for i in range(1,tValues.__len__()):
                        tParamValue=tValues[i].split("=")
                        dParams.__setitem__(tParamValue[0],tParamValue[1])
                t_result=self.runSteps(filePath,tValues[0],None,dParams).__getitem__(0)
                t_result.__setitem__("info",u"第"+str(i+1)+u"步调用公共步骤"+_value+":"+t_result.get("info"))
                result = self.mergeResult(result,t_result)
                continue

            #处理上传\比较下载文件操作的相对链接
            if((_op=="upload" or _op=="sameaslocalfile") and (not _value.__contains__(":"))):
                if(logDir<>None):
                    _value=os.path.join(os.path.dirname(logDir),_value)
                else:
                    print "can't find the logs dir,can't use the relative path"


            #处理正常操作
            t_result = self.doOperate(_op,_xpath,_value)
            if(not t_result.get("state")):
                if((_xpath or "").__len__()>0 and
                       BrowserManage.isElementPresent(self.driver,By.XPATH,_xpath)):
                    BrowserManage.scrollToElement(self.driver,self.driver.find_element_by_xpath(_xpath))
                if(logDir<>None):
                    snapFile=os.path.join(logDir,self.getNowStrftime2()+".png")
                    self.driver.get_screenshot_as_file(snapFile)
                    snapInfo="<img 0src=\"file:\\\\\\"+os.path.abspath(snapFile).strip()+"\" height=\"600\" width=\"800\">"
                else:
                    print "can't find the logs dir,can't use the relative path"
                    snapInfo=""
                t_result.__setitem__("info",u"第"+str(i+1)+u"步:"+t_result.get("info")+u"\n截图:\n"+snapInfo+"\n")
                result = self.mergeResult(result,t_result)
        if(result.get("state")):
            result.__setitem__("info",result.get("info")+" PASS\n")
        return result

    '''
    解析指定格式数据，将其解析成fixTheForm需要的数据
    originDatas的格式(元素名称)如下：
    '''
    def parseDatasFromStdExcel(self,filePath,sheetName):
        em=ExcelManage(filePath)
        dataStepSize=int(em.getDatasByCol(sheetName,1,0,1)[0])
        dataGroupSize=int(em.getDatasByCol(sheetName,2,0,1)[0])
        xpath_array=self.getXpathArrayFromStdExcel(filePath,sheetName,dataStepSize)
        datas=[]
        i=0
        while(i<dataGroupSize):
            piece=None
            runState=self.YES
            title=""
            isRun=em.getDatasByCol(sheetName,3+2*i,0,1)[0]
            if( isRun==u"忽略" or isRun==""):
                runState=self.NO
            title=em.getDatasByCol(sheetName,4+2*i,0,1)[0]
            op_array=em.getDatasByCol(sheetName,3+2*i,2,dataStepSize)
            value_array=em.getDatasByCol(sheetName,4+2*i,2,dataStepSize)
            piece=(runState,title,self.mergeInputDatas(xpath_array,op_array,value_array))
            datas.append(piece)
            i=i+1
        em.closeExcel()
        return datas

    '''
    获取xpathArray
    '''
    def getXpathArrayFromStdExcel(self,filePath,sheetName,dataSize):
        em=ExcelManage(filePath)
        sheetNames=em.getDatasByCol(sheetName,1,2,dataSize)
        elementNames=em.getDatasByCol(sheetName,2,2,dataSize)
        xpath_array=[]
        for i in range(0,dataSize):
            t_sheetName=sheetNames[i].strip()
            t_elementName=elementNames[i].strip()
            if(t_sheetName=="" or t_elementName==""):
                xpath_array.append("")
                continue
            else:
                idx=em.getIndexByCol(t_sheetName,1,t_elementName)
                if(idx>9000):
                    raise ValueError,"The (%d)st row in sheet(%s) of file(%s) has ERROR" % (i,sheetName,filePath)
                xpath_array.append(em.getDatasByCol(t_sheetName,2,idx,1)[0])
                continue
        return xpath_array


    '''
    合并xpath数组，操作数组，值数组.
    构成字典列表
    '''
    def mergeInputDatas(self,xpath_array,op_array,value_array):
        length=xpath_array.__len__()
        inputDatas=[]
        for i in range(0,length):
            t_op=""
            t_value=""
            if(i>=op_array.__len__()):
                t_op=""
            else:
                t_op=op_array[i]
            if(i>=value_array.__len__()):
                t_value=""
            else:
                t_value=value_array[i]
            inputDatas.append({"xpath":xpath_array[i],"op":t_op,"value":t_value})
        return inputDatas

    '''
    获取当前时间的格式化字符串
    '''
    def getNowStrftime(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    def getNowStrftime2(self):
        return datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    '''
    合并各个步骤的测试结果
    '''
    def mergeResult(self,result,t_result):
        result.__setitem__("state",result.get("state") and t_result.get("state"))
        result.__setitem__("info",result.get("info")+"\n"+t_result.get("info"))
        return result

    '''
    运行指定格式sheet页中的测试用例
    '''
    def runCase(self,filePath,sheetName,logsDir=None):
        datas=self.parseDatasFromStdExcel(filePath,sheetName)
        resultList=[]
        for i in range(0,datas.__len__()):
            piece=datas.__getitem__(i)
            runState=piece[0]
            if(runState==self.NO):
                continue
            else:
                title=piece[1]
                inputDatas=piece[2]
            t_result=self.fixTheForm(title,inputDatas,logDir=logsDir,filePath=filePath)
            resultList.append(t_result)
        return resultList


    '''
    运行指定格式sheet页中的测试用例
    '''
    def runSteps(self,filePath,sheetName,logsDir=None,dParams=None):
        datas=self.parseDatasFromStdExcel(filePath,sheetName)
        resultList=[]
        for i in range(0,datas.__len__()):
            piece=datas.__getitem__(i)
            runState=piece[0]
            if(runState==self.NO):
                continue
            else:
                title=piece[1]
                inputDatas=piece[2]
            t_result=self.fixTheForm(title,inputDatas,logDir=logsDir,filePath=filePath,defaultParams=dParams)
            resultList.append(t_result)
        return resultList

    '''
    获取指定格式excel中的测试集
    '''
    @staticmethod
    def getTestSuiteFromStdExcel(filePath):
        em=ExcelManage(filePath)
        caseCount=int(em.getDatasByCol(u'配置',3,0,1)[0])
        caseArray=em.getDatasByCol(u"配置",2,2,caseCount)
        stateArray=em.getDatasByCol(u"配置",3,2,caseCount)
        runCaseList=[]
        for i in range(0,caseCount):
            if(stateArray[i]<>u"忽略"):
                runCaseList.append(caseArray[i])
        return runCaseList



    '''
    退出WebDriver
    '''
    def quitDriver(self):
        self.driver.quit()





