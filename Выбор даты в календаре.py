import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
import time


from selenium.webdriver.common.by import By



"""Настройка драйвера"""
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
g = Service('E:/PycharmProjects/pythonProject/resourse/chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()




"""Найти сегодняшнюю дату и дату через 10 дней"""
future_date = str(datetime.datetime.today() + datetime.timedelta(days=10))
print("Текущая дата:", datetime.datetime.today())
print("Через 10 дней будет дата:", future_date)

inp_date = future_date[0:10]
print(inp_date)

"""Стереть старую дату на сайте"""

date_field = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
date_field.click()
date_field.send_keys(Keys.CONTROL+'a')#Выбрать всю строку (Ctrl+a)
date_field.send_keys(Keys.BACKSPACE)#Очистить строку

"""Ввод даты на сайте"""
date_field.send_keys(inp_date)
time.sleep(5)
date_field.send_keys(Keys.RETURN)


time.sleep(5)
print('Дата в календаре выбрана')
driver.close()



