from datetime import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
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


"""Проскроллить экран на 20 пикселей вниз и сделать скриншот"""
driver.execute_script("window.scrollTo(0, 20)")
time.sleep(3)
now_date = datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
name_screenshot = 'screenshot' + now_date + '.png'
driver.save_screenshot('E:\\PycharmProjects\\pythonProject\\python_selenium_m1\\screen\\' + name_screenshot)

"""Наведение на элемент / Убедиться, что элемент есть на странице"""
#Показываем драйверу, что действия будут производиться именно с этим браузером
action = ActionChains(driver)
red_t_shirt = driver.find_element(By.XPATH, '//button[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
action.move_to_element(red_t_shirt).perform()#Проскроллить экран до этого элемента
time.sleep(3)
now_date = datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
name_screenshot2 = 'red_t_shirt' + now_date + '.png'
driver.save_screenshot('E:\\PycharmProjects\\pythonProject\\python_selenium_m1\\screen\\' + name_screenshot2)





time.sleep(3)
driver.close()

