
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By


"""Настройка драйвера"""
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
g = Service('E:/PycharmProjects/pythonProject/python_selenium_m1/chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

print('Проверка авторизации')
"""Логин и пароль"""
login_standard_user = 'standard_user'
password_all = 'secret_sauce'

"""Ввод логина и пароля"""
user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login_standard_user)
print('\tВведен логин')
password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys(password_all)
print('\tВведен пароль')


"""Нажать на кнопку ввода"""
button_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
button_login.click()
print('Пользователь авторизован')
print('--------')


"""Список товаров"""

class Goods():
    def __init__(self, number, name, price, buy_button):

        self.number = number
        self.name = name
        self.price = price
        self.buy_button = buy_button

    def add_to_cart(self):
        self.buy_button.click()



"""Информация по первому товару"""
product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]/div')
catalog_name_product_1 = product_1.text
#print('\tНазвание первого товара :', catalog_name_product_1)
price_product_1 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
catalog_price_product_1 = price_product_1.text
#print('\tСтоимость первого товара :', catalog_price_product_1)
add_product1 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')


"""Информация по второму товару"""
product_2 = driver.find_element(By.XPATH, '//a[@id="item_0_title_link"]/div')
catalog_name_product_2 = product_2.text
#print('\tНазвание второго товара :', catalog_name_product_2)
price_product_2 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div')
catalog_price_product_2 = price_product_2.text
#print('\tСтоимость второго товара :', catalog_price_product_2)
add_product2 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bike-light"]')

"""Информация по третьему товару"""
product_3 = driver.find_element(By.XPATH, '//a[@id="item_1_title_link"]/div')
catalog_name_product_3 = product_3.text
#print('\tНазвание 3 товара :', catalog_name_product_3)
price_product_3 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div')
catalog_price_product_3 = price_product_3.text
#print('\tСтоимость 3 товара :', catalog_price_product_3)
add_product3 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')

"""Информация по четвертому товару"""
product_4 = driver.find_element(By.XPATH, '//a[@id="item_5_title_link"]/div')
catalog_name_product_4 = product_4.text
#print('\tНазвание 4 товара :', catalog_name_product_4)
price_product_4 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div')
catalog_price_product_4 = price_product_4.text
#print('\tСтоимость 4 товара :', catalog_price_product_4)
add_product4 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-fleece-jacket"]')


"""Информация по пятому товару"""
product_5 = driver.find_element(By.XPATH, '//a[@id="item_2_title_link"]/div')
catalog_name_product_5 = product_5.text
#print('\tНазвание 5 товара :', catalog_name_product_5)
price_product_5 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[5]/div[2]/div[2]/div')
catalog_price_product_5 = price_product_5.text
#print('\tСтоимость 5 товара :', catalog_price_product_5)
add_product5 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-onesie"]')

"""Информация по шестому товару"""
product_6 = driver.find_element(By.XPATH, '//a[@id="item_3_title_link"]/div')
catalog_name_product_6 = product_6.text
#print('\tНазвание 6 товара :', catalog_name_product_6)
price_product_6 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[6]/div[2]/div[2]/div')
catalog_price_product_6 = price_product_6.text
#print('\tСтоимость 6 товара :', catalog_price_product_6)
add_product6 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')


"""Инфо для пользователя"""

print("Приветствую тебя в нашем интернет - магазине")
print("Выбери один из следующих товаров и укажи его номер: "
      "1 - Sauce_Labs_Backpack",
      "2 - Sauce_Labs_Bike_Light",
      "3 - Sauce_Labs_Bolt_T_Shirt",
      "4 - Sauce_Labs_Fleece_Jacket",
      "5 - Sauce_Labs_Onesie",
      "6 - Test_allTheThings_T_Shirt_Red",
      )
client_number = input("Введите номер товара в этой строке: ")




"""Выбор товаров"""

Sauce_Labs_Backpack = Goods(1, catalog_name_product_1, catalog_price_product_1, add_product1)
Sauce_Labs_Bike_Light = Goods(2, catalog_name_product_2, catalog_price_product_2, add_product2)
Sauce_Labs_Bolt_T_Shirt = Goods(3, catalog_name_product_3, catalog_price_product_3, add_product3)
Sauce_Labs_Fleece_Jacket = Goods(4, catalog_name_product_4, catalog_price_product_4, add_product4)
Sauce_Labs_Onesie = Goods(5, catalog_name_product_5, catalog_price_product_5, add_product5)
Test_allTheThings_T_Shirt_Red = Goods(6, catalog_name_product_6, catalog_price_product_6, add_product6)

