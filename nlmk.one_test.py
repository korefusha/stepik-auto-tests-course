from selenium import webdriver
import time 
import math

driver = webdriver.Chrome

try:
    browser = webdriver.Chrome()
    browser.get("https://nlmk.one")
    driver.implicitly_wait(10) # seconds
    login = browser.find_element_by_xpath("//*[@id='login']")
    login.send_keys("bulgakov_bv")
    password = browser.find_element_by_xpath("//*[@id='password']")
    password.send_keys("K75079o@#4")
    button = browser.find_element_by_xpath("//*[@id='bind']")
    #ищем по всему документу html элемент с id='bind'
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
