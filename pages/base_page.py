from selenium.common.exceptions import (
    ElementClickInterceptedException,
    TimeoutException,
    StaleElementReferenceException,
)
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    OVERLAY = (
        "xpath",
        "//*[contains(@class, 'Modal_modal_overlay')]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_all_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def is_element_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_invisibility(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_element_invisible(self, locator, timeout=10):
        return self.wait_for_invisibility(locator, timeout)

    def wait_overlay_to_disappear(self):
        self.wait_for_invisibility(self.OVERLAY, timeout=10)

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
            element
        )
        return element

    def click_element(self, locator):
        self.wait_overlay_to_disappear()
        element = self.find_clickable_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
            element
        )
        try:
            element.click()
        except (ElementClickInterceptedException, StaleElementReferenceException, TimeoutException):
            self.wait_overlay_to_disappear()
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].click();", element)

    def fill_input(self, locator, text):
        self.wait_overlay_to_disappear()
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
            element
        )
        self.driver.execute_script("""
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

    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    def drag_and_drop_element_with_script(self, source_locator, target_locator):
        self.wait_overlay_to_disappear()
        source = self.scroll_to_element(source_locator)
        target = self.scroll_to_element(target_locator)

        try:
            ActionChains(self.driver).drag_and_drop(source, target).perform()
        except Exception:
            self.driver.execute_script("""
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