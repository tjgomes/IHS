# import time
from selenium import webdriver

driver = webdriver.Chrome('c:/selenium/chromedriver')  # please specify the path.
driver.get('https://dotnetfiddle.net/');
driver.implicitly_wait(5);
driver.find_element_by_id('run-button').click(); 
element = driver.find_element_by_id('output')
assert element.text == 'Hello World'

driver.quit()