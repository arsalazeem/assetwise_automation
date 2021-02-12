from selenium import webdriver
import time


def start():
    driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
    driver.maximize_window()
    return driver

def start_minize():
    driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
    driver.minimize_window()
    return driver


if __name__ == '__main__':
    start()