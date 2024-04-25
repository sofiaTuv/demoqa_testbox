from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    PAGE_URL = "https://demoqa.com/text-box"

    def __init__(self, browser):
        self.browser = browser

    def open_url(self):
        self.browser.get(self.PAGE_URL)

    def wait(self, path):
        return WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(path))

    def click_element(self, path):
        self.wait(path).click()

    def send_keys_element(self, path, text):
        self.wait(path).send_keys(text)