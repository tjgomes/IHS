import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

nameIndex = None ;
first_name = 'Pack'; 

names_AE = ('A', 'B', 'C', 'D', 'E');
names_FK = ('F', 'G', 'H', 'I', 'J', 'K');
names_LP = ('L', 'M', 'N', 'O', 'P');
names_QU = ('Q', 'R', 'S', 'T', 'U');
names_VZ = ('V', 'W', 'X', 'Y', 'Z');
all_names = {names_AE:0, names_FK:1, names_LP:2, names_QU:3, names_VZ:4};

for listItem in all_names:
    if(first_name.upper().startswith(tuple(listItem),0)):
        nameIndex = all_names[listItem];

print("index is " + str(nameIndex));

driver = webdriver.Chrome('c:/selenium/chromedriver')  # please specify the path.
driver.get('https://dotnetfiddle.net/');
driver.implicitly_wait(5);


if(nameIndex == 0):  # Test2a select Packages: nUnit (3.12.0)
    search_field = driver.find_element_by_css_selector("input[type='search']")
    search_field.clear()
    search_field.send_keys("nUnit (3.12.0)")
    result = driver.find_element_by_id('ui-id-1')
    assert result.text == 'Superwalnut.NetCoreApiTemplate'

if (nameIndex == 1): # Test2b Click “Share” button
    share_element = driver.find_element_by_id('Share')
    share_element.click();
    share_link = driver.find_element_by_id('ShareLink')
    assert share_link.get_attribute('baseURI')== 'https://dotnetfiddle.net/';

if (nameIndex == 2): # Test2c Click “<” button on “Options” panel
    left_arrow = driver.find_element_by_css_selector(".btn-sidebar-toggle[type='button']");
    option_panel = driver.find_element_by_class_name('text-center');
    left_arrow.click();
    driver.implicitly_wait(2);
    assert option_panel.is_displayed() == False;

if (nameIndex == 3): # Test2d Click “Save” button
    save_button = driver.find_element_by_id('save-button');
    login_modal = driver.find_element_by_id('login-modal-label');
    save_button.click();
    assert login_modal.get_attribute('innerHTML') == 'Log in';

if (nameIndex == 4): # Test2e Click “Getting Started” button
    getting_started_button = driver.find_element_by_xpath('//a[contains(@href,"GettingStarted")]');
    getting_started_button.click();
    driver.implicitly_wait(4);
    back_to_editor_btn = driver.find_element_by_xpath('//a[contains(.," Back To Editor")]');
    assert back_to_editor_btn.is_displayed() == True;
    assert back_to_editor_btn.get_attribute('innerText') == ' Back To Editor';
    back_to_editor_btn.click();

if (nameIndex is None):
    raise ValueError("Please provide proper name.");

driver.quit()
