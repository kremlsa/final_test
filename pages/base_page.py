from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from .locators import MainPageLocators
from .locators import ProductPageLocators

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    def open(self):
        self.browser.get(self.url)
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
           alert = self.browser.switch_to.alert
           alert_text = alert.text
           print(f"Your code: {alert_text}")
           alert.accept()
        except NoAlertPresentException:
           print("No second alert presented")
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
		
    def should_be_basket_link_top(self):
        assert self.is_element_present(*BasePageLocators.BASKET_LINK_TOP), "Basket link is not presented"
		
    def open_basket_link_top(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK_TOP)
        link.click()
		
    def guest_cant_see_product_in_basket(self):		
        assert self.is_not_element_present(*MainPageLocators.BASKET_ITEMS), "Basket items is presented, but should not be"
		
    def guest_cant_see_message_empty(self):			
        message = self.browser.find_element(*MainPageLocators.BASKET_MESSAGE).text
        assert message == "Your basket is empty. Continue shopping" , "Message not presented"
