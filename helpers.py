# хелперы для тестов

# импорт библиотек (модулей)

import random

# функция генерации случайных данных

def random_element(max_chars):
    letters = 'abcdefghijklmnopqrstuvwxyz_0123456789'
    random_element = ''
    for _ in range(max_chars):
        random_element += random.choice(letters)
    return random_element

# случайные логин, пароль, email, созданные с помощью функции генерации случайных данных

def generate_login_random():
    return random_element(5)

def generate_password_random():
    return random_element(6)

def generate_email_random():
    return f"{random_element(5)}@ya.ru"

def generate_password_random_falue():
    return random_element(5)
