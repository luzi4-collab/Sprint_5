from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import LoginPageLocators
from locators import MainPageLocators
from locators import RegistrationPageLocators
from locators import ForgotPasswordPageLocators
from helpers import (
    MAIN_PAGE,
    REGISTER_PAGE,
    FORGOT_PASSPORT_PAGE,
    PASSWORD_FIX,
    EMAIL_FIX
)

def test_login_to_personal_accoun_from_main_page_success(browser):
    
    browser.get(MAIN_PAGE)

# клик по кнопке "Личный Кабинет"
    browser.find_element(*MainPageLocators.GOTO_PERSONAL_ACCOUNT_BUTTON).click()

# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# Авторизация
    browser.find_element(*LoginPageLocators.USEREMAIL_FIELD).send_keys(EMAIL_FIX)
    browser.find_element(*LoginPageLocators.USERPASSWORD_FIELD).send_keys(PASSWORD_FIX)
    browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# есть кнопка "Оформить заказ"
    assert expected_conditions.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON)


def test_login_from_registration_form_success(browser):

    browser.get(REGISTER_PAGE)

# клик по кнопке "Войти"
    browser.find_element(*RegistrationPageLocators.LOGIN_BUTTON).click()

# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# Авторизация
    browser.find_element(*LoginPageLocators.USEREMAIL_FIELD).send_keys(EMAIL_FIX)
    browser.find_element(*LoginPageLocators.USERPASSWORD_FIELD).send_keys(PASSWORD_FIX)
    browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# есть кнопка "Оформить заказ"
    assert expected_conditions.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON)


def test_login_from_forgot_password_form_success(browser):

    browser.get(FORGOT_PASSPORT_PAGE)

# клик по кнопке "Войти"
    browser.find_element(*ForgotPasswordPageLocators.LOGIN_BUTTON).click()

# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# Авторизация
    browser.find_element(*LoginPageLocators.USEREMAIL_FIELD).send_keys(EMAIL_FIX)
    browser.find_element(*LoginPageLocators.USERPASSWORD_FIELD).send_keys(PASSWORD_FIX)
    browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# есть кнопка "Оформить заказ"
    assert expected_conditions.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON)


def test_login_by_personal_account_button_success(browser):

    browser.get(MAIN_PAGE)

# клик по кнопке "Личный Кабинет"
    browser.find_element(*MainPageLocators.GOTO_PROFILE_BUTTON).click()

# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# Авторизация
    browser.find_element(*LoginPageLocators.USEREMAIL_FIELD).send_keys(EMAIL_FIX)
    browser.find_element(*LoginPageLocators.USERPASSWORD_FIELD).send_keys(PASSWORD_FIX)
    browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# есть кнопка "Оформить заказ"
    assert expected_conditions.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON)
