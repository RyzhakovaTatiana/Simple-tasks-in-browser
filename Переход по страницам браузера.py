from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

"""Настройка драйвера"""

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


g = Service('E:/PycharmProjects/pythonProject/python_selenium_m1/chromedriver.exe')

driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

"""Логин и пароль"""
login_standard_user = 'standard_user'
password_all = 'secret_sauce'

"""Ввод логина и пароля"""
user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login_standard_user)
print('Input Login')


password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys(password_all)
print('Input Password')

"""Нажать на кнопку ввода"""
button_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
button_login.click()
print('Click ')


menu = driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
menu.click()
time.sleep(2)
link_about = driver.find_element(By.XPATH, '//a[@id="about_sidebar_link"]')
link_about.click()
print('Click link_about OK')

"""Вернуться на предыдущую страницу браузера"""
driver.back()
print('Go Back')

"""Перейти на следующую страницу браузера"""
driver.forward()
print('Go forward')

time.sleep(5)
driver.close()



