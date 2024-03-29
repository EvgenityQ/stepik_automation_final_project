from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET = (By.CSS_SELECTOR,
                   "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")

class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, "#basket_formset > div")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login_form > button")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    BOOK_NAME_BASKET = (By.CSS_SELECTOR, "div.alertinner > strong")
    BOOK_NAME = (By.CSS_SELECTOR, "div h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main p[class='price_color']")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alert div p strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

