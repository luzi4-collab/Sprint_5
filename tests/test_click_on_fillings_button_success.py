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
        driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()

# явное ожидание для загрузки страницы
        WebDriverWait(driver, 10)

# не виден элемент "Соусы"
        assert expected_conditions.invisibility_of_element_located((By.XPATH, ".//div/main/section[1]/div[2]/h2[2]"))

    finally:
        driver.quit()
