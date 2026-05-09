# Sprint_5

# список файлов:
# файл с фикстурами - conftest.py


 
# ФОРМЫ И ЛОКАТОРЫ по пунктам задания проекта


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

# 2.1. по кнопке "Войти в аккаунт" на главной
# ссылка на форму: https://stellarburgers.education-services.ru/

# 2.1.1. кнопка "Войти в аккаунт"
# XPATH = ".//button[text()='Войти в аккаунт']"
# переход на https://stellarburgers.education-services.ru/login

# 2.1.2. поле ввода "Email"
# XPATH = ".//input[@name='name']"

# 2.1.3. поле ввода "Пароль"
# XPATH = ".//input[@name='Пароль']"

# 2.1.4. кнопка "Войти"
# XPATH = ".//button[text()='Войти']"

# 2.2. через кнопку "Личный кабинет"
# ссылки:
#    https://stellarburgers.education-services.ru/
#    https://stellarburgers.education-services.ru/register
#    https://stellarburgers.education-services.ru/forgot-password

# 2.2.1. кнопка "Личный Кабинет"
# XPATH = ".//p[text()='Личный Кабинет']" - верно для всех форм
# переход на https://stellarburgers.education-services.ru/login

# 2.2.2. поле ввода "Email"
# XPATH = ".//input[@name='name']"

# 2.2.3. поле ввода "Пароль"
# XPATH = ".//input[@name='Пароль']"

# 2.2.4. кнопка "Войти"
# XPATH = ".//button[text()='Войти']"

# 2.3. по кнопке с формы регистрации
# ссылка: https://stellarburgers.education-services.ru/login

# 2.3.1. кнопка "Зарегистрироваться"
# XPATH = ".//a[text()='Зарегистрироваться']"
# переход на https://stellarburgers.education-services.ru/register

# 2.3.1.1. поле ввода "Имя"
# XPATH = ".//fieldset[1]//input"

# 2.3.1.2. поле ввода "Email"
# XPATH = ".//fieldset[2]//input"

# 2.3.1.3. поле ввода "Пароль"
# XPATH = ".//input[@name='Пароль']"

# 2.3.1.4. кнопка "Зарегистрироваться"
# XPATH = ".//button[text()='Зарегистрироваться']"

# 2.3.2. кнопка "Войти"
# XPATH = ".//a[text()='Войти']"
# переход на https://stellarburgers.education-services.ru/login

# 2.4. по кнопку в форме восстановления пароля
# ссылка: https://stellarburgers.education-services.ru/login

# 2.4.1. кнопка "Восстановить пароль"
# XPATH = ".//a[text()='Восстановить пароль']"
# переход на https://stellarburgers.education-services.ru/forgot-password

# 2.4.1.1. поле ввода "Email"
# XPATH = ".//input[@name='name']"

# 2.4.1.2. кнопка "Восстановить"
# XPATH = ".//button[text()='Восстановить']"

# 2.4.2. кнопка "Войти"
# XPATH = ".//a[text()='Войти']"
# переход на https://stellarburgers.education-services.ru/login


# 3. Переход в личный кабинет
# ссылки:
#    https://stellarburgers.education-services.ru/
#    https://stellarburgers.education-services.ru/register
#    https://stellarburgers.education-services.ru/forgot-password

# 3.1. кнопка "Личный Кабинет"
# XPATH = ".//p[text()='Личный Кабинет']" - верно для всех форм
# переход на https://stellarburgers.education-services.ru/login


# 4. Переход из личного кабинета в Конструктор
# ссылка: https://stellarburgers.education-services.ru/ ????? - уточнить

# 4.1. "Конструктор"
# XPATH = ".//p[text()='Конструктор']" - верно для всех форм
# переход на https://stellarburgers.education-services.ru/

# 4.2. логотип Stellar Burgers
# XPATH = ".//div/a" - верно для всех форм
# переход на https://stellarburgers.education-services.ru/


# 5. Выход из аккаунта
# ссылка:
# кнопка "Выйти"


# 6. Раздел "Конструктор"
# ссылка: https://stellarburgers.education-services.ru/

