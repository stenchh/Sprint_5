import random
import string
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators


@pytest.fixture
def auth_data():
    return {
        "email": "elenashagova14764@yandex.ru",
        "password": "123456"
    }

@pytest.fixture
def generate_email():
    domains = ["gmail.com", "yandex.ru", "mail.ru"]
    login = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return f"{login}@{random.choice(domains)}"


@pytest.fixture
def generate_password():
    def _generate():
        length = random.randint(6, 12)
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choices(characters, k=length))

    return _generate

@pytest.fixture(params=["chrome", "firefox"])  # Параметризуем фикстуру для Chrome и Firefox
def browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")  # Открываем сайт
    yield driver
    driver.quit()


@pytest.fixture
def login(browser, auth_data):
    driver = browser

    driver.find_element(*LoginPageLocators.ENTER_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))

    driver.find_element(By.NAME, "name").send_keys(auth_data['email'])
    driver.find_element(By.NAME, "Пароль").send_keys(auth_data['password'])

    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON))


    return driver



