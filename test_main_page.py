import pytest

from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage


link = 'https://selenium1py.pythonanywhere.com/'


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        """
        Проверка, что пользователь-гость может перейти на страницу логина
        :param browser: Экземпляр браузера
        :return: Процедура
        """
        page = MainPage(browser,
                        link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        """
        Проверка, что пользователь-гость видит ссылку на страницу логина
        :param browser: Экземпляр браузера
        :return: Процедура
        """
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    Проверка, что пользователь-гость может открыть страницу корзины с главной страницы сайта
    :param browser: Экземпляр браузера
    :return: Процедура
    """
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty()
