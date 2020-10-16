from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/cats.html")
    #open browser
    browser.find_element_by_id("button")
    #find element by id
    time.sleep(5)
    
    
finally:
    browser.quit()
    #close browser window