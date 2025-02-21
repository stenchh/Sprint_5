import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorPageLocators


class TestsActivityOfTabsConstructor:

    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_tab_main_page_sousi(self, browser):
        driver = browser
        tab_sousi = driver.find_element(*ConstructorPageLocators.SOUSI_TAB)
        tab_sousi.click()


        assert "tab_tab_type_current__2BEPc" in tab_sousi.get_attribute("class")



    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_tab_main_page_bulki(self, browser):
        driver = browser

        tab_bulki = driver.find_element(*ConstructorPageLocators.BULKI_TAB)
        tab_bulki.click()


        assert "tab_tab_type_current__2BEPc" in tab_bulki.get_attribute("class")




    @pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
    def test_tab_main_page_nachinki(self, browser):
        driver = browser
        tab_nachinki = driver.find_element(*ConstructorPageLocators.NACHINKI_TAB)
        tab_nachinki.click()

        assert "tab_tab_type_current__2BEPc" in tab_nachinki.get_attribute("class")

