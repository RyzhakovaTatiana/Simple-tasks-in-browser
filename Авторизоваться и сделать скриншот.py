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

"""Проверка наличия элемента после авторизации"""
text_products = driver.find_element(By.XPATH, '//span[@class="title"]')
value_text_products = text_products.text
print(value_text_products)
assert value_text_products == "Products"
print('Test 1 OK')

"""Проверка ссылки после авторизации"""
url = 'https://www.saucedemo.com/inventory.html'
get_url = driver.current_url
print(get_url)
assert url == get_url
print("Test 2 OK")
time.sleep(3)


"""Сделать скриншот"""
now_date = datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
name_screenshot = 'screenshot' + now_date + '.png'
driver.save_screenshot('E:\\PycharmProjects\\pythonProject\\python_selenium_m1\\screen\\' + name_screenshot)
time.sleep(3)
driver.close()



