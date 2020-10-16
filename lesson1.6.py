from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # открыли страницу
    first_name = browser.find_element_by_xpath("//div[@class='first_block']//input[contains(@class, 'first')]")
    first_name.send_keys("Boris")
    last_name = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control second']")
    last_name.send_keys("Razor")
    email = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control third']")
    email.send_keys("123@ya.ru")
    # заполнили поля формы
    submit = browser.find_element_by_xpath("//button[@type='submit']")
    submit.click()
    # нажали кнопку Submit 
    time.sleep(1)
    welcome_text_raw = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_raw.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    
    
finally:
    time.sleep(5)
    browser.quit()