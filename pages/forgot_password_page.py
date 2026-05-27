from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators


class ForgotPasswordPage(BasePage):
    def enter_email(self, email):
        self.add_text_to_element(ForgotPasswordPageLocators.email_input, email)

    def click_restore_button(self):
        self.click_element(ForgotPasswordPageLocators.restore_button)

    def click_password_eye_button(self):
        self.click_element(ForgotPasswordPageLocators.password_eye_button)

    def is_forgot_password_page_opened(self):
        return self.is_element_visible(ForgotPasswordPageLocators.email_input)

    def is_reset_password_page_opened(self):
        return self.is_element_visible(ForgotPasswordPageLocators.reset_password_title)

    def is_active_password_field(self):
        field_type = self.get_attribute(
            ForgotPasswordPageLocators.password_input,
            "type"
        )
        return field_type == "text"