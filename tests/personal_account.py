import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_personal_account_page_open(login_google):
    login_google.find_element(By.XPATH, "//*[@id='root']/div/header/nav/a").click() #Кнопка "Личный кабинет"
    WebDriverWait(login_google, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[1]/a"))) #Поле изменения имени


def test_personal_account_page_open(login_mozilla):
    login_mozilla.find_element(By.XPATH, "//*[@id='root']/div/header/nav/a").click() #Кнопка "Личный кабинет"
    WebDriverWait(login_mozilla, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[1]/a"))) #Поле изменения имени