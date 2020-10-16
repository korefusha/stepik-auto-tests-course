from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/selects1.html"
    browser.get(link)
    # open link in browser
    
    first_num_str = browser.find_element_by_xpath("//span[@id='num1']").text
    
    second_num_str = browser.find_element_by_xpath("//span[@id='num2']").text
    # found two numbers and get text value from them
    
    first_num = int(first_num_str)
    second_num = int(second_num_str)
    #convert strings to integer type to sum them
    
    sum_result = first_num + second_num
    #count sum of two numbers
    sum_str = str(sum_result)
    # convert to string to compare with value in next step
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum_str)
    
    browser.find_element_by_xpath("//button[@type='submit']").click()
    
finally:
    time.sleep(8)
    browser.quit()
    # close browser
    