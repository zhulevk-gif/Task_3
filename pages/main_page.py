from urllib.parse import urlsplit

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def _base_url(self):
        parts = urlsplit(self.driver.current_url)
        return f"{parts.scheme}://{parts.netloc}/"

    def open_constructor(self):
        self.click_element(MainPageLocators.constructor_tab)

    def open_feed(self):
        self.click_element(MainPageLocators.feed_tab)

    def open_profile(self):
        self.wait_overlay_to_disappear()

        try:
            self.click_element(MainPageLocators.profile_button)
            WebDriverWait(self.driver, 5).until(
                lambda driver: "/login" in driver.current_url
                or "/account" in driver.current_url
            )
        except TimeoutException:
            pass

        if "/login" in self.driver.current_url or "/account" in self.driver.current_url:
            return

        self.driver.get(self._base_url() + "account")
        WebDriverWait(self.driver, 15).until(
            lambda driver: "/login" in driver.current_url
            or "/account" in driver.current_url
        )

    def click_ingredient_card(self):
        self.click_element(MainPageLocators.ingredient_card)

    def close_popup(self):
        self.click_element(MainPageLocators.close_popup_button)

    def is_ingredient_popup_opened(self):
        return self.is_element_visible(MainPageLocators.ingredient_details_popup)

    def get_ingredient_counter_value(self, locator):
        if self.is_element_visible(locator):
            return self.get_text_from_element(locator)
        return "0"

    def drag_ingredient_to_constructor(self, source_locator):
        self.drag_and_drop_element_with_script(
            source_locator,
            MainPageLocators.constructor_drop_area
        )

    def click_order_button(self):
        self.click_element(MainPageLocators.create_order_button)

    def get_order_number(self):
        return self.get_text_from_element(MainPageLocators.order_number)

    def is_order_button_visible(self):
        return self.is_element_visible(MainPageLocators.create_order_button)