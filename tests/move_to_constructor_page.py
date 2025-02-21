import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators
from locators import ConstructorPageLocators

class TestMovingToConstructorPage:
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_click_on_constructor_move_constructor_page(self, browser, login):
        driver = browser
        driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ConstructorPageLocators.SIGN_OUT_BUTTON))

        driver.find_element(*ConstructorPageLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ConstructorPageLocators.MENU_CONTAINER))

        assert driver.find_element(*ConstructorPageLocators.MENU_CONTAINER).is_displayed()

