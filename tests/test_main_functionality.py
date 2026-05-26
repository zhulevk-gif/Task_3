import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage
from locators.main_page_locators import MainPageLocators
from urls import BASE_URL


@allure.feature("Основной функционал")
class TestMainFunctionality:

    @allure.title("Открыть вкладку Конструктор")
    @allure.story("Навигация по главной странице")
    @allure.severity(allure.severity_level.NORMAL)
    def test_open_constructor_tab(self, driver):
        driver.get(BASE_URL)

        main_page = MainPage(driver)

        main_page.open_feed()
        main_page.open_constructor()

        assert main_page.is_element_visible(MainPageLocators.constructor_tab)

    @allure.title("Открыть вкладку Лента заказов")
    @allure.story("Навигация по главной странице")
    @allure.severity(allure.severity_level.NORMAL)
    def test_open_feed_tab(self, driver):
        driver.get(BASE_URL)

        main_page = MainPage(driver)

        main_page.open_feed()

        assert "feed" in driver.current_url

    @allure.title("Клик по ингредиенту открывает попап")
    @allure.story("Просмотр состава")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_ingredient_opens_popup(self, driver):
        driver.get(BASE_URL)

        main_page = MainPage(driver)

        main_page.click_ingredient_card()

        assert main_page.is_element_visible(MainPageLocators.ingredient_details_popup)

    @allure.title("Попап закрывается по кнопке")
    @allure.story("Закрытие модального окна")
    @allure.severity(allure.severity_level.NORMAL)
    def test_popup_closes_by_click_on_close_button(self, driver):
        driver.get(BASE_URL)

        main_page = MainPage(driver)

        main_page.click_ingredient_card()
        main_page.close_popup()
        main_page.wait_for_element_invisible(MainPageLocators.ingredient_details_popup)

        assert not main_page.is_element_visible(MainPageLocators.ingredient_details_popup)

    @allure.title("Счётчик ингредиента увеличивается после добавления")
    @allure.story("Работа конструктора")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_ingredient_counter_increases_after_add_to_order(self, driver):
        driver.get(BASE_URL)

        main_page = MainPage(driver)

        before_value = main_page.get_ingredient_counter_value(MainPageLocators.constructor_bun_counter)
        main_page.drag_ingredient_to_constructor(MainPageLocators.bun_ingredient)
        after_value = main_page.get_ingredient_counter_value(MainPageLocators.constructor_bun_counter)

        assert int(after_value) >= int(before_value)

    @allure.title("Авторизованный пользователь может создать заказ")
    @allure.story("Оформление заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_authorized_user_can_create_order(self, driver, create_user):
        user_data, _ = create_user()

        driver.get(BASE_URL)

        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.open_profile()
        login_page.login(user_data["email"], user_data["password"])

        main_page.drag_ingredient_to_constructor(MainPageLocators.bun_ingredient)
        main_page.click_order_button()

        assert main_page.get_order_number() != ""