from .base_page import BasePage
from .locators import LoginPageLocators
import time
import random


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        assert login in self.url, f"The following issue happened {AssertionError}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), f"The following issue happened {AssertionError}"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), \
            f"The following issue happened {AssertionError}"
    def register_new_user(self):
        count = random.randint(1, 1000)
        email = str(time.time() + count) + "@fakemail.org"
        password = str(time.time() + count)
        register_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        register_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        register_password_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM).send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

