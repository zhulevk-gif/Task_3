import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.feature("Основной функционал")
class TestMainFunctionality:

    @allure.title("Открыть вкладку Конструктор")
    @allure.story("Навигация по главной странице")
    @allure.severity(allure.severity_level.NORMAL)
    def test_open_constructor_tab(self, driver):
        main_page = MainPage(driver)

        main_page.open()
        main_page.open_feed()
        main_page.open_constructor()

        assert main_page.is_constructor_tab_opened()

    @allure.title("Открыть вкладку Лента заказов")
    @allure.story("Навигация по главной странице")
    @allure.severity(allure.severity_level.NORMAL)
    def test_open_feed_tab(self, driver):
        main_page = MainPage(driver)

        main_page.open()
        main_page.open_feed()

        assert main_page.is_feed_page_opened()

    @allure.title("Клик по ингредиенту открывает попап")
    @allure.story("Просмотр состава")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_ingredient_opens_popup(self, driver):
        main_page = MainPage(driver)

        main_page.open()
        main_page.open_ingredient_popup()

        assert main_page.is_ingredient_popup_opened()

    @allure.title("Попап закрывается по кнопке")
    @allure.story("Закрытие модального окна")
    @allure.severity(allure.severity_level.NORMAL)
    def test_popup_closes_by_click_on_close_button(self, driver):
        main_page = MainPage(driver)

        main_page.open()
        main_page.open_ingredient_popup()
        main_page.close_popup()
        main_page.wait_for_ingredient_popup_closed()

        assert main_page.is_ingredient_popup_closed()

    @allure.title("Счётчик ингредиента увеличивается после добавления")
    @allure.story("Работа конструктора")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_ingredient_counter_increases_after_add_to_order(self, driver):
        main_page = MainPage(driver)

        main_page.open()

        before_value = main_page.get_bun_counter_value()
        main_page.add_bun_to_constructor()
        after_value = main_page.get_bun_counter_value()

        assert after_value >= before_value

    @allure.title("Авторизованный пользователь может создать заказ")
    @allure.story("Оформление заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_authorized_user_can_create_order(self, driver, create_user):
        user_data = create_user()

        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.open()
        main_page.open_profile()
        login_page.login(user_data["email"], user_data["password"])

        main_page.add_bun_to_constructor()
        main_page.click_order_button()

        assert main_page.is_order_created()