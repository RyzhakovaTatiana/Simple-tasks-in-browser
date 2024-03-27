import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math


browser = webdriver.Chrome()
link = 'https://suninjuly.github.io/alert_accept.html'
browser.get(link)

#Locators 1
want_to_go_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')


#Actions

want_to_go_button.click()
confirm = browser._switch_to.alert
confirm.accept()


#Locators 2
num = browser.find_element(By.ID, 'input_value')
place = browser.find_element(By.ID, 'answer')
submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')

x=num.text
result = str(math.log(abs(12*math.sin(int(x)))))
place.send_keys(result)
submit_button.click()

time.sleep(10)