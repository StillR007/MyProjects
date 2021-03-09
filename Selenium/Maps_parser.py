import openpyxl
import datetime
import time
from itertools import permutations, combinations

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementNotVisibleException

all_addresses = []
all_info = []
addresses = []


def write_book():
    book = openpyxl.Workbook()
    sheet = book.active
    pair_addresses = [all_addresses[i:i + 2] for i in range(0, len(all_addresses), 2)]
    date_name = str(datetime.datetime.today().strftime("%Y.%m.%d--%H`%M`%S"))
    sheet['A1'] = 'Пункт 1'
    sheet['B1'] = 'Пункт 2'
    sheet['C1'] = 'инфо'
    for i in range(2, len(pair_addresses)+2):
        sheet['A'+str(i)] = pair_addresses[i - 2][0]
        sheet['B'+str(i)] = pair_addresses[i - 2][1]
        sheet['C'+str(i)] = all_info[i - 2]
    sheet.column_dimensions['A'].width = 20
    sheet.column_dimensions['B'].width = 20
    sheet.column_dimensions['C'].width = 35
    book.save(f"{date_name}.xlsx")
    book.close()
    print("*" * 5, f' Файл {date_name}.xlsx создан ', "*" * 5)


def clear_the_field(field):
    # Очищаем поле ввода (топорно, конечно, но относительно похоже на человека)
    for i in range(50):
        field.send_keys(Keys.BACKSPACE)
        field.send_keys(Keys.DELETE)


def find_reverse_path():
    reverse_button = driver.find_element_by_class_name("route-form-view__reverse")
    ActionChains(driver).click_and_hold(on_element=reverse_button).perform()
    reverse_button.click()
    time.sleep(2)
    info2 = driver.find_element_by_class_name('auto-route-snippet-view__route-subtitle').text
    return info2


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
    info1 = driver.find_element_by_class_name('auto-route-snippet-view__route-subtitle').text

    info2 = find_reverse_path()

    driver.back()
    return info1, info2


def main():
    while True:
        address = input('Введите адрес. Чтобы остановить, введите <стоп>')
        if address.lower() == 'стоп' or (address.lower() == 'cnjg'):
            break
        addresses.append(address)

    # Список всех маршрутов
    paths = permutations(addresses, len(addresses))
    # Все комбинации маршрутов
    pairs = combinations(addresses, 2)
    global driver
    while True:
        try:

            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get('https://yandex.ru/maps/geo/yekaterinburg/53166537/?ll=60.597383%2C56.837712&z=19.21')
            for pair in pairs:
                wait = WebDriverWait(driver, 50, poll_frequency=1, ignored_exceptions=(ElementNotVisibleException,
                                                                                       TimeoutError))
                info1, info2 = input_addresses(pair, wait)
                all_info.append(str(info1))
                all_info.append(str(info2))
                all_addresses.append(str(pair[0]))
                all_addresses.append(str(pair[1]))
                all_addresses.append(str(pair[1]))
                all_addresses.append(str(pair[0]))
                print(f"От {pair[0]} до {pair[1]} = {info1}")
                print(f"От {pair[1]} до {pair[0]} = {info2}")
        except Exception:
            print("Не удалось подключиться к Яндекс.Картам")
        finally:
            driver.close()
            driver.quit()
            break
    write_book()


if __name__ == '__main__':
    main()
