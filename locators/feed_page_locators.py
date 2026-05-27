from selenium.webdriver.common.by import By


class FeedPageLocators:
    first_order = (
        By.XPATH,
        "(//a[contains(@href, '/feed/')])[1]"
    )

    order_popup = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]"
    )

    total_done_counter = (
        By.XPATH,
        "//*[contains(text(), 'Выполнено за все время')]/following-sibling::*[1]"
    )

    today_done_counter = (
        By.XPATH,
        "//*[contains(text(), 'Выполнено за сегодня')]/following-sibling::*[1]"
    )

    in_work_block = (
        By.XPATH,
        "//*[contains(text(), 'В работе')]/following-sibling::*[1]"
    )