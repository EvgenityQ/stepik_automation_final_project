from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_card(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        link.click()

    def product_is_added(self):
        book_message = self.browser.find_element(*ProductPageLocators.BOOK_NAME_BASKET)
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)

        book_price_in_basket = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)

        print(book_message.text)
        print(book_name.text)
        print(book_price_in_basket.text)
        print(book_price.text)

        assert book_message.text in book_name.text, "The Name of the Book is not the same"
        assert book_price_in_basket.text == book_price.text, "Price is not the same"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"


    def should_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message didn't disappear"






