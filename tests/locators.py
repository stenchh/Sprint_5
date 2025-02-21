from selenium.webdriver.common.by import By

class LoginPageLocators:
    ENTER_ACCOUNT_BUTTON = (By.XPATH, "//*[@id='root']/div/main/section[2]/div/button") #Кнопка "Войти в аккаунт
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]") # Кнопка "Личный кабинет"
    EMAIL_INPUT = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input") #Поле ввода почты
    PASSWORD_INPUT = (By.NAME, "Пароль") # Поле ввода пароля
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa") #Кнопка "Войти"
    ORDER_BUTTON = (By.XPATH, "//*[@id='root']/div/main/section[2]/div/button") #Кнопка "Оформить заказ"
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться") #Линк-текст "Зарегистрироваться"
    EMAIL_LABEL = (By.XPATH, "//label[contains(text(), 'Email')]") #Плейсхолдер почти
    LOGIN_LINK = (By.LINK_TEXT, "Войти") #Линк-текст Войти
    LINK_RESET_PASS = (By.LINK_TEXT, "Восстановить пароль") #Линк-текст "Восстановиться пароль"

class RegistrationPageLocators:
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]") #Линк-текст "Зарегистрироваться"
    EMAIL_INPUT = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input") #Поле ввода почты
    NAME_INPUT = (By.NAME, "name") #Поле ввода имени
    PASSWORD_INPUT = (By.NAME, "Пароль") #Поле ввода пароля
    LOGIN_BUTTON = (By. XPATH, "//button[contains(text(),'Войти')]") #Кнопка Зарегистрироваться
    EMAIL_LABEL = (By.XPATH, "//label[contains(text(), 'Email')]") #Плейсхолдер почты
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться") #Линк-текст Зарегистрироваться

class ConstructorPageLocators:
    LOGO_HEADER = (By. CSS_SELECTOR, "#root > div > header > nav > div > a") #Логотип
    SIGN_OUT_BUTTON = (By. XPATH, "//button[contains(text(), 'Выход')]") #Кнопка Выйти
    CONSTRUCTOR_BUTTON = (By. CSS_SELECTOR, "#root > div > header > nav > ul > li:nth-child(1) > a > svg") #Кнопка конструктора
    MENU_CONTAINER = (By. XPATH, "//*[@id='root']/div/main/section[1]/div[2]") #Контейнер с меню
    SOUSI_TAB = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[2]") #Таб Соусы
    BULKI_TAB = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[1]") #Таб Булки
    NACHINKI_TAB = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[3]") #Таб Начинки

















