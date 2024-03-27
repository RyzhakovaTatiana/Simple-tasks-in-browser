from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By



"""Настройка драйвера"""
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
g = Service('E:/PycharmProjects/pythonProject/python_selenium_m1/chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.maximize_window()

yes_radio_button = driver.find_element(By.XPATH, '//label[@for="yesRadio"]')
yes_radio_button.click()

try:
    message = driver.find_element(By.XPATH, '//span[@class="text-success"]')
    value_message = message.text
    print(value_message)
    assert value_message == 'No'
except AssertionError as exception:
    driver.refresh()
    yes_radio_button = driver.find_element(By.XPATH, '//label[@for="yesRadio"]')
    yes_radio_button.click()
    message = driver.find_element(By.XPATH, '//span[@class="text-success"]')
    value_message = message.text
    print(value_message)
    assert value_message == 'Yes'
    print('Выбран радиобаттон Yes')
print('Тест прошел успешно')


time.sleep(3)
driver.close()



