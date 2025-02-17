import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_register_google(browser_google,auth_data):
    driver = browser_google
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click() # Кнопка войти
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, "Зарегистрироваться"))) #Линк-текст "Зарегистрироваться"

    driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Email')]"))) #Плейсхолдер почты

    driver.find_element(By.NAME, "name").send_keys("Елена") #Поле ввода имени
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys(auth_data['email']) #Поле ввода почты
    driver.find_element(By.NAME, "Пароль").send_keys(auth_data["password"]) #Поле ввода пароля

    driver.find_element(By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]").click() #Кнопка регистрации

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By. XPATH, "//button[contains(text(),'Войти')]"))) #Кнопка Войти

def test_register_google_with_empty_name(browser_google,auth_data):
    driver = browser_google
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click() # Кнопка войти
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, "Зарегистрироваться"))) #Линк-текст "Зарегистрироваться"

    driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Email')]"))) #Плейсхолдер почты

    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys(auth_data['email']) #Поле ввода почты
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(auth_data['password']) #Поле ввода пароля

    driver.find_element(By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]").click()  #Кнопка регистрации

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Войти')]"))) #Кнопка Войти

def test_register_google_with_len_password_5(browser_google,auth_data):
    driver = browser_google
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click() # Кнопка войти
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, "Зарегистрироваться"))) #Линк-текст "Зарегистрироваться"

    driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Email')]"))) #Плейсхолдер почты

    driver.find_element(By.NAME, "name").send_keys("Елена") #Поле ввода имени
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys(auth_data['email']) #Поле ввода почты
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys('12345') #Поле ввода пароля

    driver.find_element(By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]").click()  #Кнопка регистрации

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Войти')]"))) #Кнопка Войти

def test_register_google_with_email_without_at_symbol(browser_google,auth_data):
    driver = browser_google
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click() # Кнопка войти
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, "Зарегистрироваться"))) #Линк-текст "Зарегистрироваться"

    driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Email')]"))) #Плейсхолдер почты

    driver.find_element(By.NAME, "name").send_keys("Елена") #Поле ввода имени
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys('shagova123.com') #Поле ввода почты
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys('12345') #Поле ввода пароля

    driver.find_element(By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]").click()  #Кнопка регистрации

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Войти')]"))) #Кнопка Войти

def test_register_mozilla(browser_mozilla,auth_data):
    driver = browser_mozilla
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click() # Кнопка войти
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, "Зарегистрироваться"))) #Линк-текст "Зарегистрироваться"

    driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Email')]"))) #Плейсхолдер почты

    driver.find_element(By.NAME, "name").send_keys("Елена") #Поле ввода имени
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys(auth_data['email']) #Поле ввода почты
    driver.find_element(By.NAME, "Пароль").send_keys(auth_data["password"]) #Поле ввода пароля

    driver.find_element(By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]").click() #Кнопка регистрации

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By. XPATH, "//button[contains(text(),'Войти')]"))) #Кнопка Войти

def test_register_with_empty_name(browser_mozilla,auth_data):
    driver = browser_mozilla
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click() # Кнопка войти
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, "Зарегистрироваться"))) #Линк-текст "Зарегистрироваться"

    driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Email')]"))) #Плейсхолдер почты

    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys(auth_data['email']) #Поле ввода почты
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(auth_data['password']) #Поле ввода пароля

    driver.find_element(By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]").click()  #Кнопка регистрации

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Войти')]"))) #Кнопка Войти

def test_register_with_len_password_5(browser_mozilla,auth_data):
    driver = browser_mozilla
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click() # Кнопка войти
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, "Зарегистрироваться"))) #Линк-текст "Зарегистрироваться"

    driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Email')]"))) #Плейсхолдер почты

    driver.find_element(By.NAME, "name").send_keys("Елена") #Поле ввода имени
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys(auth_data['email']) #Поле ввода почты
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys('12345') #Поле ввода пароля

    driver.find_element(By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]").click()  #Кнопка регистрации

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Войти')]"))) #Кнопка Войти

def test_register_with_email_without_at_symbol(browser_mozilla,auth_data):
    driver = browser_mozilla
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click() # Кнопка войти
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, "Зарегистрироваться"))) #Линк-текст "Зарегистрироваться"

    driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()

    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Email')]"))) #Плейсхолдер почты

    driver.find_element(By.NAME, "name").send_keys("Елена") #Поле ввода имени
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys('shagova123.com') #Поле ввода почты
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys('12345') #Поле ввода пароля

    driver.find_element(By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]").click()  #Кнопка регистрации

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Войти')]"))) #Кнопка Войти








