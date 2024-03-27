from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


g = Service('E:/PycharmProjects/pythonProject/python_selenium_m1/chromedriver.exe')

driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'


driver.get(base_url)
driver.maximize_window()

login_standard_user = 'standard_user2'
password_all = 'bad_pass'

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login_standard_user)
print('Input Login')
password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys(password_all)
print('Input Password')
button_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
button_login.click()
print('Click ')

warring_text = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
value_warring_text = warring_text.text
assert value_warring_text == 'Epic sadface: Username and password do not match any user in this service'
print('Test 1 PASS')


warring_password_text = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
value_warring_password_text = warring_password_text.text
assert value_warring_password_text == 'Epic sadface: Username and password do not match any user in this service'
print('Test 2 PASS')


driver.refresh()
time.sleep(3)
driver.close()

