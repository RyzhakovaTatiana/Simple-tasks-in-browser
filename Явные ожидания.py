from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""Настройка драйвера"""
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
g = Service('E:/PycharmProjects/pythonProject/python_selenium_m1/chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/text-box'
driver.get(base_url)
#driver.maximize_window()


driver.execute_script("window.scrollTo(0, 30)")
new_url = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[9]')
new_url.click()
print('Пользователь перешел на страницу с тестированием кнопок')



"""Добавить блок с ожиданием появления кнопки"""


print('Старт тест')




visible_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="visibleAfter"]')))

visible_button.click()
print('Финиш тест')

driver.close()



