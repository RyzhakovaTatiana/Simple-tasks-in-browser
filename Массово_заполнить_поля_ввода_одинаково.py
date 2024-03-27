from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import math

link = "http://suninjuly.github.io/huge_form.html"
number = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:

    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    g = Service('E:\\PycharmProjects\\pythonProject\\resourse\\chromedriver.exe')
    browser = webdriver.Chrome(options=options, service=g)
    browser.get(link)

    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()