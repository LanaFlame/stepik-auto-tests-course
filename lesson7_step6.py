import math
import time

#Definition for calc(x)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
from selenium import webdriver

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_image = browser.find_element_by_id('treasure')
    x_element=x_image.get_attribute('valuex')
    x = x_element
    y = calc(x)
    
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    
    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click()
    
    option1 = browser.find_element_by_id('robotsRule')
    option1.click()
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
