from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        """
        Добавление товара в корзину
        :return: Процедура
        """
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_alert_after_added_to_basket(self):
        """
        Проверка сообщения об успехе после добавления товара в корзину
        :return: Процедура
        """
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Alert is not presented"

    def should_be_product_name_in_alert(self):
        """
        Проверка наименования товара в сообщении об успехе после добавления товара в корзину
        :return: Процедура
        """
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
            "Product name is not presented on the page"

        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME), \
            "Product name is not presented in alert"

        product_name_in_alert = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text

        assert product_name_in_alert == product_name, "Book name is incorrect"

    def should_be_price_in_alert(self):
        """
        Проверка цены в сообщении после добавления товара в корзину
        :return: Процедура
        """
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), \
            "Product price is not presented on the page"

        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_PRICE), \
            "Alert with product price is not presented on the page"

        product_price_in_alert = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE).text

        assert product_price_in_alert == product_price, "Price is incorrect"

    def should_not_be_success_message(self):
        """
        Проверка отсутствия сообщения об успехе
        :return: Процедура
        """
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_message(self):
        """
        Проверка исчезания сообщения
        :return: Процедура
        """
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
