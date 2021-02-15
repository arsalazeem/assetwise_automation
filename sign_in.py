from selenium.webdriver.common.by import By
import time
import init_chrome

driver=init_chrome.start()
driver.get("hhttp://54.186.118.166:3600/auth/signin")
driver.implicitly_wait(40)
driver.find_element(By.XPATH,'//*[@id="root"]/form/div/div/div/div[1]/div[1]/input').send_keys("asifsaeed@yopmail.com")
driver.find_element(By.XPATH,'//*[@id="root"]/form/div/div/div/div[1]/div[2]/input').send_keys("12345678")
driver.find_element(By.XPATH,'//*[@id="root"]/form/div/div/div/button').click()



