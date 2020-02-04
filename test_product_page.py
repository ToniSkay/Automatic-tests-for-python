from .base_page import BasePage
from .product_page import PageObject
import pytest

@pytest.mark.xfail
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