from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.pepper.ru/')
# Находим нужное поле, выбираем, вставляем нужный результат и ищем
search_field = browser.find_element_by_xpath('/html/body/main/div[1]/header/div/div/div[3]/form/div/input')
search_field.click()
time.sleep(3)
search_field.send_keys('funko pop фигурка')
time.sleep(1)
search_field.send_keys(Keys.ENTER)

# Прокручиваем страницу до конца вниз
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Находим записи, в которых содержится нужная информация (по части имени класса)
records = browser.find_elements_by_class_name('cept-tt')
prices = browser.find_elements_by_class_name('cept-tp')

# Обрабатываем и сохраняем
all_records = []
all_prices = []
for record in records:
    title = str(record.get_attribute('title'))
    link = str(record.get_attribute('href'))
    record = f"{title}, {link}"
    all_records.append(record)
for _price in prices:
    price = _price.text
    all_prices.append(price)

# Закрываем браузер
time.sleep(3)
browser.close()

# Выводим результат на экран
for record, price in zip(all_records, all_prices):
    print(f"{record} : {price}")



