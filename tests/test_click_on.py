from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import ProfilePageLocators
from locators import LoginPageLocators
from locators import MainPageLocators
from helpers import (
    MAIN_PAGE,
    LOGIN_PAGE, 
    PASSWORD_FIX,
    EMAIL_FIX
)
def test_click_on_button_personal_account_logined_success(browser):

    browser.get(LOGIN_PAGE)

# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# Авторизация
    browser.find_element(*LoginPageLocators.USEREMAIL_FIELD).send_keys(EMAIL_FIX)
    browser.find_element(*LoginPageLocators.USERPASSWORD_FIELD).send_keys(PASSWORD_FIX)
    browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# клик по кнопке
    browser.find_element(*MainPageLocators.GOTO_PROFILE_BUTTON).click()

# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# текущий ULR = https://stellarburgers.education-services.ru/account/profile
    assert expected_conditions.visibility_of_element_located(ProfilePageLocators.PROFILE_BUTTON)


def test_click_on_button_personal_account_logouted_success(browser):

    browser.get(MAIN_PAGE)

# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# клик по кнопке "Личный Кабинет"
    browser.find_element(*MainPageLocators.GOTO_PERSONAL_ACCOUNT_BUTTON).click()

# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# есть заголовок "Вход"
    assert expected_conditions.visibility_of_element_located(LoginPageLocators.ENTRANCE_HEADER)


def test_click_on_rolls_button_success(browser):

    browser.get(MAIN_PAGE)

# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# клик по кнопке "Начинки"
    browser.find_element(*MainPageLocators.GOTO_FILLINGS_BUTTON).click()

# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# клик по кнопке "Булки"
    browser.find_element(*MainPageLocators.GOTO_ROLLS_BUTTON).click()

# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)    

# активный элемент "Булки"
    assert expected_conditions.visibility_of_element_located(MainPageLocators.ROLLS_ACTIVE)


def test_click_on_sauces_button_success(browser):

    browser.get(MAIN_PAGE)

# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# клик по кнопке "Соусы"
    browser.find_element(*MainPageLocators.GOTO_SAUCES_BUTTON).click()

# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# активный элемент "Соусы"
    assert expected_conditions.visibility_of_element_located(MainPageLocators.SAUCES_ACTIVE)


def test_click_on_fillings_button_success(browser):

    browser.get(MAIN_PAGE)

# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# клик по кнопке "Начинки"
    browser.find_element(*MainPageLocators.GOTO_FILLINGS_BUTTON).click()

# явное ожидание для загрузки страницы
    WebDriverWait(browser, 10)

# активный элемент "Начинки"
    assert expected_conditions.visibility_of_element_located(MainPageLocators.FILLINGS_ACTIVE)
