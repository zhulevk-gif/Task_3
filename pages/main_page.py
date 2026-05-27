from urllib.parse import urlsplit

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import BASE_URL


class MainPage(BasePage):
    def _base_url(self):
        parts = urlsplit(self.driver.current_url)
        return f"{parts.scheme}://{parts.netloc}/"

    def open(self):
        self.driver.get(BASE_URL)

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
        except Exception:
            pass

        if "/login" in self.driver.current_url or "/account" in self.driver.current_url:
            return

        self.driver.get(self._base_url() + "account")
        WebDriverWait(self.driver, 15).until(
            lambda driver: "/login" in driver.current_url
            or "/account" in driver.current_url
        )

    def is_constructor_tab_opened(self):
        return self.is_element_visible(MainPageLocators.constructor_tab)

    def is_feed_page_opened(self):
        return "/feed" in self.driver.current_url

    def click_ingredient_card(self):
        self.click_element(MainPageLocators.ingredient_card)

    def open_ingredient_popup(self):
        self.click_ingredient_card()

    def close_popup(self):
        self.click_element(MainPageLocators.close_popup_button)

    def is_ingredient_popup_opened(self):
        return self.is_element_visible(MainPageLocators.ingredient_details_popup)

    def wait_for_ingredient_popup_closed(self):
        return self.wait_for_element_invisible(MainPageLocators.ingredient_details_popup)

    def is_ingredient_popup_closed(self):
        return not self.is_element_visible(MainPageLocators.ingredient_details_popup, timeout=3)

    def get_ingredient_counter_value(self, locator):
        if self.is_element_visible(locator, timeout=3):
            return self.get_text_from_element(locator)
        return "0"

    def get_bun_counter_value(self):
        return int(self.get_ingredient_counter_value(MainPageLocators.constructor_bun_counter))

    def drag_ingredient_to_constructor(self, source_locator):
        self.drag_and_drop_element_with_script(
            source_locator,
            MainPageLocators.constructor_drop_area
        )

    def add_bun_to_constructor(self):
        self.drag_ingredient_to_constructor(MainPageLocators.bun_ingredient)

    def click_order_button(self):
        self.click_element(MainPageLocators.create_order_button)

    def get_order_number(self):
        try:
            WebDriverWait(self.driver, 15).until(
                lambda driver: self.is_element_visible(MainPageLocators.order_number, timeout=1)
            )
            order_number = self.get_text_from_element(MainPageLocators.order_number).strip()
        except TimeoutException:
            raise AssertionError("Order number popup was not opened or number was not found")

        if not order_number or not order_number.isdigit():
            raise AssertionError(f"Incorrect order number received: {order_number}")

        return order_number

    def is_order_button_visible(self):
        return self.is_element_visible(MainPageLocators.create_order_button)

    def is_order_created(self):
        try:
            return self.get_order_number() != ""
        except AssertionError:
            return False