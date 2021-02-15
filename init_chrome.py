from selenium import webdriver



def start():
    driver = webdriver.Chrome(executable_path='drivers/linux/chromedriver')
    driver.maximize_window()
    return driver

def start_minize():
    driver = webdriver.Chrome(executable_path='drivers/linux/chromedriver')
    driver.minimize_window()
    return driver


if __name__ == '__main__':
    start()