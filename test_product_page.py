from .locator import AddToBasketTest
from .base_page import BasePage
from .product_page import PageObject

def test_guest_can_add_product_to_basket(browser):
    link = AddToBasketTest.LINK_BASKET
    page = BasePage(browser, link)
    page.open()
    page_object = PageObject(browser, link)
    page_object.expected_product_name_and_price()
    page_object.add_to_basket()
    page.solve_quiz_and_get_code()
    page_object.check_correct_product_name()