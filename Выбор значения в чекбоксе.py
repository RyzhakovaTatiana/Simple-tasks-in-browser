from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By



"""Настройка драйвера"""
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
g = Service('E:/PycharmProjects/pythonProject/python_selenium_m1/chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/checkbox'
driver.get(base_url)
driver.maximize_window()

check_box = driver.find_element(By.XPATH, '//button[@aria-label="Toggle"]')
check_box.click()


time.sleep(3)
driver.close()



