from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By



"""Настройка драйвера"""
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
g = Service('E:/PycharmProjects/pythonProject/python_selenium_m1/chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/text-box'
driver.get(base_url)
driver.maximize_window()


driver.execute_script("window.scrollTo(0, 30)")
new_url = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[9]')
new_url.click()
print('Пользователь перешел на страницу с тестированием кнопок')



"""Добавить блок с ожиданием появления кнопки"""

try:
    visible_button = driver.find_element(By.XPATH, '//button[@id="visibleAfter"]')
    visible_button.click()
except NoSuchElementException as exception:
    print('NoSuchElementException')
    time.sleep(10)
    visible_button = driver.find_element(By.XPATH, '//button[@id="visibleAfter"]')
    visible_button.click()
    print('Пользователь кликнул на кнопку')


time.sleep(3)
driver.close()