all_goods = [Sauce_Labs_Backpack, Sauce_Labs_Bike_Light, Sauce_Labs_Bolt_T_Shirt, Sauce_Labs_Fleece_Jacket,
             Sauce_Labs_Onesie, Test_allTheThings_T_Shirt_Red]

for i in all_goods:
    if int(client_number) == int(i.number):
        print(f"Вы выбрали товар {i.name} стоимостью {i.price}")
        first_purchase = i
        first_purchase.add_to_cart()
        break


user_answer = input("Хотите выбрать еще один товар (один товар можно выбрать только один раз)? Напишите 'да' или 'нет' в этой строке: ").lower()
if user_answer == 'да':
    client_number2 = input("Введите номер товара в этой строке: ")
    for i in all_goods:
        if int(client_number2) == int(i.number):
            print(f"Вы выбрали товар {i.name} стоимостью {i.price}")
            second_purchase = i
            second_purchase.add_to_cart()
            break

elif user_answer == 'нет':
    print('Хорошо, тогда давайте преступим к оформлению заказа на один выбранный Вами товар')


"""Открыть корзину"""
cart = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
cart.click()
print('Открылась страница корзины')

print('--------')
print('Проверка названий и цен товаров в корзине')

quantity_goods = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
quantity = int(quantity_goods.text)

if quantity == 1:
    """Убедиться, что в корзину правильно добавлены товары"""
    cart_purchase_1 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/a/div')
    cart_name_purchase_1 = cart_purchase_1.text
    print('\tНазвание первого товара в корзине:', cart_name_purchase_1)

    assert cart_name_purchase_1 == first_purchase.name
    print('\tТЕСТ №1 - Название первого товара в корзине - ОК')

    cart_price_purchase_1 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/div')
    value_cart_price_purchase_1 = cart_price_purchase_1.text
    print('\tСтоимость первого товара в корзине: ', value_cart_price_purchase_1)
    assert value_cart_price_purchase_1 == first_purchase.price
    print('\tТЕСТ №2 - Стоимость первого товара в корзине - ОК')


if quantity == 2:
    """Убедиться, что в корзину правильно добавлены товары"""
    cart_purchase_1 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/a/div')
    cart_name_purchase_1 = cart_purchase_1.text
    print('\tНазвание первого товара в корзине:', cart_name_purchase_1)
    assert cart_name_purchase_1 == first_purchase.name
    print('\tТЕСТ №1 - Название первого товара в корзине - ОК')

    cart_price_purchase_1 = driver.find_element(By.XPATH,
                                                '/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/div')
    value_cart_price_purchase_1 = cart_price_purchase_1.text
    print('\tСтоимость первого товара в корзине: ', value_cart_price_purchase_1)
    assert value_cart_price_purchase_1 == first_purchase.price
    print('\tТЕСТ №2 - Стоимость первого товара в корзине - ОК')


    cart_purchase_2 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[1]/div[4]/div[2]/a/div')
    cart_name_purchase_2 = cart_purchase_2.text
    print('\tНазвание второго товара в корзине:', cart_name_purchase_2)
    assert cart_name_purchase_2 == second_purchase.name
    print('\tТЕСТ №3 - Название второго товара в корзине - ОК')

    cart_price_purchase_2 = driver.find_element(By.XPATH,
                                                '/html/body/div/div/div/div[2]/div/div[1]/div[4]/div[2]/div[2]/div')
    value_cart_price_purchase_2 = cart_price_purchase_2.text
    print('\tСтоимость второго товара в корзине: ', value_cart_price_purchase_2)
    assert value_cart_price_purchase_1 == first_purchase.price
    print('\tТЕСТ №4 - Стоимость второго товара в корзине - ОК')



print('--------')
print('Оформление заказа')

checkout_button = driver.find_element(By.XPATH, '//button[@id="checkout"]')
checkout_button.click()
print('\tПереход к заполнению информации о покупателе')
first_name = driver.find_element(By.XPATH, '//input[@id="first-name"]')
first_name.send_keys('Покупатель')
print('\tВведено имя покупателя')
last_name = driver.find_element(By.XPATH, '//input[@id="last-name"]')
last_name.send_keys('Тестов')
print('\tВведена фамилия покупателя')
field_zip = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
field_zip.send_keys('109364')
print('\tВведен почтовый код')

continue_button = driver.find_element(By.XPATH, '//input[@id="continue"]')
continue_button.click()
print('Продолжено оформление заказа')

