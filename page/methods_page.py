from page.base_page import BasePage
from page.paths import Paths


class MethodsPage(BasePage, Paths):

    def enter_full_name(self, text):
        self.wait(self.FULL_NAME).send_keys(text)

    def enter_email(self, text):
        self.wait(self.EMAIL).send_keys(text)

    def enter_current_address(self, text):
        self.wait(self.CURRENT_ADDRESS).send_keys(text)

    def enter_permanent_address(self, text):
        self.wait(self.PERMANENT_ADDRESS).send_keys(text)

    def click_submit(self):
        self.wait(self.SUBMIT).click()

    def get_name_text(self):
        return self.wait(self.CHECK_NAME).text

    def get_email_text(self):
        return self.wait(self.CHECK_EMAIL).text

    def get_current_address(self):
        return self.wait(self.CHECK_CUR_ADDRESS).text

    def get_permanent_address(self):
        return self.wait(self.CHECK_PER_ADDRESS).text