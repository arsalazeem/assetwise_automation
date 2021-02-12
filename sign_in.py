from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import init_chrome

driver=init_chrome.start()
driver.get("https://nesma.ondemandstartup.com/auth/signin")
driver.implicitly_wait(40)
driver.find_element(By.XPATH,'//*[@id="root"]/form/div/div/div/div[1]/div[1]/input').send_keys("asifsaeed@yopmail.com")
driver.find_element(By.XPATH,'//*[@id="root"]/form/div/div/div/div[1]/div[2]/input').send_keys("12345678")
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="root"]/form/div/div/div/button').click()



