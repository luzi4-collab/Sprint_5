from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_registration_success(login_page, email_fix, password_fix):
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

# клик по кнопке
        driver.find_element(By.XPATH, ".//div/nav/ul/li[3]/button").click()

# есть заголовок "Вход"
        assert expected_conditions.visibility_of_element_located((By.XPATH, ".//div/h2[text()='Вход']"))

    finally:
        driver.quit()