print('--------')
print('Проверка названий товаров и цен в заказе:')
if quantity == 1:
    purchased_product_1 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/a/div')
    name_purchased_product_1 = purchased_product_1.text
    assert name_purchased_product_1 == first_purchase.name
    print('\tНазвание первого товара в заказе:', name_purchased_product_1)
    print('\tТЕСТ №3 -  Название первого товара в заказе - ОК')

    price_purchased_product_1 = driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/div')
    value_price_purchased_product_1 = price_purchased_product_1.text
    print('\tСтоимость первого товара в заказе:', value_price_purchased_product_1)
    assert value_price_purchased_product_1 == first_purchase.price
    print('\tТЕСТ №4 -  Стоимость первого товара в заказе - ОК')

    print('--------')
    print('Проверка общей суммы в заказе:')

    cost_product_1 = float(value_price_purchased_product_1[1:])
    products_cost = cost_product_1
    print('\tСтоимость товаров: ', products_cost)

    value_products_price = driver.find_element(By.XPATH, '//div[@class="summary_subtotal_label"]')
    text_products_price = value_products_price.text
    sum_products_price = float(text_products_price[13:])
    print('\tСтоимость товаров, указанная в заказе: ', sum_products_price)
    assert products_cost == sum_products_price
    print('\tТЕСТ №5 -  Стоимость за товар - ОК')

    print('--------')
    print('Проверка общей суммы с учетом налога:')

    tax = driver.find_element(By.XPATH, '//div[@class="summary_tax_label"]')
    text_tax = tax.text
    tax_price = float(text_tax[6:])
    print('\tНалог: ', tax_price)

    total = driver.find_element(By.XPATH, '//div[@class="summary_info_label summary_total_label"]')
    total_text = total.text
    total_price = float(total_text[8:])
    print('\tСумма заказа: ', total_price)

    total_sum = products_cost + tax_price
    print('\tОбщая сумма товаров с учетом налога в заказе: ', total_sum)
    assert total_sum == total_price
    print('\tТЕСТ №6 -  Общая сумма заказа - ОК')




if quantity == 2:
    purchased_product_1 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/a/div')
    name_purchased_product_1 = purchased_product_1.text
    assert name_purchased_product_1 == first_purchase.name
    print('\tНазвание первого товара в заказе:', name_purchased_product_1)
    print('\tТЕСТ №5 -  Название первого товара в заказе - ОК')

    price_purchased_product_1 = driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/div')
    value_price_purchased_product_1 = price_purchased_product_1.text
    print('\tСтоимость первого товара в заказе:', value_price_purchased_product_1)
    assert value_price_purchased_product_1 == first_purchase.price
    print('\tТЕСТ №6 -  Стоимость первого товара в заказе - ОК')


    purchased_product_2 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[1]/div[4]/div[2]/a/div')
    name_purchased_product_2 = purchased_product_2.text
    assert name_purchased_product_2 == second_purchase.name
    print('\tНазвание второго товара в заказе:', name_purchased_product_2)
    print('\tТЕСТ №7 -  Название второго товара в заказе - ОК')

    price_purchased_product_2 = driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div/div[2]/div/div[1]/div[4]/div[2]/div[2]/div')
    value_price_purchased_product_2 = price_purchased_product_2.text
    print('\tСтоимость второго товара в заказе:', value_price_purchased_product_2)
    assert value_price_purchased_product_2 == second_purchase.price
    print('\tТЕСТ №8 -  Стоимость второго товара в заказе - ОК')

    print('--------')
    print('Проверка общей суммы в заказе:')

    cost_product_1 = float(value_price_purchased_product_1[1:])
    cost_product_2 = float(value_price_purchased_product_2[1:])
    products_cost = cost_product_1 + cost_product_2
    print('\tСтоимость двух товаров: ', products_cost)

    value_products_price = driver.find_element(By.XPATH, '//div[@class="summary_subtotal_label"]')
    text_products_price = value_products_price.text
    sum_products_price = float(text_products_price[13:])
    print('\tСтоимость двух товаров, указанная в заказе: ', sum_products_price)
    assert products_cost == sum_products_price
    print('\tТЕСТ №9 -  Стоимость за два товара - ОК')

    print('--------')
    print('Проверка общей суммы с учетом налога:')

    tax = driver.find_element(By.XPATH, '//div[@class="summary_tax_label"]')
    text_tax = tax.text
    tax_price = float(text_tax[6:])
    print('\tНалог: ', tax_price)

    total = driver.find_element(By.XPATH, '//div[@class="summary_info_label summary_total_label"]')
    total_text = total.text
    total_price = float(total_text[8:])
    print('\tСумма заказа: ', total_price)

    total_sum = products_cost + tax_price
    print('\tОбщая сумма товаров с учетом налога в заказе: ', total_sum)
    assert total_sum == total_price
    print('\tТЕСТ №10 -  Общая сумма заказа - ОК')

time.sleep(3)
driver.close()