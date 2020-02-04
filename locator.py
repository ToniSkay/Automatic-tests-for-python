from selenium.webdriver.common.by import By

class AddToBasketTest:
    LINK_BASKET = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
    BASKET_SELECT = (By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')

    EXPECTED_NAME_PRODUCT = (By.CSS_SELECTOR, 'div.col-sm-6.product_main h1')
    REAL_NAME_PRODUCT = (By.CSS_SELECTOR, 'div.alertinner strong')

    EXPECTED_PRICE_PRODUCT = (By.CSS_SELECTOR, 'div.col-sm-6.product_main .price_color')
    REAL_PRICE_PRODUCT = (By.CSS_SELECTOR, 'div.alertinner p strong ')
