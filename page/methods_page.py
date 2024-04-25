from page.base_page import BasePage
from page.paths import Path


class MethodsPage(BasePage):

    def enter_full_name(self, text):
        self.send_keys_element(Path.FULL_NAME, text)

    def enter_email(self, text):
        self.send_keys_element(Path.EMAIL, text)

    def enter_current_address(self, text):
        self.send_keys_element(Path.CURRENT_ADDRESS, text)

    def enter_permanent_address(self, text):
        self.send_keys_element(Path.PERMANENT_ADDRESS, text)

    def click_submit(self):
        self.click_element(Path.SUBMIT)

    def get_name_text(self):
        return self.wait(Path.CHECK_NAME).text

    def get_email_text(self):
        return self.wait(Path.CHECK_EMAIL).text

    def get_current_address(self):
        return self.wait(Path.CHECK_CUR_ADDRESS).get_attribute('value')

    def get_permanent_address(self):
        return self.wait(Path.CHECK_PER_ADDRESS).get_attribute('value')
