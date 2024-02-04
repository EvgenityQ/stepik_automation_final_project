from .locators import BasePageLocators
from .base_page import BasePage
from .main_page import MainPage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Basket is not empty"
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            (f"Expected basket is empty message, got {Exception}")

