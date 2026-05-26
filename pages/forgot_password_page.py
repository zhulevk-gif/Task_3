from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators


class ForgotPasswordPage(BasePage):
    def enter_email(self, email):
        self.add_text_to_element(ForgotPasswordPageLocators.email_input, email)

    def click_restore_button(self):
        self.click_element(ForgotPasswordPageLocators.restore_button)

    def click_password_eye_button(self):
        try:
            self.click_element(ForgotPasswordPageLocators.password_eye_button)
        except TimeoutException:
            password_input = self.find_element(ForgotPasswordPageLocators.password_input)

            self.driver.execute_script(
                """
                const input = arguments[0];
                const rect = input.getBoundingClientRect();
                const clickX = rect.right - 20;
                const clickY = rect.top + rect.height / 2;

                const target = document.elementFromPoint(clickX, clickY);
                if (!target) {
                    return false;
                }

                target.dispatchEvent(new MouseEvent('mousedown', {
                    bubbles: true,
                    clientX: clickX,
                    clientY: clickY
                }));

                target.dispatchEvent(new MouseEvent('mouseup', {
                    bubbles: true,
                    clientX: clickX,
                    clientY: clickY
                }));

                target.dispatchEvent(new MouseEvent('click', {
                    bubbles: true,
                    clientX: clickX,
                    clientY: clickY
                }));

                return true;
                """,
                password_input
            )

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