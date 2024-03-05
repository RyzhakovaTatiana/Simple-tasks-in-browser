from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By



"""Настройка драйвера"""
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
g = Service('E:/PycharmProjects/pythonProject/python_selenium_m1/chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://testpages.eviltester.com/styled/basic-html-form-test.html'
driver.get(base_url)
driver.maximize_window()

radio_button = driver.find_element(By.XPATH, '//input[@value="rd2"]')
radio_button.click()
radio_button = driver.find_element(By.XPATH, '//input[@value="rd1"]')
radio_button.click()





time.sleep(3)
driver.close()



