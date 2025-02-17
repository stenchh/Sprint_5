import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_main_page_sousi(browser_google):
    driver = browser_google
    element = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/h2[2]") #Раздел Соусы
    driver.execute_script("arguments[0].scrollIntoView();", element)

def test_main_page_bulki(browser_google):
    driver = browser_google
    element = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/h2[1]") #Раздел Булки
    driver.execute_script("arguments[0].scrollIntoView();", element)

def test_main_page_nachinki(browser_google):
    driver = browser_google
    element = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/h2[3]") #Раздел Начинка
    driver.execute_script("arguments[0].scrollIntoView();", element)

def test_main_page_sousi(browser_mozilla):
    driver = browser_mozilla
    element = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/h2[2]") #Раздел Соусы
    driver.execute_script("arguments[0].scrollIntoView();", element)

def test_main_page_bulki(browser_mozilla):
    driver = browser_mozilla
    element = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/h2[1]") #Раздел Булки
    driver.execute_script("arguments[0].scrollIntoView();", element)

def test_main_page_nachinki(browser_mozilla):
    driver = browser_mozilla
    element = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/h2[3]") #Раздел Начинка
    driver.execute_script("arguments[0].scrollIntoView();", element)