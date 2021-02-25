import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

address1 = 'Луначарского, 117'
address2 = 'Ленина, 103'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://yandex.ru/maps/geo/yekaterinburg/53166537/?ll=60.601571%2C56.788751&z=10.22')

search_field = WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[1]/div["
                                                                                        "2]/div[2]/div/div/div/"
                                                                                        "form/div[2]/div/span/span/"
                                                                                        "input")))

ActionChains(driver).click_and_hold(on_element=search_field).perform()
search_field.send_keys(address1)
search_field.send_keys(Keys.ENTER)

button_path = WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CLASS_NAME, "_type_route")))
button_path.click()

from_where_field = WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH,
                                                                                  "//input[@placeholder='Откуда']")))

from_where_field.click()
from_where_field.send_keys(address1)
from_where_field.send_keys(Keys.ENTER)

to_where_field = WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH,
                                                                                "//input[@placeholder='Куда']")))
to_where_field.click()

for i in range(0, 30):
    to_where_field.send_keys(Keys.BACKSPACE)
    to_where_field.send_keys(Keys.DELETE)

to_where_field.send_keys(address2)
to_where_field.send_keys(Keys.ENTER)
time.sleep(2)
info = driver.find_element_by_class_name('auto-route-snippet-view__route-subtitle').text

# Закрываем браузер
driver.close()

# Выводим на экран
print(f"От {address1} до {address2} = {info}")
all_distance.append(route_distance)
all_time.append(route_time)
