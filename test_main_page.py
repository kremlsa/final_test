from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import time
import pytest

#def test_guest_can_go_to_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#    page.open()                      # открываем страницу
#    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
#    login_page = LoginPage(browser, browser.current_url)
#    login_page.should_be_login_page()
	
#def test_guest_should_see_login_link(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    page = MainPage(browser, link)
#    page.open()
#    page.should_be_login_link()
	
#def test_should_be_login_url(browser):
#    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
#    page = LoginPage(browser, link)
#    page.open()
#    page.should_be_login_url()

#def test_guest_should_be_login_form(browser):
#    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
#    page = LoginPage(browser, link)
#    page.open()
#    page.should_be_login_form()

#def test_guest_should_be_reg_form(browser):
#    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
#    page = LoginPage(browser, link)
#    page.open()
#    page.should_be_register_form()
	
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    link ="http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_basket_link_top()
    time.sleep(5)
    page.open_basket_link_top()
    page.guest_cant_see_product_in_basket()	
    page.guest_cant_see_message_empty()	
    time.sleep(5)
	