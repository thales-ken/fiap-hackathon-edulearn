from test_cases.base_test import BaseTest
from page_objects.login_page import LoginPage


class LoginPageTest(BaseTest):
    def test_login_with_valid_user(self):
        login_page = LoginPage(self.driver)
        login_page.login_with_valid_credentials()
        self.assertIn("/dashboard", self.driver.current_url)

    def test_login_with_invalid_user(self):
        login_page = LoginPage(self.driver)
        result = login_page.login_with_invalid_credentials()
        self.assertIn("Failed to login. Please check your credentials.", result)
