from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        """
        Инициализация страницы логина
        :return: Процедура
        """
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """
        Проверка на корректный адрес страницы логина
        :return: Процедура
        """
        assert ("login" in self.browser.current_url), (f"expected 'login' to be substring of "
                                                       f"'{self.browser.current_url}'")

    def should_be_login_form(self):
        """
        Проверка формы логина на странице логина
        :return: Процедура
        """
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        """
        Проверка формы регистрации на странице логина
        :return: Процедура
        """
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        """
        Регистрация нового пользователя
        :param email: Email пользователя
        :param password: Пароль пользователя
        :return: Процедура
        """
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        email_field.send_keys(email)

        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD)
        password_field.send_keys(password)

        confirmation_password_field = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRMATION_PASSWORD_FIELD)
        confirmation_password_field.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
