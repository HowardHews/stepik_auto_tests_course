from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

'''
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
2. Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
3. Нажать на кнопку "Book"
4. Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
'''

brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
link = "https://suninjuly.github.io/explicit_wait2.html"

option = webdriver.ChromeOptions()
option.binary_location = brave_path
driver = webdriver.Chrome(options=option)
driver.get(link)

try:
    button = driver.find_element(By.ID, 'book')
    price = WebDriverWait(driver, 12).until((EC.text_to_be_present_in_element((By.ID, 'price'), '$100')))
    button.click()

    x = int(driver.find_element(By.ID, 'input_value').text)
    expr = str(math.log(abs(12 * math.sin(x))))
    driver.find_element(By.ID, 'answer').send_keys(expr)
    driver.find_element(By.ID, 'solve').click()

    alert_text = driver.switch_to.alert.text.split(": ")[-1]
    print(alert_text)

finally:
    time.sleep(5)
    driver.quit()
