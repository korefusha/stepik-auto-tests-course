from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    first_name = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control first' and @required]")
    first_name.send_keys("Boris")
    # находим поле First name по XPath и заполняем его
    last_name = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control second' and @required]")
    last_name.send_keys("Razor")
    # находим поле Last name по XPath и заполняем его
    email = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control third' and @required]")
    email.send_keys("123@ya.ru")
    # находим поле Email по XPath и заполняем его
    
    submit = browser.find_element_by_xpath("//button[@type='submit']")
    submit.click()
    # находим кнопку Submit и нажимаем на него
    
    time.sleep(1)
    welcome_text_raw = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_raw
    welcome_text = welcome_text_raw.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    
    
finally:
    time.sleep(5)
    browser.quit()