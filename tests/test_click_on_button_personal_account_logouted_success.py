from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_registration_success(main_page):
    driver = webdriver.Chrome()

    try:
        driver.get(main_page)

# явное ожидание для загрузки страницы
        WebDriverWait(driver, 10)

# клик по кнопке
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

# явное ожидание для загрузки страницы
        WebDriverWait(driver, 10)

# есть заголовок "Вход"
        assert expected_conditions.visibility_of_element_located((By.XPATH, ".//div/h2[text()='Вход']"))

    finally:
        driver.quit()
