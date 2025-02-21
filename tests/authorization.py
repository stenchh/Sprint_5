import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators

class TestAuthorization:

    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_auth_through_enter_the_account_button(self, browser, auth_data):
        driver = browser
        driver.find_element(*LoginPageLocators.ENTER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(auth_data['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(auth_data['password'])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON))
        assert driver.find_element(*LoginPageLocators.ORDER_BUTTON).is_displayed()

    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_auth_through_enter_the_personal_account_button(self, browser, auth_data):
        driver = browser
        driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(auth_data['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(auth_data['password'])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON))
        assert driver.find_element(*LoginPageLocators.ORDER_BUTTON).is_displayed()

    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_auth_through_link_already_have_account(self, browser, auth_data):
        driver = browser
        driver.find_element(*LoginPageLocators.ENTER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginPageLocators.REGISTER_LINK))

        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_LABEL))
        driver.find_element(*LoginPageLocators.LOGIN_LINK).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(auth_data['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(auth_data['password'])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON)
        )
        assert driver.find_element(*LoginPageLocators.ORDER_BUTTON).is_displayed()

    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_auth_through_link_forget_the_password(self, browser, auth_data):
        driver = browser
        driver.find_element(*LoginPageLocators.ENTER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginPageLocators.LINK_RESET_PASS))

        driver.find_element(*LoginPageLocators.LINK_RESET_PASS).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_LABEL))
        driver.find_element(*LoginPageLocators.LOGIN_LINK).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(auth_data['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(auth_data['password'])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON)
        )
        assert driver.find_element(*LoginPageLocators.ORDER_BUTTON).is_displayed()


