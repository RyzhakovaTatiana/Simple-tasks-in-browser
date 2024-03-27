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
base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
driver.get(base_url)
driver.maximize_window()

time.sleep(3)

action = ActionChains(driver)
my_element = driver.find_element(By.CSS_SELECTOR, 'id="id1"')
action.click_and_hold(my_element).move_by_offset(20, 0).release().perform()
# release() - отпустить мышь
# perform() - сохранить результат

time.sleep(3)
print('OK')

driver.close()



