import time
from .pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException
import pytest


xfail = pytest.mark.xfail


@pytest.mark.parametrize('promo_offer', ["0", "1", "3", "4", "5", "6", "7", "8", "9"])
@xfail
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_product_basket_add()
    page.solve_quiz_and_get_code()
    page.should_be_name_product()
    page.should_be_price_product()
    time.sleep(60)


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_product_basket_add()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_product_basket_add()
    page.should_not_be_success_message_disappeared()
