from selenium.webdriver.common.by import By


class ProfilePageLocators:
    profile_link = (
        By.XPATH,
        "//a[contains(@href, '/account/profile')]"
    )

    profile_title = (
        By.XPATH,
        "//a[contains(@href, '/account/profile') and contains(normalize-space(), 'Профиль')] | //a[contains(@href, '/account/profile')]"
    )

    order_history_button = (
        By.XPATH,
        "//a[contains(@href, '/account/order-history') and contains(normalize-space(), 'История заказов')] | //a[contains(@href, '/account/order-history')]"
    )

    order_history_title = (
        By.XPATH,
        "//a[contains(@href, '/account/order-history') and contains(@class, 'Account_link_active')] | //a[contains(@href, '/account/order-history')]"
    )

    logout_button = (
        By.XPATH,
        "//button[contains(normalize-space(), 'Выход')]"
    )