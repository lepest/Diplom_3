import allure

from data import TestUrl, TestData
from pages.main_page import MainPage
from pages.user_page import UserPage

class TestMainPage:

    @allure.title('Переход по клику на "Конструктор"')
    def test_constructor(self, driver):
        main_page = MainPage(driver)
        assert main_page.constructor() == TestUrl.main_page_url

    @allure.title('Переход по клику на "Лента заказов"')
    def test_order_feed(self, driver):
        main_page = MainPage(driver)
        assert main_page.order_feed()

    @allure.title('Появление окна с деталями при клике на ингредиент')
    def test_click_ingredient(self, driver):
        main_page = MainPage(driver)
        assert main_page.click_ingredient()

    @allure.title('Всплывающее окно закрывается по клику')
    def test_close_popup_window(self, driver):
        main_page = MainPage(driver)
        assert main_page.close_popup_window() == TestData.popup_window

    @allure.title('Увеличение каунтера ингредиента при добавлении в заказ')
    def test_increase_count_ingredient(self, driver):
        main_page = MainPage(driver)
        assert main_page.increase_count_ingredient() == '2'

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_authorized_user_and_order(self, driver):
        main_page = MainPage(driver)
        user_page = UserPage(driver)
        user_page.enter_login_to_account()
        assert main_page.authorized_user_and_order() == TestData.order_placed