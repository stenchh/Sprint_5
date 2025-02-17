import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_auth_through_enter_the_account_button(browser_google,auth_data):
    driver = browser_google
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[2]/div/button").click() #Кнопка "Войти в аккаунт"
    driver.find_element(By.NAME, "name").send_keys(auth_data['email']) #Поле ввода почты
    driver.find_element(By.NAME, "Пароль").send_keys(auth_data['password']) #Поле ввода пароля
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button").click() #Кнопка "Войти"

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]"))) #Кнопка "Оформить заказ"

def test_auth_through_enter_the_personal_account_button(browser_google,auth_data):
    driver = browser_google
    driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click() #Кнопка "Личный кабинет"

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input"))) #Поле ввода почты

    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys(auth_data['email']) #Поле ввода почты
    driver.find_element(By.NAME, "Пароль").send_keys(auth_data['password']) #Поле ввода пароля
    driver.find_element(By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa").click() #Кнопка "Войти"

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]"))) #Кнопка "Оформить заказ"

def test_auth_through_link_already_have_account(browser_google,auth_data):
    driver = browser_google
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, "Зарегистрироваться"))) #Линк-текст Зарегистрироваться

    driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Email')]")))

    driver.find_element(By.LINK_TEXT, "Войти").click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Email')]")))

    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys(auth_data['email']) #Поле ввода почты
    driver.find_element(By.NAME, "Пароль").send_keys(auth_data['password']) #Поле ввода пароля
    driver.find_element(By.CSS_SELECTOR,"button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa").click() #Кнопка "Войти"

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]"))) #Кнопка "Оформить заказ"

def test_auth_through_link_forget_password(browser_google,auth_data):
    driver = browser_google
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, "Восстановить пароль"))) #Линк-текст "Восстановить пароль"

    driver.find_element(By.LINK_TEXT, "Восстановить пароль").click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='root']/div/main/div/form/fieldset/div/div/input"))) #Поле ввода Почты

    driver.find_element(By.LINK_TEXT, 'Войти').click() #Линк-текст Войти

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")))
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys(auth_data['email']) #Поле ввода почты
    driver.find_element(By.NAME, "Пароль").send_keys(auth_data['password']) #Поле ввода пароля
    driver.find_element(By.CSS_SELECTOR,"button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa").click() #Кнопка "Войти"

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]"))) #Кнопка "Оформить заказ"


def test_auth_through_enter_the_account_button(browser_mozilla,auth_data):
    driver = browser_mozilla
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[2]/div/button").click() #Кнопка "Войти в аккаунт"
    driver.find_element(By.NAME, "name").send_keys(auth_data['email']) #Поле ввода почты
    driver.find_element(By.NAME, "Пароль").send_keys(auth_data['password']) #Поле ввода пароля
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button").click() #Кнопка "Войти"

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]"))) #Кнопка "Оформить заказ"

def test_auth_through_enter_the_personal_account_button(browser_mozilla,auth_data):
    driver = browser_mozilla
    driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click() #Кнопка "Личный кабинет"

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input"))) #Поле ввода почты

    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys(auth_data['email']) #Поле ввода почты
    driver.find_element(By.NAME, "Пароль").send_keys(auth_data['password']) #Поле ввода пароля
    driver.find_element(By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa").click() #Кнопка "Войти"

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]"))) #Кнопка "Оформить заказ"

def test_auth_through_link_already_have_account(browser_mozilla,auth_data):
    driver = browser_mozilla
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, "Зарегистрироваться"))) #Линк-текст Зарегистрироваться

    driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Email')]")))

    driver.find_element(By.LINK_TEXT, "Войти").click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Email')]")))

    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys(auth_data['email']) #Поле ввода почты
    driver.find_element(By.NAME, "Пароль").send_keys(auth_data['password']) #Поле ввода пароля
    driver.find_element(By.CSS_SELECTOR,"button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa").click() #Кнопка "Войти"

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]"))) #Кнопка "Оформить заказ"

def test_auth_through_link_forget_password(browser_mozilla,auth_data):
    driver = browser_mozilla
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Восстановить пароль")))  # Линк-текст "Восстановить пароль"

    driver.find_element(By.LINK_TEXT, "Восстановить пароль").click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset/div/div/input")))  # Поле ввода Почты

    driver.find_element(By.LINK_TEXT, 'Войти').click()  # Линк-текст Войти

    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")))
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys(
        auth_data['email'])  # Поле ввода почты
    driver.find_element(By.NAME, "Пароль").send_keys(auth_data['password'])  # Поле ввода пароля
    driver.find_element(By.CSS_SELECTOR,
                        "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa").click()  # Кнопка "Войти"

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        (By.XPATH, "//button[contains(text(),'Оформить заказ')]")))  # Кнопка "Оформить заказ"

