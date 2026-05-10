# фикстуры для тестов

# импорт библиотек (модулей)
import pytest

from selenium import webdriver

# старт и завершение работы браузера
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
