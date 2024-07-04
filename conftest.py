import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    """
    Добавление выбора опций браузера и языка для запуска тестов
    :param parser: Объект pytest для парсинга аргументов командной строки, а также для значений файла .ini
    :return: Процедура
    """
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    """
    Инициализация браузера
    :param request: Встроенная фикстура request, которая получает данные о текущем запущенном тесте
    :return: Процедура
    """
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = OptionsFirefox()
        options.set_preference("intl.accept_languages", language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser

    browser.quit()
