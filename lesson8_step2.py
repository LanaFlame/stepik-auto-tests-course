import math
import time
from selenium.webdriver.support.ui import Select
  
from selenium import webdriver

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id('num1')
    x = x.text
    x = int(x)
    y = browser.find_element_by_id('num2')
    y = y.text
    y = int(y)
    sum=x+y
    sum_text=str(sum)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum_text)
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
