from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    NAME_FIELD = (By.XPATH, ".//fieldset[1]//input")
    EMAIL_FIELD = (By.XPATH, ".//fieldset[2]//input")
    PASSWORD_FIELD = (By.XPATH, ".//input[@name='Пароль']")
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    REGISTER_ERROR_TEXT = (By.XPATH, ".//p[text()='Некорректный пароль']")
    LOGIN_BUTTON = (By.XPATH, ".//a[text()='Войти']")

class LoginPageLocators:
    USEREMAIL_FIELD = (By.XPATH, ".//input[@name='name']")
    USERPASSWORD_FIELD = (By.XPATH, ".//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    GOTO_REGISTER_BUTTON = (By.XPATH, ".//a[text()='Зарегистрироваться']")
    GOTO_FORGOT_PASSWORD_BUTTON = (By.XPATH, ".//a[text()='Восстановить пароль']")
    ENTRANCE_HEADER = (By.XPATH, ".//div/h2[text()='Вход']")

class ProfilePageLocators:
    EXIT_BUTTON = (By.XPATH, ".//div/nav/ul/li[3]/button")
    GOTO_CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    LOGO_STELLAR_BURGER_BUTTON = (By.XPATH, ".//div/a")
    PROFILE_BUTTON = (By.XPATH, ".//a[text()='Профиль']")

class MainPageLocators:
    GOTO_PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    GOTO_PROFILE_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")
    GOTO_ROLLS_BUTTON = (By.XPATH, ".//span[text()='Булки']")
    GOTO_SAUCES_BUTTON = (By.XPATH, ".//span[text()='Соусы']")
    GOTO_FILLINGS_BUTTON = (By.XPATH, ".//span[text()='Начинки']")
    PLACE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    ROLLS_ACTIVE = (By.XPATH, ".//div/main/section[1]/div[1]/div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Булки']")
    SAUCES_ACTIVE = (By.XPATH, ".//div/main/section[1]/div[1]/div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Соусы']")
    FILLINGS_ACTIVE = (By.XPATH, ".//div/main/section[1]/div[1]/div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Начинки']")


class ForgotPasswordPageLocators:
    LOGIN_BUTTON = (By.XPATH, ".//a[text()='Войти']")
