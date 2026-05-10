from selenium.webdriver.support.wait import WebDriverWait
from locators import LoginPageLocators
from locators import MainPageLocators
from locators import ProfilePageLocators
from helpers import (
    MAIN_PAGE,
    LOGIN_PAGE, 
    PASSWORD_FIX,
    EMAIL_FIX
)

def test_form_personal_account_page_by_logotype_button_success(browser):

    browser.get(LOGIN_PAGE)

# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# Авторизация
    browser.find_element(*LoginPageLocators.USEREMAIL_FIELD).send_keys(EMAIL_FIX)
    browser.find_element(*LoginPageLocators.USERPASSWORD_FIELD).send_keys(PASSWORD_FIX)
    browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# клик по кнопке "Личный Кабинет"
    browser.find_element(*MainPageLocators.GOTO_PROFILE_BUTTON).click()

# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# клик по логитипу "STELLAR BURGER"
    browser.find_element(*ProfilePageLocators.LOGO_STELLAR_BURGER_BUTTON).click()

# текущий ULR = https://stellarburgers.education-services.ru
    assert browser.current_url == MAIN_PAGE


def test_form_personal_account_page_by_constructor_button_success(browser):

    browser.get(LOGIN_PAGE)

# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# Авторизация
    browser.find_element(*LoginPageLocators.USEREMAIL_FIELD).send_keys(EMAIL_FIX)
    browser.find_element(*LoginPageLocators.USERPASSWORD_FIELD).send_keys(PASSWORD_FIX)
    browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# клик по кнопке "Личный Кабинет"
    browser.find_element(*MainPageLocators.GOTO_PROFILE_BUTTON).click()

# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# клик по кнопке "Конструктор"
    browser.find_element(*ProfilePageLocators.GOTO_CONSTRUCTOR_BUTTON).click()

# текущий ULR = https://stellarburgers.education-services.ru
    assert browser.current_url == MAIN_PAGE
