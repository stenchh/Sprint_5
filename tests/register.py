import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators

class TestRegistration:

    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_register_with_all_data(self, browser, generate_email, generate_password):
        driver = browser
        email = generate_email
        password = generate_password()

        driver.find_element(*RegistrationPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(RegistrationPageLocators.REGISTER_LINK))

        driver.find_element(*RegistrationPageLocators.REGISTER_LINK).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_LABEL))

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Елена")
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)

        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.LOGIN_BUTTON))
        assert driver.find_element(*RegistrationPageLocators.LOGIN_BUTTON).is_displayed()

    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_register_google_with_empty_name(self, browser, generate_email, generate_password):
        driver = browser
        email = generate_email
        password = generate_password()

        driver.find_element(*RegistrationPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(RegistrationPageLocators.REGISTER_LINK))

        driver.find_element(*RegistrationPageLocators.REGISTER_LINK).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_LABEL))

        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)

        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.LOGIN_BUTTON))
        assert driver.find_element(*RegistrationPageLocators.LOGIN_BUTTON).is_displayed()

    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_register_google_with_len_password_5(self, browser, generate_email):
        driver = browser
        email = generate_email

        driver.find_element(*RegistrationPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(RegistrationPageLocators.REGISTER_LINK))

        driver.find_element(*RegistrationPageLocators.REGISTER_LINK).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_LABEL))

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Елена")
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys('12345')

        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.LOGIN_BUTTON))
        assert driver.find_element(*RegistrationPageLocators.LOGIN_BUTTON).is_displayed()

    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_register_google_with_email_without_at_symbol(self, browser):
        driver = browser

        driver.find_element(*RegistrationPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(RegistrationPageLocators.REGISTER_LINK))

        driver.find_element(*RegistrationPageLocators.REGISTER_LINK).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_LABEL))

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Елена")
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys('shagova123.com')
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys('12345')

        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.LOGIN_BUTTON))
        assert driver.find_element(*RegistrationPageLocators.LOGIN_BUTTON).is_displayed()
