from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

def test_registration_success(login_page, email_fix, password_fix, personal_account_page):
    driver = webdriver.Chrome()

    try:
        driver.get(login_page)

# явное ожидание для загрузки страницы
        WebDriverWait(driver, 10)

# Авторизация
        driver.find_element(By.XPATH, ".//input[@name='name']").send_keys(email_fix)
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(password_fix)
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

# явное ожидание для загрузки страницы
        WebDriverWait(driver, 10)

# клик по кнопке
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

# явное ожидание для загрузки страницы
        WebDriverWait(driver, 10)

# текущий ULR = https://stellarburgers.education-services.ru/account/profile
        assert driver.current_url == personal_account_page

    finally:
        driver.quit()
