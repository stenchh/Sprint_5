from selenium.webdriver.common.by import By

class LoginPageLocators:
    ENTER_ACCOUNT_BUTTON = (By.XPATH, "//*[@id='root']/div/main/section[2]/div/button")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    EMAIL_INPUT = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")
    ORDER_BUTTON = (By.XPATH, "//*[@id='root']/div/main/section[2]/div/button")
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")
    EMAIL_LABEL = (By.XPATH, "//label[contains(text(), 'Email')]")
    LOGIN_LINK = (By.LINK_TEXT, "Войти")
    LINK_RESET_PASS = (By.LINK_TEXT, "Восстановить пароль")

class RegistrationPageLocators:
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    EMAIL_INPUT = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")
    NAME_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOGIN_BUTTON = (By. XPATH, "//button[contains(text(),'Войти')]")
    EMAIL_LABEL = (By.XPATH, "//label[contains(text(), 'Email')]")
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")

class ConstructorPageLocators:
    LOGO_HEADER = (By. CSS_SELECTOR, "#root > div > header > nav > div > a")
    SIGN_OUT_BUTTON = (By. XPATH, "//button[contains(text(), 'Выход')]")
    CONSTRUCTOR_BUTTON = (By. CSS_SELECTOR, "#root > div > header > nav > ul > li:nth-child(1) > a > svg")
    MENU_CONTAINER = (By. XPATH, "//*[@id='root']/div/main/section[1]/div[2]")
    SOUSI_TAB = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[2]")
    BULKI_TAB = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[1]")
    NACHINKI_TAB = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[3]")

















