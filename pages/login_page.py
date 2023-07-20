from .base_page import BasePage
from.locators import BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in "http://selenium1py.pythonanywhere.com/ru/accounts/login/", 'element login is not in URL'
        assert True

    def should_be_login_form(self):
        assert self.browser.find_element(*BasePageLocators.LOGIN_FORM), 'Login form element not found'
        assert True

    def should_be_register_form(self):
        assert self.browser.find_element(*BasePageLocators.REGISTRATION_FORM), 'Registration form element not found'
        assert True