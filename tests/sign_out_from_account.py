import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators
from locators import ConstructorPageLocators

class TestSignOutPersonalAccount:
    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_click_on_sign_out_button(self, browser, login):
        driver = browser
        driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ConstructorPageLocators.SIGN_OUT_BUTTON))

        driver.find_element(*ConstructorPageLocators.SIGN_OUT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))

        assert driver.find_element(*LoginPageLocators.EMAIL_INPUT).is_displayed()
