from helper import Helper
from page.methods_page import MethodsPage


class TestDemoQA:
    def test_box(self, browser):
        # ARRANGE
        page = MethodsPage(browser)
        page.open()

        # ACT
        f_name = Helper.generate_name()
        page.enter_full_name(f_name)

        email = Helper.generate_email()
        page.enter_email(email)

        c_address = Helper.generate_address()
        page.enter_current_address(c_address)

        p_address = Helper.generate_address()
        page.enter_permanent_address(p_address)

        page.click_submit()

        # ASSERT
        name_text = page.get_name_text()
        email_text = page.get_email_text()
        c_address_text = page.get_current_address()
        p_address_text = page.get_permanent_address()

        assert f_name in name_text
        assert email in email_text
        assert c_address in c_address_text
        assert p_address in p_address_text




