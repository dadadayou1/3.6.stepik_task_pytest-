import time
from selenium import webdriver 
from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestProductPage:
    
    def test_button_add_to_basket_is_visible(self, browser):
        browser.get(link)
        time.sleep(5)
        assert browser.find_element(By.ID,"add_to_basket_form")
 
