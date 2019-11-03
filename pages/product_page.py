from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def add_product_to_basket(self):
    #def go_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        button.click()
        time.sleep(2)
    def should_be_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD), "Message add is not presented"
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        messageadd = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD).text
        print (product)
        print (messageadd)
        assert product == messageadd, "No product add"

    def should_be_message_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_TOTAL), "Message total is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
        message_total = self.browser.find_element(*ProductPageLocators.MESSAGE_TOTAL)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        message_text = message_total.text
        product_text = product_price.text
        assert message_text == product_text, "No product price"
		
    def should_be_basket_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.is_element_present(*ProductPageLocators.BASKET_LINK), "Basket link is not presented"
        #assert "login" in str(*LoginPageLocators.CUR_URL), "Login url not found"