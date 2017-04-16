#coding=utf-8
__author__ = 'maohuan'
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import ui
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.by import By
import re

class BrowserManage(object):
    def __init__(self,browser="",ip="",port=0,timeout=30):
        self.browser=browser
        self.ip = ip
        self.port = port
        self.timeout = timeout
    def setBrowser(self, browser):
        self.browser = browser
    def setProxy(self, ip, port):
        self.ip = ip
        self.port = port
    def setTimeout(self, timeout):
        self.timeout = timeout
    def getBrowser(self):
        return self.browser
    def getIp(self):
        return self.ip
    def getPort(self):
        return self.port
    def getDriver(self):
        return BrowserManage.startDriver(_browser=self.browser,_ip=self.ip,_port=self.port,_timeout=self.timeout)


    #获取对应的webdriver
    @staticmethod
    def startDriver(_browser="chrome",_ip="",_port=0,_timeout=30):
        driver=None
        browser = _browser.lower()
        ip=_ip
        port=_port
        timeout=_timeout
        #默认chrome浏览器
        if not("firefox","chrome","ie").__contains__(browser):
            browser="chrome"
        myProxy = ip + ":" + str(port)
        if browser == "firefox":
            if (ip <> "" and ip <> 0):
                proxy = Proxy({
                    'proxyType': ProxyType.MANUAL,
                    'httpProxy': myProxy,
                    'ftpProxy': myProxy,
                    'sslProxy': myProxy,
                    'noProxy': ''
                })
                driver = webdriver.Firefox(proxy=proxy)
            else:
                driver = webdriver.Firefox()
        elif browser == "chrome":
            if (ip <> "" and ip <> 0):
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--proxy-server=%s' % myProxy)
                driver = webdriver.Chrome(chrome_options=chrome_options)
            else:
                cmd_switchProxy="reg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\" /v ProxyEnable /t REG_DWORD /d 0 /f & "+\
                        "reg add \"HKCU\\Software\\Microsoft\Windows\\CurrentVersion\\Internet Settings\" /v ProxyServer /d \"\" /f & "+\
                        "ipconfig /flushdns"
                os.system(cmd_switchProxy)
                driver = webdriver.Chrome()
        elif browser == "ie":
              #ie无法手动配置代理，配置系统代理
              if (ip <> "" and ip <> 0):
                    cmd_switchProxy="reg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\" /v ProxyEnable /t REG_DWORD /d 1 /f & "+\
                        "reg add \"HKCU\\Software\\Microsoft\Windows\\CurrentVersion\\Internet Settings\" /v ProxyServer /d \""+myProxy+"\" /f & "+\
                        "ipconfig /flushdns"
                    os.system(cmd_switchProxy)
              else:
                    cmd_switchProxy="reg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\" /v ProxyEnable /t REG_DWORD /d 0 /f & "+\
                        "reg add \"HKCU\\Software\\Microsoft\Windows\\CurrentVersion\\Internet Settings\" /v ProxyServer /d \"\" /f & "+\
                        "ipconfig /flushdns"
                    os.system(cmd_switchProxy)
              driver = webdriver.Ie()
        driver.set_page_load_timeout(timeout)
        driver.accept_next_alert = True
        return driver



    #处理HTML中展示的文本首尾的无效内容（空格符、换行符...）
    @staticmethod
    def slimmingString(value):
        t_v=value.replace("&nbsp;"," ")
        return t_v.strip()



    #滚轮滚动到对应元素
    @staticmethod
    def scrollToElement(driver, element):
        try:
            scrollto = "window.scrollTo(" + str(element.location.get("x")) + "," + str(
                element.location.get("y")) + ")"
            driver.execute_script(scrollto)
        except Exception as e1:
            print e1.message

    #鼠标移动到元素上
    @staticmethod
    def moveOverElement(driver,element):
        ActionChains(driver).move_to_element(element).perform()

    @staticmethod
    def singleClick(driver,element):
        ActionChains(driver).click(element).perform()

    @staticmethod
    def doubleClick(driver,element):
        ActionChains(driver).double_click(element).perform()

    @staticmethod
    def clickAndHold(driver,element):
        ActionChains(driver).click_and_hold(element).perform()

    @staticmethod
    def contextClick(driver,element):
        ActionChains(driver).context_click(element).perform()

    #拖拽元素1到元素2
    @staticmethod
    def drag_to_drop(driver,element1,element2):
        ActionChains(driver).drag_and_drop(element1,element2).perform()

    #复选框选中及不选中(0不选,>0选中)
    @staticmethod
    def checkTheCheckbox(driver,element,flag=1):
        if not element.is_selected():
            if(flag>0):
               element.click()
        else:
            if(flag==0):
                element.click()

    #下拉菜单，根据index选择
    @staticmethod
    def selectByIndex(driver,element,idx):
        ui.Select(element).select_by_index(idx)

    #下拉菜单,根据text选择
    @staticmethod
    def selectByText(driver,element,text):
        ui.Select(element).select_by_visible_text(text)

    #下拉菜单,根据value选择
    @staticmethod
    def selectByValue(driver,element,value):
        ui.Select(element).select_by_value(value)

    #判断元素是否存在
    @staticmethod
    def isElementPresent(driver,by,value):
        try:
            driver.find_element(by,value)
            return True
        except Exception as e1:
            return False

    # 在等待的一定秒数中，获取指定元素
    @staticmethod
    def getElementByWaitInSec(driver, by,value,secs):
        try:
            return ui.WebDriverWait(driver, secs).until(lambda x: x.find_element(by, value))
        except Exception as e1:
            print e1.message
            return None

    #获取cookie字符串
    @staticmethod
    def getCookieString(driver):
        Cookie=driver.get_cookies()
        tmp=""
        for c in Cookie:
            tmp=tmp+c["name"]+"="+c["value"]+"; "
        return tmp


    # 添加修改cookie
    @staticmethod
    def modifyCookie(driver, name, value=None, path=None, domain=None, secure=None, expiry=None):
        cookie = driver.get_cookie(name)
        _value = value
        _path = path
        _domain = domain
        _secure = secure
        _expiry = expiry
        if cookie:
            if not _value:
                _value = cookie["value"]
            if not _path:
                _path = cookie["path"]
            if not _domain:
                _domain = cookie["domain"]
            if not _secure:
                _secure = cookie["secure"]
            if not _expiry:
                _expiry = "Session"
            driver.delete_cookie(name)
        cookie_dic = {"name": name, "value": _value, "path":_path, "domain":_domain, "expiry":_expiry, "secure":_secure}
        driver.add_cookie(cookie_dic)

    #上传文件
    @staticmethod
    def upload(driver,element,filePath):
        filePath=os.path.abspath(filePath)
        element.send_keys(filePath)
