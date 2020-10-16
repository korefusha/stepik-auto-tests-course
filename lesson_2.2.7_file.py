from selenium import webdriver
import time
import os

try:   
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    
    first_name = browser.find_element_by_xpath("//div[@class='form-group']//input[@name='firstname' and @required]")
    first_name.send_keys("boris")
    last_name = browser.find_element_by_xpath("//div[@class='form-group']//input[@name='lastname' and @required]")
    last_name.send_keys("bulgakov")
    email = browser.find_element_by_xpath("//div[@class='form-group']//input[@name='email' and @required]")
    email.send_keys("boris@123.ru")
    #find fields and fill them
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    #create path to current directory
    file_path = os.path.join(current_dir, "123.txt")
    #add file name
    browser.find_element_by_id("file").send_keys(file_path)
    #load file to page
    
    browser.find_element_by_xpath("//button[@type='submit']").click()
    
    time.sleep(5)
   
finally:
    browser.quit()   