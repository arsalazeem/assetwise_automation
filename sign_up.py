from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pdb
import init_chrome
def writekeys(driver,path,text):
    driver.find_element(By.XPATH,path).send_keys(text)
    return driver
def makeclick(driver,path_name,method="click"):
    if method=="click":
        driver.find_element(By.XPATH, path_name).click()
        return driver
    if method=="name":
        driver.find_element(By.NAME,path_name).click()
        return driver




driver=init_chrome.start()
driver.get("https://nesma.ondemandstartup.com/auth/signup-1")
driver.implicitly_wait(30)
driver=writekeys(driver,'//*[@id="root"]/div/div[2]/div/div/form/div[1]/div/div[1]/input','arsal')
driver=writekeys(driver,'//*[@id="root"]/div/div[2]/div/div/form/div[1]/div/div[2]/input','azeem')
driver=writekeys(driver,'//*[@id="root"]/div/div[2]/div/div/form/div[2]/div/div/input','whereareyou1@yopmail.com')
driver=writekeys(driver,'//*[@id="root"]/div/div[2]/div/div/form/div[3]/div/div/input','12345678')
driver=writekeys(driver,'//*[@id="root"]/div/div[2]/div/div/form/div[4]/div/div/input','12345678')
driver=writekeys(driver,'//*[@id="root"]/div/div[2]/div/div/form/div[5]/div/div/input',"Vizteck")
driver=makeclick(driver,'terms',"name")
driver=makeclick(driver,'//*[@id="root"]/div/div[2]/div/div/form/div[8]/div/div[2]/button')

pdb.set_trace()
