@pytest.fixture
def browser_google():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture
def browser_mozilla():
    driver = webdriver.Firefox()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture
def auth_data():
    return {
        "email": "elenashagova14764@yandex.ru",
        "password": "123456"
    }


@pytest.fixture
def login_google(browser_google, auth_data):
    driver = browser_google

    driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[2]/div/button").click()

    driver.find_element(By.NAME, "name").send_keys(auth_data['email'])
    driver.find_element(By.NAME, "Пароль").send_keys(auth_data['password'])

    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button").click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))

    return driver

@pytest.fixture
def login_mozilla(browser_mozilla, auth_data):
    driver = browser_mozilla

    driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[2]/div/button").click()

    driver.find_element(By.NAME, "name").send_keys(auth_data['email'])
    driver.find_element(By.NAME, "Пароль").send_keys(auth_data['password'])

    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button").click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))

    return driver