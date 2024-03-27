import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
link = 'https://suninjuly.github.io/file_input.html'
browser.get(link)


#Locators

first_name_place = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter first name"]')
last_name_place = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter last name"]')
email_place = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter email"]')
load_button = browser.find_element(By.ID, 'file')
submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')

#Actions
first_name_place.send_keys('Ivan')
last_name_place.send_keys('Familia')
email_place.send_keys('tester@test.ru')


# получаем путь к директории текущего исполняемого скрипта
current_dir = os.path.abspath(os.path.dirname(__file__))

# имя файла, который будем загружать на сайт
file_name = '2_2_8_lesson.txt'

# получаем путь к file_example.txt
file_path = os.path.join(current_dir, file_name)


load_button.send_keys(file_path)
submit_button.click()
time.sleep(10)
