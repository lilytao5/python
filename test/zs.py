from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Remote(desired_capabilities=DesiredCapabilities.HTMLUNIT)
#browser = webdriver.DesiredCapabilities.HTMLUNIT() # Get local session of firefox
browser.get("http://www.yahoo.0com") # Load page
assert "Yahoo" in browser.title
elem = browser.find_element_by_name("p") # Find the query box
elem.send_keys("seleniumhq" + Keys.RETURN)
time.sleep(0.2) # Let the page load, will be added to the API
try:
    browser.find_element_by_xpath("//a[@data-bk='5174.1']")
    print"ok"
except NoSuchElementException:
    assert 0, "can't find seleniumhq"
browser.close() 
