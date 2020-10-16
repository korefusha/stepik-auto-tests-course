from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))
  # считаем функцию по этой формуле

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    #open browser
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
        )
    #wait while price become 100$
    browser.find_element_by_xpath("//button[@id='book']").click()
    #click Book button

    x = int(browser.find_element_by_xpath("//span[@id='input_value']").text)
    y = calc(x)
    #find x and calculate with formule
    browser.find_element_by_xpath("//*[@id='answer']").send_keys(y)
    browser.find_element_by_xpath("//button[@type='submit']").click()
    #fill in field and click on Submit button
    time.sleep(5)
    
    
finally:
    browser.quit()