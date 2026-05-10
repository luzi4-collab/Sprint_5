from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegistrationPageLocators
from locators import LoginPageLocators
from helpers import (
    REGISTER_PAGE, 
    generate_login_random, 
    generate_email_random, 
    generate_password_random, 
    generate_password_random_falue
)

def test_registration_success(browser):
    login_random = generate_login_random()
    email_random = generate_email_random()
    password_random = generate_password_random()

    browser.get(REGISTER_PAGE)

# Авторизация
    browser.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys(login_random)
    browser.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(email_random)
    browser.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(password_random)
    browser.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

# явное ожидание
    WebDriverWait(browser, 10)

# есть заголовок "Вход"
    assert expected_conditions.visibility_of_element_located(LoginPageLocators.ENTRANCE_HEADER)


def test_registration_falue(browser):
    login_random = generate_login_random()
    email_random = generate_email_random()
    password_random_falue = generate_password_random_falue()

    browser.get(REGISTER_PAGE)

# Авторизация
    browser.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys(login_random)
    browser.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(email_random)
    browser.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(password_random_falue)
    browser.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# есть ошибка 'Некорректный пароль'
    assert expected_conditions.visibility_of_element_located(RegistrationPageLocators.REGISTER_ERROR_TEXT)
