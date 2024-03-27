import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()
link = 'https://suninjuly.github.io/explicit_wait2.html'
browser.get(link)


WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

book_button = browser.find_element(By.ID, 'book')
book_button.click()


submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')

browser.execute_script("arguments[0].scrollIntoView();", submit_button)
num = browser.find_element(By.ID, 'input_value')
place = browser.find_element(By.ID, 'answer')

x=num.text
result = str(math.log(abs(12*math.sin(int(x)))))

place.send_keys(result)
submit_button.click()

time.sleep(10)