import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)

#Locators
button = browser.find_element(By.TAG_NAME, "button")
elem_x = browser.find_element(By.ID, 'input_value')
place = browser.find_element(By.ID, 'answer')
check_robot = browser.find_element(By.ID, 'robotCheckbox')

button_submit = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')


#Actions

x = int(elem_x.text)
#print(type(x))
result = str(math.log(abs(12*math.sin(int(x)))))
#print(result)

place.send_keys(result)
check_robot.click()

radio_robot_rule = browser.find_element(By.ID, 'robotsRule')


browser.execute_script("return arguments[0].scrollIntoView(true);", radio_robot_rule)

radio_robot_rule.click()

button_submit.click()

time.sleep(10)