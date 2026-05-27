from selenium.webdriver.common.by import By


class BasePageLocators:
    overlay = (
        By.XPATH,
        "//*[contains(@class, 'Modal_modal_overlay')]"
    )