from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    PAGE_URL = "https://demoqa.com/text-box"

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(self.PAGE_URL)

    def wait(self, path):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(path))
        return self.browser.find_element(*path)


