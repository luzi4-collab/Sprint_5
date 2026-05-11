from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import ProfilePageLocators
from locators import LoginPageLocators
from locators import MainPageLocators
from constants import (
    LOGIN_PAGE, 
    PASSWORD_FIX,
    EMAIL_FIX
)

def test_logout_success(browser):

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
        
# клик по кнопке "Выход"
    browser.find_element(*ProfilePageLocators.EXIT_BUTTON).click()

# есть заголовок "Вход"
    assert expected_conditions.visibility_of_element_located(LoginPageLocators.ENTRANCE_HEADER)
