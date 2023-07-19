import time
from .pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_product_basket_add()
    page.solve_quiz_and_get_code()
    page.should_be_name_product()
    page.should_be_price_product()

