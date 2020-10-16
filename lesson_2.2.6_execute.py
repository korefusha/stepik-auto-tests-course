from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  # считаем функцию по этой формуле

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
	# открыли страницу браузера
	
    get_x = browser.find_element_by_xpath("//span[@id='input_value']").text
    x = int(get_x)
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
    browser.execute_script("return arguments[0].scrollIntoView(true);" , radio)
    radio.click()
    # нашли чекбокс и поставили галочку
    
    submit = browser.find_element_by_xpath("//button[@class='btn btn-primary']")
    browser.execute_script("return arguments[0].scrollIntoView(true);" , submit)
    submit.click()
    # с помощью скрипта прокрутили страницу вниз, пока кнопка Submit не станет видимойы
    time.sleep(8)
    
finally:
    browser.quit()