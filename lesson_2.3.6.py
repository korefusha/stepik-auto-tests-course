from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))
  # считаем функцию по этой формуле

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    #open browser
    browser.find_element_by_xpath("//button[@class='trollface btn btn-primary']").click()
    #click on button
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    #switch to open window
    #wait for loading page
    x = int(browser.find_element_by_xpath("//span[@id='input_value']").text)
    y = calc(x)
    #find x and calculate with formule
    browser.find_element_by_xpath("//*[@id='answer']").send_keys(y)
    browser.find_element_by_xpath("//button[@type='submit']").click()
    #fill in field and click on Submit button
    time.sleep(5)
    
    
finally:
    browser.quit()