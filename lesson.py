from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

"""создаем экземпляр класса ChromeOptions и добавляем опцию "detach",
 чтобы браузер не закрывался после завершения сеанса тестирования."""
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

"""создаем экземпляр класса Service, 
который представляет собой фоновый процесс драйвера Chrome. 
Этот процесс будет работать в фоновом режиме и управлять браузером."""


g = Service('E:/PycharmProjects/pythonProject/resourse/chromedriver.exe')

"""создаем экземпляр класса WebDriver, 
который представляет собой драйвер для управления браузером. 
В параметре options мы передаем опции, которые мы создали в первых двух строках кода, 
а в параметре service мы передаем экземпляр класса Service."""
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'

"""вызываем метод get, чтобы открыть сайт"""
driver.get(base_url)
driver.maximize_window()


user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]')
password = driver.find_element(By.CSS_SELECTOR, "#password")
button_login = driver.find_element(By.XPATH, '//input[@value="Login"]')


user_name.send_keys("standard_user")
password.send_keys("secret_sauce")
button_login.click()


time.sleep(5)
driver.close()


