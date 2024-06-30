import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_alert_after_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.FIRST_ALERT), "Alert is not presented"

    def should_be_product_name_in_alert(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
            "Product name is not presented on the page"

        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

        assert self.is_element_present(*ProductPageLocators.FIRST_ALERT_PRODUCT_NAME), \
            "Product name is not presented in alert"

        product_name_in_alert = self.browser.find_element(*ProductPageLocators.FIRST_ALERT_PRODUCT_NAME).text

        assert product_name_in_alert == product_name, "Book name is incorrect"

    def should_be_price_in_alert(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), \
            "Product price is not presented on the page"

        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_PRICE), \
            "Alert with product price is not presented on the page"

        product_price_in_alert = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE).text

        assert product_price_in_alert == product_price, "Price is incorrect"
