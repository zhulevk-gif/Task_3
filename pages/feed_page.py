from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):
    def click_first_order(self):
        self.click_element(FeedPageLocators.first_order)

    def is_order_popup_opened(self):
        return self.is_element_visible(FeedPageLocators.order_popup)

    def get_total_done_counter(self):
        return self.get_text_from_element(FeedPageLocators.total_done_counter)

    def get_today_done_counter(self):
        return self.get_text_from_element(FeedPageLocators.today_done_counter)

    def get_in_work_text(self):
        return self.get_text_from_element(FeedPageLocators.in_work_block)

    def wait_for_total_counter_change(self, old_value):
        try:
            self.wait.until(
                lambda driver: int(self.get_total_done_counter()) >= old_value
            )
        except TimeoutException:
            pass

    def wait_for_today_counter_change(self, old_value):
        try:
            self.wait.until(
                lambda driver: int(self.get_today_done_counter()) >= old_value
            )
        except TimeoutException:
            pass

    def wait_for_order_in_work(self, order_number):
        try:
            self.wait.until(
                lambda driver: order_number in driver.page_source
            )
        except TimeoutException:
            pass