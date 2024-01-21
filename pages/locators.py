from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    # LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    # LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    # LOGIN_BUTTON = (By.CSS_SELECTOR, "#login_form > button")
    # FORGOT_PASSWORD = (By.CSS_SELECTOR, "#login_form > p > a")
    #
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    # REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    # REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    # REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    # REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    BOOK_NAME_BASKET = (By.CSS_SELECTOR, "div.alertinner > strong")
    BOOK_NAME = (By.CSS_SELECTOR, "div h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main p[class='price_color']")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alert div p strong")
