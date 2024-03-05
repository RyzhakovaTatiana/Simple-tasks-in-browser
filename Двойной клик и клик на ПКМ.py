from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By



"""Настройка драйвера"""
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
g = Service('E:/PycharmProjects/pythonProject/python_selenium_m1/chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/buttons'
driver.get(base_url)
driver.maximize_window()



action = ActionChains(driver)
double = driver.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')
action.double_click(double).perform()



right_click = driver.find_element(By.XPATH, '//button[@id="rightClickBtn"]')
action.context_click(right_click).perform()

print('OK')

time.sleep(3)
driver.close()



