from . import languages

from .base_page import BasePage
from .locators import BasketPageLocators, BasePageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        """
        Проверка, что корзина пуста
        :return: Процедура
        """
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_FORM), 'Basket is not empty'
        lang = self.browser.find_element(*BasePageLocators.LANGUAGE).get_attribute("lang")
        basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert languages.empty_basket[lang] in basket_text, 'Message text is not displayed'

    def should_be_product(self):
        """
        Проверка товара в корзине (заглушка)
        :return: Процедура
        """
        pass
