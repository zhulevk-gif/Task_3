from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from urls import LOGIN_URL


class LoginPage(BasePage):
    def open(self):
        self.open_url(LOGIN_URL)

    def open_forgot_password_page(self):
        self.click_element(LoginPageLocators.forgot_password_link)

    def fill_email(self, email):
        self.fill_input(LoginPageLocators.email_input, email)

    def fill_password(self, password):
        self.fill_input(LoginPageLocators.password_input, password)

    def click_login_button(self):
        self.click_element(LoginPageLocators.login_button)

    def get_login_error_text(self):
        if self.is_element_visible(LoginPageLocators.error_text, timeout=3):
            return self.get_text_from_element(LoginPageLocators.error_text)
        return ""

    def is_login_page_opened(self):
        return self.current_url_contains("/login")

    def login(self, email, password):
        self.fill_email(email)
        self.fill_password(password)

        email_value = self.get_attribute(LoginPageLocators.email_input, "value")
        password_value = self.get_attribute(LoginPageLocators.password_input, "value")

        assert email_value == email, f"Email not filled. Actual value: {email_value}"
        assert password_value == password, f"Password not filled. Actual value: {password_value}"

        self.click_login_button()

        if not self.wait_for_url_not_contains("/login", timeout=10):
            error_text = self.get_login_error_text()
            current_url = self.get_current_url()

            if error_text:
                raise AssertionError(
                    f"Login failed with UI error: {error_text}. Current URL: {current_url}"
                )

            raise AssertionError(
                f"Login was not completed. Current URL: {current_url}"
            )