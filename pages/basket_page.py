from .base_page import BasePage
from .locators import BasketPageLocators, BasePageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_FORM), 'Basket is not empty'
        basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert 'Ваша корзина пуста' in basket_text, 'Message text is not displayed'

    def should_be_product(self):
        pass
