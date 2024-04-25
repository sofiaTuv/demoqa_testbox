from selenium.webdriver.common.by import By


class Path:
    FULL_NAME = (By.XPATH, '//input[@id="userName"]')
    EMAIL = (By.XPATH, '//input[@id="userEmail"]')
    CURRENT_ADDRESS = (By.XPATH, '//textarea[@id="currentAddress"]')
    PERMANENT_ADDRESS = (By.XPATH, '//textarea[@id="permanentAddress"]')
    SUBMIT = (By.XPATH, '//button[@id="submit"]')
    CHECK_NAME = (By.CSS_SELECTOR, '#name')
    CHECK_EMAIL = (By.CSS_SELECTOR, '#email')
    CHECK_CUR_ADDRESS = (By.CSS_SELECTOR, '#currentAddress')
    CHECK_PER_ADDRESS = (By.CSS_SELECTOR, '#permanentAddress')
