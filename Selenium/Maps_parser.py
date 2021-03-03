from bs4 import BeautifulSoup
import requests

import time
from itertools import permutations, combinations

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


all_distance = []
all_time = []
addresses = []


def find_proxy():
    url = "http://foxtools.ru/Proxy"
    ips = get_proxy_ip(url)
    proxy = check_proxy(ips)
    capabilities = webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": proxy,
        "ftpProxy": proxy,
        "sslProxy": proxy,
        "noProxy": None,
        "proxyType": "MANUAL",
        "class": "org.openqa.selenium.Proxy",
        "autodetect": False
    }
    return capabilities


def get_proxy_ip(url):
    page = requests.get(url=url)
    html = page.content
    soup = BeautifulSoup(html, 'lxml')
    # Выделяем нужное значение
    ip_list = soup.find_all("input", class_="ch")
    for i in range(0, len(ip_list)):
        ip_list[i] = ip_list[i]['value']
    return ip_list


def check_proxy(ips):
    for ip in ips:
        with webdriver.Chrome() as driver:
            driver.get("https://google.com/ncr")
            driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
            result = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "h3>div")))
            if result:
                return ip


def clear_the_field(field):
    # Очищаем поле ввода (очень топорно пока что, но относительно похоже на человека)
    for i in range(30):
        field.send_keys(Keys.BACKSPACE)
        field.send_keys(Keys.DELETE)


def input_addresses(address, wait):
    xpath_search_field = "/html/body/div[1]/div[2]/div[2]/div/div/div/form/div[2]/div/span/span/input"
    search_field = wait.until(ec.presence_of_element_located((By.XPATH, xpath_search_field)))
    clear_the_field(search_field)
    ActionChains(driver).click_and_hold(on_element=search_field).perform()
    search_field.send_keys(address[0])
    search_field.send_keys(Keys.ENTER)
    button_path = wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "_type_route")))
    button_path.click()
    from_where_field = wait.until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Откуда']")))
    from_where_field.click()
    from_where_field.send_keys(address[0])
    from_where_field.send_keys(Keys.ENTER)

    to_where_field = wait.until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Куда']")))
    to_where_field.click()

    clear_the_field(to_where_field)

    to_where_field.send_keys(address[1])
    to_where_field.send_keys(Keys.ENTER)

    time.sleep(2)
    info = driver.find_element_by_class_name('auto-route-snippet-view__route-subtitle').text
    print(f"От {address[1]} до {address[0]} = {info}")

    # Обратный путь
    reverse_button = driver.find_element_by_class_name("route-form-view__reverse")
    ActionChains(driver).click_and_hold(on_element=reverse_button).perform()
    reverse_button.click()

    time.sleep(2)
    info2 = driver.find_element_by_class_name('auto-route-snippet-view__route-subtitle').text
    print(f"От {address[1]} до {address[0]} = {info2}")
    driver.back()
    return info, info2


if __name__ == '__main__':
    while True:
        address = input('Введите адрес. Чтобы остановить, введите <стоп>')
        if address.lower() == 'стоп' or (address.lower() == 'cnjg'):
            break
        addresses.append(address)

    capabilities = find_proxy()

    driver = webdriver.Chrome(desired_capabilities=capabilities)
    driver.maximize_window()
    driver.get('https://yandex.ru/maps/geo/yekaterinburg/53166537/?ll=60.601571%2C56.788751&z=10.22')

    wait = WebDriverWait(driver, 40)

    # Список всех маршрутов
    paths = permutations(addresses, len(addresses))
    # Все комбинации маршрутов
    pairs = combinations(addresses, 2)

    for pair in pairs:
        input_addresses(pair, wait)

    driver.close()
