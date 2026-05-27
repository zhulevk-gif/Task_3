from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def _get_wait(self, timeout=15):
        return WebDriverWait(self.driver, timeout)

    def open_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def get_page_source(self):
        return self.driver.page_source

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def current_url_contains(self, text):
        return text in self.get_current_url()

    def current_url_contains_any(self, parts):
        return any(self.current_url_contains(part) for part in parts)

    def is_text_in_page_source(self, text):
        return text in self.get_page_source()

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_all_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def is_element_visible(self, locator, timeout=5):
        try:
            self._get_wait(timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_invisibility(self, locator, timeout=10):
        try:
            self._get_wait(timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_element_invisible(self, locator, timeout=10):
        return self.wait_for_invisibility(locator, timeout)

    def wait_for_url_contains(self, text, timeout=15):
        try:
            self._get_wait(timeout).until(EC.url_contains(text))
            return True
        except TimeoutException:
            return False

    def wait_for_url_not_contains(self, text, timeout=15):
        try:
            self._get_wait(timeout).until(
                lambda driver: text not in driver.current_url
            )
            return True
        except TimeoutException:
            return False

    def wait_for_any_url_contains(self, parts, timeout=15):
        try:
            self._get_wait(timeout).until(
                lambda driver: any(part in driver.current_url for part in parts)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_text_in_page_source(self, text, timeout=15):
        try:
            self._get_wait(timeout).until(
                lambda driver: text in driver.page_source
            )
            return True
        except TimeoutException:
            return False

    def wait_for_text_in_element(self, locator, text, timeout=15):
        try:
            self._get_wait(timeout).until(
                lambda driver: text in driver.find_element(*locator).text
            )
            return True
        except TimeoutException:
            return False

    def wait_for_numeric_text_at_least(self, locator, min_value, timeout=15):
        try:
            self._get_wait(timeout).until(
                lambda driver: self._to_int(driver.find_element(*locator).text) >= min_value
            )
            return True
        except TimeoutException:
            return False

    def wait_overlay_to_disappear(self):
        self.wait_for_invisibility(BasePageLocators.overlay, timeout=10)

    def scroll_into_view(self, element):
        self.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
            element
        )

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.scroll_into_view(element)
        return element

    def click_element(self, locator):
        self.wait_overlay_to_disappear()
        element = self.find_clickable_element(locator)
        self.scroll_into_view(element)

        try:
            element.click()
        except (ElementClickInterceptedException, StaleElementReferenceException, TimeoutException):
            self.wait_overlay_to_disappear()
            element = self.find_element(locator)
            self.execute_script("arguments[0].click();", element)

    def fill_input(self, locator, text):
        self.wait_overlay_to_disappear()
        element = self.find_element(locator)
        self.scroll_into_view(element)

        self.execute_script("""
            const element = arguments[0];
            const value = arguments[1];

            element.focus();
            const nativeInputValueSetter =
                Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
            nativeInputValueSetter.call(element, value);

            element.dispatchEvent(new Event('input', { bubbles: true }));
            element.dispatchEvent(new Event('change', { bubbles: true }));
            element.blur();
        """, element, text)

    def add_text_to_element(self, locator, text):
        self.fill_input(locator, text)

    def get_text_from_element(self, locator):
        return self.find_element(locator).text

    def get_numeric_text_from_element(self, locator):
        return self._to_int(self.get_text_from_element(locator))

    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    def drag_and_drop_element_with_script(self, source_locator, target_locator):
        self.wait_overlay_to_disappear()
        source = self.scroll_to_element(source_locator)
        target = self.scroll_to_element(target_locator)

        try:
            ActionChains(self.driver).drag_and_drop(source, target).perform()
        except Exception:
            self.execute_script("""
                const source = arguments[0];
                const target = arguments[1];
                const dataTransfer = new DataTransfer();

                source.dispatchEvent(new DragEvent('dragstart', {
                    bubbles: true,
                    dataTransfer: dataTransfer
                }));

                target.dispatchEvent(new DragEvent('dragover', {
                    bubbles: true,
                    dataTransfer: dataTransfer
                }));

                target.dispatchEvent(new DragEvent('drop', {
                    bubbles: true,
                    dataTransfer: dataTransfer
                }));

                source.dispatchEvent(new DragEvent('dragend', {
                    bubbles: true,
                    dataTransfer: dataTransfer
                }));
            """, source, target)

    @staticmethod
    def _to_int(value):
        digits = "".join(symbol for symbol in str(value) if symbol.isdigit())
        return int(digits) if digits else 0