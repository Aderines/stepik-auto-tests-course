import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# код ниже для урока с явным ожиданием
link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    button = browser.find_element_by_id("book")
    # ожидаем в явном виде изменение цены до 100$
    WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()

    # с помощью math считаем функцию по значению, которое передается в тексте страницы (генерируется рандомно каждый
    # раз)
    x = browser.find_element_by_id('input_value').text
    answer = math.log(abs(12 * math.sin(int(x))))
    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(str(answer))
    button = browser.find_element_by_id("solve")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