# 6.1. переход в "Булки"
# XPATH = ".//span[text()='Булки']"
# видимость блока с булкой XPATH = ".//div/main/section[1]/div[2]/ul[1]/a" 
# или видимость заголовка блока "Булки" XPATH = ".//div/main/section[1]/div[2]/h2[1]"

# 6.2. переход в "Соусы"
# XPATH = ".//span[text()='Соусы']"
# видимость блока с соусом XPATH = ".//div/main/section[1]/div[2]/ul[2]/a" 
# или видимость заголовка блока "Соусы" XPATH = ".//div/main/section[1]/div[2]/h2[2]" + не видимость заголовка блока "Булки" XPATH = ".//div/main/section[1]/div[2]/h2[1]"

# 6.3. переход в "Начинки"
# XPATH = ".//span[text()='Начинки']"
# видимость блока с начинкой XPATH = ".//div/main/section[1]/div[2]/ul[3]/a" 
# или видимость заголовка блока "Начинки" XPATH = ".//div/main/section[1]/div[2]/h2[3]" + не видимость заголовков "Булки" и "Соусы" (XPATH = ".//div/main/section[1]/div[2]/h2[1]" и XPATH = ".//div/main/section[1]/div[2]/h2[2]")



# РАСКЛАДКА ПО ФОРМАМ


# 1. форма Регистрация
# ссылка на форму: https://stellarburgers.education-services.ru/register

# тест 1: Успешная регистрация

# поле ввода "Имя" - валидное имя непустое: например, 1
# XPATH = ".//fieldset[1]//input"
# поле ввода "Email" - валидный email в формате логин@домен: например, 123@ya.ru
# XPATH = ".//fieldset[2]//input"
# поле ввода "Пароль" - валидный пароль не менее 6 символов: например, 123456
# XPATH = ".//input[@name='Пароль']"
# кнопка "Зарегистрироваться"
# XPATH = ".//button[text()='Зарегистрироваться']"
# Критерий прохождения: успешный переход на страницу входа (отображение элемента с XPATH = ".//div/h2[text()='Вход']") (ссылка: https://stellarburgers.education-services.ru/login)

# тест 2: Ошибка некорректного пароля

# поле ввода "Имя" - валидное имя непустое: например, 1
# XPATH = ".//fieldset[1]//input"
# поле ввода "Email" - валидный email в формате логин@домен: например, 123@ya.ru
# XPATH = ".//fieldset[2]//input"
# поле ввода "Пароль" - не валидный пароль менее 6 символов: например, 12345
# XPATH = ".//input[@name='Пароль']"
# кнопка "Зарегистрироваться"
# XPATH = ".//button[text()='Зарегистрироваться']"
# Критерий прохождения: появление ошибки для некорректного пароля 'Некорректный пароль' (XPATH - ".//p[text()='Некорректный пароль']")

# тест 3: Переход ко Входу

# кнопка "Войти"
# XPATH = ".//a[text()='Войти']"
# Критерий прохождения: успешный переход на https://stellarburgers.education-services.ru/login

# тест 4: Переход в ЛК по кнопке по кнопке "Личный кабинет"

# кнопка "Личный Кабинет"
# XPATH = ".//p[text()='Личный Кабинет']" - верно для всех форм
# Критерий прохождения: успешный переход в ЛК или успешный переход на https://stellarburgers.education-services.ru/login


# 2. форма Главная
# ссылка на форму: https://stellarburgers.education-services.ru

# тест 1: Вход и переход ко Входу

# тест 1.1: Переход ко Входу с Главной по кнопке "Войти в аккаунт"

# кнопка "Войти в аккаунт"
# XPATH = ".//button[text()='Войти в аккаунт']"
# Критерий прохождения: успешный переход на https://stellarburgers.education-services.ru/login

# тест 1.2: Переход ко Входу с Главной по кнопке "Личный кабинет"

# кнопка "Личный Кабинет"
# XPATH = ".//p[text()='Личный Кабинет']" - верно для всех форм
# Критерий прохождения: успешный переход на https://stellarburgers.education-services.ru/login

# тест 1.3: Переход в ЛК по кнопке по кнопке "Личный кабинет"

# кнопка "Личный Кабинет"
# XPATH = ".//p[text()='Личный Кабинет']" - верно для всех форм
# Критерий прохождения: успешный переход в ЛК

