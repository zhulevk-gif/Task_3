from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):
    def open_order_history(self):
        if not self.current_url_contains("/account"):
            raise AssertionError("Account page is not opened")

        self.click_element(ProfilePageLocators.order_history_button)

        if not self.wait_for_url_contains("/account/order-history", timeout=15):
            raise AssertionError("Order history page was not opened")

    def click_logout_button(self):
        if not self.current_url_contains("/account"):
            raise AssertionError("Account page is not opened")

        self.click_element(ProfilePageLocators.logout_button)

        if not self.wait_for_url_contains("/login", timeout=15):
            raise AssertionError("Login page was not opened after logout")

    def is_profile_page_opened(self):
        return (
            self.current_url_contains("/account")
            and self.is_element_visible(ProfilePageLocators.profile_title, timeout=5)
        )

    def is_order_history_opened(self):
        return (
            self.current_url_contains("/account/order-history")
            and self.is_element_visible(ProfilePageLocators.order_history_title, timeout=5)
        )