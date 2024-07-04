from selenium.webdriver.common.by import By


class BasePageLocators:
    """
    Локаторы для base_page
    """
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "div.basket-mini .btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LANGUAGE = (By.CSS_SELECTOR, "html[lang]")


class MainPageLocators:
    """
    Локаторы для main_page
    """
    pass


class LoginPageLocators:
    """
    Локаторы для login_page
    """
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_FORGOTTEN_LINK = (By.TAG_NAME, "a")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name=login_submit]")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRMATION_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit]")


class ProductPageLocators:
    """
    Локаторы для product_page
    """
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main  h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "div#messages :first-child div.alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, "div#messages div.alertinner p strong")


class BasketPageLocators:
    """
    Локаторы для basket_page
    """
    PRODUCT_FORM = (By.CSS_SELECTOR, "form#basket_formset")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "div.content p")
