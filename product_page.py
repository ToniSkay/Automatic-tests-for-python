from selenium import webdriver
from .base_page import BasePage
from .locator import AddToBasketTest

class PageObject(BasePage, AddToBasketTest):
    def expected_product_name_and_price(self):
        self.expected_name = self.browser.find_element(*AddToBasketTest.EXPECTED_NAME_PRODUCT).text
        self.expected_price = self.browser.find_element(*AddToBasketTest.EXPECTED_PRICE_PRODUCT).text

    def add_to_basket(self):
        self.browser.execute_script('window.scrollTo(0,100)')
        self.browser.find_element(*AddToBasketTest.BASKET_SELECT).click()

    def check_correct_product_name(self):
        real_name = self.browser.find_element(*AddToBasketTest.REAL_NAME_PRODUCT).text
        assert self.expected_name == real_name, 'Invalid product name in basket'

    def check_correct_product_price(self):
        real_price = self.browser.find_element(*AddToBasketTest.REAL_PRICE_PRODUCT).text
        assert self.expected_price == real_price, 'Invalid product price in basket'




