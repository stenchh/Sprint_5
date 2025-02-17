import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_click_on_logo(login_google):
    login_google.find_element(By.XPATH, "//*[@id='root']/div/header/nav/a").click()
    WebDriverWait(login_google, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/main/div/div/div/div/button[2]"))) #Кнопка "Сохранить"

    login_google.find_element(By.XPATH, "//*[@id='root']/div/header/nav/div/a").click() #Логотип
    WebDriverWait(login_google, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]"))) #Кнопка "Оформить заказ"

def test_click_on_logo(login_mozilla):
    login_mozilla.find_element(By.XPATH, "//*[@id='root']/div/header/nav/a").click()
    WebDriverWait(login_mozilla, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/main/div/div/div/div/button[2]"))) #Кнопка "Сохранить"

    login_mozilla.find_element(By.XPATH, "//*[@id='root']/div/header/nav/div/a").click() #Логотип
    WebDriverWait(login_mozilla, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]"))) #Кнопка "Оформить заказ"