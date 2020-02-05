from .base_page import BasePage
from .product_page import PageObject
import pytest

''''@pytest.mark.xfail
@pytest.mark.parametrize('link', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4",
                                  "?promo=offer5", "?promo=offer6", "?promo=offer7", "?promo=offer8", "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = f'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/{link}'
    page = BasePage(browser, link)
    page.open()
    page_object = PageObject(browser, link)
    page_object.expected_product_name_and_price()
    page_object.add_to_basket()
    page.solve_quiz_and_get_code()
    page_object.check_correct_product_name()
    page_object.check_correct_product_price()

def test_negative_checks(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207'
    page_object = PageObject(browser, link)
    page_object.test_guest_cant_see_success_message_after_adding_product_to_basket()

def test_negative_checks1(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207'
    page_object = PageObject(browser, link)
    page_object.test_guest_cant_see_success_message()

def test_negative_checks2(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207'
    page_object = PageObject(browser, link)
    page_object.test_message_disappeared_after_adding_product_to_basket()'''

def test_login_page_checking(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page_object = PageObject(browser, link)
    page_object.test_guest_should_see_login_link_on_product_page()

def test_go_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page_object = PageObject(browser, link)
    page_object.test_guest_can_go_to_login_page_from_product_page()


