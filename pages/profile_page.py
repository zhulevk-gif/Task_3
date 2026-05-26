from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):
    def open_order_history(self):
        if "/account" not in self.driver.current_url:
            raise AssertionError("Account page is not opened")

        self.click_element(ProfilePageLocators.order_history_button)
        WebDriverWait(self.driver, 15).until(
            lambda driver: "/account/order-history" in driver.current_url
        )

    def click_logout_button(self):
        if "/account" not in self.driver.current_url:
            raise AssertionError("Account page is not opened")

        self.click_element(ProfilePageLocators.logout_button)
        WebDriverWait(self.driver, 15).until(
            EC.url_contains("/login")
        )

    def is_profile_page_opened(self):
        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: "/account" in driver.current_url
            )
            return True
        except TimeoutException:
            return False

    def is_order_history_opened(self):
        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: "/account/order-history" in driver.current_url
            )
            return True
        except TimeoutException:
            return False