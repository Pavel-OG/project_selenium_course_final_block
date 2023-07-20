from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
import math
import webbrowser


class ProductPage(BasePage):
    def go_product_basket_add(self):
        self.browser.find_element(*ProductPageLocators.BTN_ADD_BASKET).click()


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

    def should_be_name_product(self):
        product_name = self.is_element_present(*ProductPageLocators.PRODUCT_NAME)
        message = self.is_element_present(*ProductPageLocators.CONFIRM_MESSAGE)
        assert product_name == message, "Наименование товара отсутсвует в корзине"

    def should_be_price_product(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message_price = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        assert product_price in message_price, "Цена товара не соответствует цене в корзине"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
