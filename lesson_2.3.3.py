from selenium import webdriver
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  # считаем функцию по этой формуле
try:   
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    # открыли страницу  
    browser.find_element_by_xpath("//button[@type='submit']").click()
    # нажали кнопку "Submit"
    alert = browser.switch_to.alert
    alert.accept()
    # переключились на всплывающее окно и нажали ОК
    x_str = browser.find_element_by_xpath("//span[@id='input_value']").text
    x = int(x_str)
    # получили значение Х и преобразовали его в число
    y = calc(x)
    browser.find_element_by_xpath("//input[@id='answer']").send_keys(y)
    browser.find_element_by_xpath("//button[@type='submit']").click()
    # вычислили по формуле, записали результат в поле Ответ и нажали кнопку Submit
    time.sleep(5)
   
finally:
    browser.quit()   