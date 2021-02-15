from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import random
import pdb
import init_chrome

payload={
    "f_name":"arsal",
    "l_name":"azeem",
    "email":str(random.randint(1,1000))+"azeem@vizteck.com",
    "password":"12345678",
    "c_name":"vizteckians",
    "country_name":"Pakistan"

}


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

def writekey_withname(driver,name,text):
    driver.find_element(By.NAME,name).send_keys(text)
    return driver

def drop_down_select(driver,xpath,text):
    select = Select(driver.find_element(By.XPATH,xpath))
    select.select_by_visible_text(text)
    return driver


driver=init_chrome.start()
driver.get("http://54.186.118.166:3600/auth/signup-1")
driver.implicitly_wait(30)
driver=writekeys(driver,'//*[@id="root"]/div/div[2]/div/div/form/div[1]/div/div[1]/input',payload["f_name"])
driver=writekeys(driver,'//*[@id="root"]/div/div[2]/div/div/form/div[1]/div/div[2]/input',payload["l_name"])
driver=writekeys(driver,'//*[@id="root"]/div/div[2]/div/div/form/div[2]/div/div/input',payload["email"])
driver=writekeys(driver,'//*[@id="root"]/div/div[2]/div/div/form/div[3]/div/div/input',payload["password"])
driver=writekeys(driver,'//*[@id="root"]/div/div[2]/div/div/form/div[4]/div/div/input',payload["password"])
driver=writekeys(driver,'//*[@id="root"]/div/div[2]/div/div/form/div[5]/div/div/input',payload["c_name"])
driver=makeclick(driver,'terms',"name")
driver=makeclick(driver,'//*[@id="root"]/div/div[2]/div/div/form/div[8]/div/div[2]/button')
driver=writekeys(driver,'//*[@id="root"]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/form/div[1]/div[2]/div[1]/div/div/input',payload["c_name"])
driver=drop_down_select(driver,'//*[@id="root"]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/form/div[1]/div[2]/div[2]/div/div/select','Pakistan')
pdb.set_trace()
