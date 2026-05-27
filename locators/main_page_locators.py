from selenium.webdriver.common.by import By


class MainPageLocators:
    constructor_tab = (
        By.XPATH,
        "//p[normalize-space()='Конструктор']/ancestor::a"
    )

    feed_tab = (
        By.XPATH,
        "//p[normalize-space()='Лента Заказов']/ancestor::a | //a[contains(@href, '/feed')]"
    )

    profile_button = (
        By.XPATH,
        "//a[contains(@href, '/account')]"
    )

    ingredient_card = (
        By.XPATH,
        "(//a[contains(@href, '/ingredient/')])[1]"
    )

    ingredient_details_popup = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]"
    )

    close_popup_button = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//button"
    )

    bun_ingredient = (
        By.XPATH,
        "(//a[contains(@href, '/ingredient/')])[1]"
    )

    constructor_bun_counter = (
        By.XPATH,
        "((//a[contains(@href, '/ingredient/')])[1]//p[contains(@class, 'counter_counter__num')])[1]"
    )

    constructor_drop_area = (
        By.XPATH,
        "//section[contains(., 'Соберите бургер')]"
    )

    create_order_button = (
        By.XPATH,
        "//button[contains(., 'Оформить заказ')]"
    )

    order_number = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//*[contains(@class, 'text_type_digits-large')]"
    )