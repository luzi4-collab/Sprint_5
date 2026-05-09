# Sprint_5

# список файлов:

# conftest.py - файл с фикстурами

# все тесты размещены в каталоге tests, список тестов по файлам:
# test_registration_success.py - успешная регистрация
# test_registration_falue.py - ошибка регистрации по причины неправильного пароля (пароль короче 6 символов)
# test_login_to_personal_accoun_from_main_page_success.py - вход по кнопке "Войти в аккаунт" на главной
# test_login_from_registration_form_success.py - вход по кнопке с формы регистрации
# test_login_from_forgot_password_form_success.py - вход по кнопке с формы восстановления пароля
# test_login_by_personal_account_button_success.py - вход по кнопке "Личный кабинет"
# test_click_on_button_personal_account_logouted_success.py - переход по клику на "Личный кабинет", незалогиненный пользователь
# test_click_on_button_personal_account_logined_success.py - переход по клику на "Личный кабинет", залогиненный пользователь
# test_form_personal_account_page_by_constructor_button_success.py - переход из личного кабинета по клику на "Конструктор"
# test_form_personal_account_page_by_logotype_button_success.py - переход из личного кабинета по клику на на логотип Stellar Burgers
# test_logout_success.py - выход по кнопке "Выйти" в личном кабинете
# test_click_on_rolls_button_success.py - переход к разделу "Булки"
# test_click_on_sauces_button_success.py - переход к разделу "Соусы"
# test_click_on_fillings_button_success.py - переход к разделу "Начинки"


# ФОРМЫ И ЛОКАТОРЫ


# 1. Регистрация
# ссылка на форму: https://stellarburgers.education-services.ru/register

# 1.1. поле ввода "Имя"
# XPATH = ".//fieldset[1]//input"

# 1.2. поле ввода "Email"
# XPATH = ".//fieldset[2]//input"

# 1.3. поле ввода "Пароль"
# XPATH = ".//input[@name='Пароль']"

# 1.4. кнопка "Зарегистрироваться"
# XPATH = ".//button[text()='Зарегистрироваться']"

# 1.5. ошибка для некорректного пароля
# XPATH - ".//p[text()='Некорректный пароль']"


# 2. Вход
# ссылка на https://stellarburgers.education-services.ru/login

# 2.1. поле ввода "Email"
# XPATH = ".//input[@name='name']"

# 2.2. поле ввода "Пароль"
# XPATH = ".//input[@name='Пароль']"

# 2.3. кнопка "Войти"
# XPATH = ".//button[text()='Войти']"

# 2.4. кнопка "Зарегистрироваться"
# XPATH = ".//a[text()='Зарегистрироваться']"

# 2.5. кнопка "Восстановить пароль"
# XPATH = ".//a[text()='Восстановить пароль']"

# 2.6. заголовок "Вход"
# XPATH = ".//div/h2[text()='Вход']"

# 2.7. текст ошибки о некорректном пароле
# XPATH = ".//p[text()='Некорректный пароль']"


# 3. Личный кабинет
# ссылка на форму: https://stellarburgers.education-services.ru/account/profile

# 3.1. кнопка "Выход"
# XPATH = ".//div/nav/ul/li[3]/button"

# 3.2. "Конструктор"
# XPATH = ".//p[text()='Конструктор']" - верно для всех форм
# переход на https://stellarburgers.education-services.ru/

# 3.3. логотип Stellar Burgers
# XPATH = ".//div/a" - верно для всех форм
# переход на https://stellarburgers.education-services.ru/


# 4. Главная
# ссылка на форму: https://stellarburgers.education-services.ru

# 4.1. кнопка "Войти в аккаунт"
# XPATH = ".//button[text()='Войти в аккаунт']"

# 4.2. кнопка "Личный Кабинет"
# XPATH = ".//p[text()='Личный Кабинет']" - верно для всех форм

# 4.3. пункт "Булки"
# XPATH = ".//span[text()='Булки']"

# 4.4. пункт "Соусы"
# XPATH = ".//span[text()='Соусы']"

# 4.5. пункт "Начинки"
# XPATH = ".//span[text()='Начинки']"

# 4.6. кнопка "Оформить заказ"
# XPATH = ".//button[text()='Оформить заказ']"

# 4.7. заголовок "Булки"
# XPATH = ".//div/main/section[1]/div[2]/h2[1]"

# 4.8. заголовок "Соусы"
# XPATH = ".//div/main/section[1]/div[2]/h2[2]"

# 4.9. заголовок "Начинки"
# XPATH = ".//div/main/section[1]/div[2]/h2[3]"


# 5. Восстановление пароля
# ссылка на форму: https://stellarburgers.education-services.ru/forgot-password

# 5.1. кнопка "Войти"
# XPATH = ".//a[text()='Войти']"
