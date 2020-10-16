from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
    # считаем функцию по этой формуле

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
	# открыли страницу браузера
	
    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text
	# нашли элемент по id и записали текстовое значение в переменную x
    y = calc(x)
	# высчитали значение y с помощью функции
    
    input_field = browser.find_element_by_xpath("//input[@id='answer' and @required]")
    input_field.send_keys(y)
    
    checkbox = browser.find_element_by_xpath("//input[@id='robotCheckbox' and @required]")
    checkbox.click()
    # нашли чекбокс и поставили галочку
    radio = browser.find_element_by_xpath("//input[@id='robotsRule' and @value='robots']")
    radio.click()
    # нашли чекбокс и поставили галочку
    time.sleep(8)
    submit = browser.find_element_by_xpath("//button[@class='btn btn-default']")
    submit.click()
    # нажали кнопку Submit
    time.sleep(8)
    
finally:
    browser.quit()