# тест 2: Переходы к разделам конструктора

# тест 2.1: Переход в "Булки"

# пункт "Булки"
# XPATH = ".//span[text()='Булки']"
# Критерий прохождения: видимость блока с булкой XPATH = ".//div/main/section[1]/div[2]/ul[1]/a" 
# или видимость заголовка блока "Булки" XPATH = ".//div/main/section[1]/div[2]/h2[1]"

# тест 2.2: Переход в "Соусы"

# пункт "Соусы"
# XPATH = ".//span[text()='Соусы']"
# Критерий прохождения: видимость блока с соусом XPATH = ".//div/main/section[1]/div[2]/ul[2]/a" 
# или видимость заголовка блока "Соусы" XPATH = ".//div/main/section[1]/div[2]/h2[2]" + не видимость заголовка блока "Булки" XPATH = ".//div/main/section[1]/div[2]/h2[1]"

# тест 2.3: Переход в "Начинки"

# пункт "Начинки"
# XPATH = ".//span[text()='Начинки']"
# Критерий прохождения: видимость блока с начинкой XPATH = ".//div/main/section[1]/div[2]/ul[3]/a" 
# или видимость заголовка блока "Начинки" XPATH = ".//div/main/section[1]/div[2]/h2[3]" + не видимость заголовков "Булки" и "Соусы" (XPATH = ".//div/main/section[1]/div[2]/h2[1]" и XPATH = ".//div/main/section[1]/div[2]/h2[2]")


# 3. форма Вход
# ссылка на форму: https://stellarburgers.education-services.ru/login

# тест 1: Успешный Вход

# поле ввода "Email"
# XPATH = ".//input[@name='name']"
# поле ввода "Пароль"
# XPATH = ".//input[@name='Пароль']"
# кнопка "Войти"
# XPATH = ".//button[text()='Войти']"
# Критерий прохождения: успешная регистрация: нет ошибки, есть кнопка "Оформить заказ" (XPATH = ".//button[text()='Оформить заказ']")

# тест 2: Переход в ЛК по кнопке по кнопке "Личный кабинет"

# кнопка "Личный Кабинет"
# XPATH = ".//p[text()='Личный Кабинет']" - верно для всех форм
# Критерий прохождения: успешный переход в ЛК

# тест 3: Переход к регистрации по кнопке  "Зарегистрироваться"

# кнопка "Зарегистрироваться"
# XPATH = ".//button[text()='Зарегистрироваться']"
# Критерий прохождения: успешный переход на https://stellarburgers.education-services.ru/register

# тест 4: Переход к восстановлению пароля по кнопке "Восстановить пароль"

# кнопка "Восстановить пароль"
# XPATH = ".//a[text()='Восстановить пароль']"
# Критерий прохождения: успешный переход на https://stellarburgers.education-services.ru/forgot-password


# 4. форма Восстановление пароля
# ссылка на форму: https://stellarburgers.education-services.ru/forgot-password

# тест 1: Переход ко Входу

# кнопка "Войти"
# XPATH = ".//a[text()='Войти']"
# Критерий прохождения: успешный переход на https://stellarburgers.education-services.ru/login

# тест 2: Переход в ЛК по кнопке по кнопке "Личный кабинет"

# кнопка "Личный Кабинет"
# XPATH = ".//p[text()='Личный Кабинет']" - верно для всех форм
# Критерий прохождения: успешный переход в ЛК или успешный переход на https://stellarburgers.education-services.ru/login


# 5. форма Личный кабинет (ЛК)
# ссылка на форму: ?????

# тест 1: Переход в Конструктор по кнопке Конструктор

# кнопка "Конструктор"
# XPATH = ".//p[text()='Конструктор']" - верно для всех форм
# Критерий прохождения: успешный переход на https://stellarburgers.education-services.ru/

# тест 2: Переход в Конструктор по клику на логотип Stellar Burgers

# логотип Stellar Burgers
# XPATH = ".//div/a" - верно для всех форм
# Критерий прохождения: успешный переход на https://stellarburgers.education-services.ru/

# тест 3: Выход

# кнопка "Выйти"
# XPATH = ???????
# Критерий прохождения: успешный переход на https://stellarburgers.education-services.ru/


# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
