# фикстуры для тестов

# импорт библиотек (модулей)
import pytest

import random

# функция генерации случайных данных

def random_element(max_chars):
    letters = 'abcdefghijklmnopqrstuvwxyz_0123456789'
    random_element = ''
    for _ in range(max_chars):
        random_element += random.choice(letters)
    return random_element

# фикстуры для URL

@pytest.fixture(scope='function')
def main_page():
    main_page = "https://stellarburgers.education-services.ru/"
    return main_page

@pytest.fixture(scope='function')
def login_page():
    login_page = "https://stellarburgers.education-services.ru/login"
    return login_page

@pytest.fixture(scope='function')
def register_page():
    register_page = "https://stellarburgers.education-services.ru/register"
    return register_page

@pytest.fixture(scope='function')
def forgot_password_page():
    forgot_password_page = "https://stellarburgers.education-services.ru/forgot-password"
    return forgot_password_page

@pytest.fixture(scope='function')
def personal_account_page():
    personal_account_page = "https://stellarburgers.education-services.ru/account/profile"
    return personal_account_page

# фикстуры для логина, пароля, email

# фиксированные логин, пароль, email

@pytest.fixture(scope='function')
def login_fix():
    login_fix = "minakova_46fs"
    return login_fix

@pytest.fixture(scope='function')
def password_fix():
    password_fix = "123456poiuyt"
    return password_fix

@pytest.fixture(scope='function')
def email_fix():
    email_fix = "minakova_46fs-cohort@ya.ru"
    return email_fix

# случайные логин, пароль, email, созданные с помощью функции генерации случайных данных

@pytest.fixture(scope='function')
def login_random():
    login_random = random_element(5)
    return login_random

@pytest.fixture(scope='function')
def password_random():
    password_random = random_element(6)
    return password_random

@pytest.fixture(scope='function')
def email_random():
    email_random = random_element(5) + '@ya.ru'
    return email_random

@pytest.fixture(scope='function')
def password_random_falue():
    password_random_falue = random_element(5)
    return password_random_falue
