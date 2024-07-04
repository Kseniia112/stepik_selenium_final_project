from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        """
        Инициализация главной страницы
        :param args: Экземпляр браузера
        :param kwargs: Путь (ссылка)
        """
        super(MainPage, self).__init__(*args, **kwargs)
