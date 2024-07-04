import time

import pytest

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """
        Стартовая процедура для регистрации пользователя
        :param browser: Экземпляр браузера
        :return: Процедура
        """
        link = 'https://selenium1py.pythonanywhere.com/ru/accounts/login/'
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(str(time.time()) + "@fakemail.org", 'userpass321')
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """
        Проверка, что авторизованный пользователь может добавить продукт в корзину
        :param browser: Экземпляр браузера
        :return: Процедура
        """
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_alert_after_added_to_basket()
        page.should_be_product_name_in_alert()
        page.should_be_price_in_alert()

    def test_user_cant_see_success_message(self, browser):
        """
        Проверка, что авторизованный пользователь не видит сообщение о добавлении товара в корзину до его добавления
        :param browser: Экземпляр браузера
        :return: Процедура
        """
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue"
                                               "/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    """
    Проверка, что пользователь-гость может добавить товар в корзину
    :param browser: Экземпляр браузера
    :param link: Ссылка на товар, определена как параметр теста
    :return: Процедура
    """
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_alert_after_added_to_basket()
    page.should_be_product_name_in_alert()
    page.should_be_price_in_alert()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """
    Проверка, что пользователь-гость видит сообщение об успехе после добавления товара в корзину
    :param browser: Экземпляр браузера
    :return: Процедура
    """
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    """
    Проверка, что пользователь-гость не видит сообщение о добавлении товара в корзину до его добавления
    :param browser: Экземпляр браузера
    :return: Процедура
    """
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    Проверка, что сообщение о добавлении в корзину исчезает
    :param browser: Экземпляр браузера
    :return: Процедура
    """
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_disappeared_message()


def test_guest_should_see_login_link_on_product_page(browser):
    """
    Проверка, что пользователь-гость видит ссылку на страницу логина на странице товара
    :param browser: Экземпляр браузера
    :return: Процедура
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """
    Проверка, что пользователь-гость может перейти на страницу логина со страницы товара
    :param browser: Экземпляр браузера
    :return: Процедура
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
    Проверка, что пользователь-гость видит сообщение о пустой корзине, открытой со страницы товара
    :param browser: Экземпляр браузера
    :return: Процедура
    """
    link = f"http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty()
