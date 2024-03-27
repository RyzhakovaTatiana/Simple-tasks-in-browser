import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'
browser.get(link)

#Locators 1
button_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')

#Actions 1
time.sleep(5)
button_submit.click()
time.sleep(5)

"""""Переход в новую вкладку браузера"""
second_window = browser.window_handles[1]
browser.switch_to.window(second_window)


#Locators 2
num = browser.find_element(By.ID, 'input_value')
place = browser.find_element(By.ID, 'answer')
submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')

#Actions 2
x=num.text
result = str(math.log(abs(12*math.sin(int(x)))))

place.send_keys(result)
submit_button.click()
time.sleep(10)