from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  # считаем функцию по этой формуле

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
	# открыли страницу браузера
	
    treasure_x = browser.find_element_by_xpath("//img[@id='treasure']")
    x = treasure_x.get_attribute("valuex")
	# нашли картинку по id и записали текстовое значение атрибута valuex в переменную x
    y = calc(x)
	# высчитали значение y с помощью функции
    
    input_field = browser.find_element_by_xpath("//input[@id='answer' and @required]")
    input_field.send_keys(y)
    # в поле ввели результат вычисления по формуле
    checkbox = browser.find_element_by_xpath("//input[@id='robotCheckbox' and @required]")
    checkbox.click()
    # нашли чекбокс и поставили галочку
    radio = browser.find_element_by_xpath("//input[@id='robotsRule' and @value='robots']")
    radio.click()
    # нашли чекбокс и поставили галочку
    submit = browser.find_element_by_xpath("//button[@class='btn btn-default']")
    submit.click()
    
    time.sleep(8)
    
finally:
    browser.quit()