from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")


class ProductPageLocators():
    BTN_ADD_BASKET = (By.ID, "add_to_basket_form")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    CONFIRM_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong")




