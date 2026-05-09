from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_registration_falue(register_page, login_random, email_random, password_random_falue):
    driver = webdriver.Chrome()

    try:
        driver.get(register_page)

# Авторизация
        driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(login_random)
        driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(email_random)
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(password_random_falue)
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

# явное ожидание для загрузки страницы
        WebDriverWait(driver, 10)

# есть ошибка 'Некорректный пароль'
        assert expected_conditions.visibility_of_element_located((By.XPATH, ".//p[text()='Некорректный пароль']"))

    finally:
        driver.quit()
