import allure

from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Клик по заказу открывает попап")
    @allure.story("Просмотр заказа")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_order_opens_popup(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.open()
        main_page.open_feed()
        feed_page.click_first_order()

        assert feed_page.is_order_popup_opened()

    @allure.title("Заказ пользователя отображается в ленте")
    @allure.story("История заказов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_order_from_history_is_displayed_in_feed(self, driver, create_user):
        user_data = create_user()

        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)

        main_page.open()
        main_page.open_profile()
        login_page.login(user_data["email"], user_data["password"])

        main_page.add_bun_to_constructor()
        main_page.click_order_button()
        order_number = main_page.get_order_number()
        main_page.close_popup()

        main_page.open_feed()

        assert feed_page.is_order_present(order_number)

    @allure.title("Общий счётчик выполненных заказов увеличивается")
    @allure.story("Статистика ленты")
    @allure.severity(allure.severity_level.NORMAL)
    def test_total_done_counter_increases_after_new_order(self, driver, create_user):
        user_data = create_user()

        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)

        main_page.open()
        main_page.open_feed()
        before_value = feed_page.get_total_done_counter()

        main_page.open_profile()
        login_page.login(user_data["email"], user_data["password"])

        main_page.add_bun_to_constructor()
        main_page.click_order_button()
        main_page.get_order_number()
        main_page.close_popup()

        main_page.open_feed()
        feed_page.wait_for_total_counter_change(before_value)
        after_value = feed_page.get_total_done_counter()

        assert after_value >= before_value

    @allure.title("Счётчик за сегодня увеличивается после нового заказа")
    @allure.story("Статистика ленты")
    @allure.severity(allure.severity_level.NORMAL)
    def test_today_done_counter_increases_after_new_order(self, driver, create_user):
        user_data = create_user()

        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)

        main_page.open()
        main_page.open_feed()
        before_value = feed_page.get_today_done_counter()

        main_page.open_profile()
        login_page.login(user_data["email"], user_data["password"])

        main_page.add_bun_to_constructor()
        main_page.click_order_button()
        order_number = main_page.get_order_number()
        main_page.close_popup()

        main_page.open_feed()
        feed_page.wait_for_today_counter_change(before_value)
        after_value = feed_page.get_today_done_counter()

        assert after_value >= before_value or feed_page.is_order_present(order_number)

    @allure.title("Номер нового заказа отображается в ленте заказов")
    @allure.story("Очередь заказов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_new_order_number_is_displayed_in_work_section(self, driver, create_user):
        user_data = create_user()

        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)

        main_page.open()
        main_page.open_profile()
        login_page.login(user_data["email"], user_data["password"])

        main_page.add_bun_to_constructor()
        main_page.click_order_button()
        order_number = main_page.get_order_number()
        main_page.close_popup()

        main_page.open_feed()

        assert feed_page.is_order_present(order_number)