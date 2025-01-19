import pytest
import allure

from data import TestUrl
from pages.main_page import MainPage
from pages.user_page import UserPage
from helpers import WebdriverFactory

class TestMainPage:

    @allure.title('Переход по клику на "Конструктор"')
    @pytest.mark.parametrize('browser_name', ['chrome', 'firefox'])
    def test_constructor(self, browser_name):
        driver = WebdriverFactory().web_driver(browser_name)
        main_page = MainPage(driver)
        driver.get(TestUrl.main_page_url)
        assert main_page.constructor() == TestUrl.main_page_url
        driver.quit()

    @allure.title('Переход по клику на "Лента заказов"')
    @pytest.mark.parametrize('browser_name', ['chrome', 'firefox'])
    def test_order_feed(self, browser_name):
        driver = WebdriverFactory().web_driver(browser_name)
        main_page = MainPage(driver)
        driver.get(TestUrl.main_page_url)
        assert main_page.order_feed() == True
        driver.quit()

    @allure.title('Появление окна с деталями при клике на ингредиент')
    @pytest.mark.parametrize('browser_name', ['chrome', 'firefox'])
    def test_click_ingredient(self, browser_name):
        driver = WebdriverFactory().web_driver(browser_name)
        main_page = MainPage(driver)
        driver.get(TestUrl.main_page_url)
        assert main_page.click_ingredient() == True
        driver.quit()

    @allure.title('Всплывающее окно закрывается по клику')
    @pytest.mark.parametrize('browser_name', ['chrome', 'firefox'])
    def test_close_popup_window(self, browser_name):
        driver = WebdriverFactory().web_driver(browser_name)
        main_page = MainPage(driver)
        driver.get(TestUrl.main_page_url)
        assert main_page.close_popup_window() == "Соберите бургер"
        driver.quit()

    @allure.title('Увеличение каунтера ингредиента при добавлении в заказ')
    @pytest.mark.parametrize('browser_name', ['chrome', 'firefox'])
    def test_increase_count_ingredient(self, browser_name):
        driver = WebdriverFactory().web_driver(browser_name)
        main_page = MainPage(driver)
        driver.get(TestUrl.main_page_url)
        assert main_page.increase_count_ingredient_firefox() == '2'
        driver.quit()

    @allure.title('Залогиненный пользователь может оформить заказ')
    @pytest.mark.parametrize('browser_name', ['chrome', 'firefox'])
    def test_authorized_user_and_order(self, browser_name):
        driver = WebdriverFactory().web_driver(browser_name)
        main_page = MainPage(driver)
        user_page = UserPage(driver)
        driver.get(TestUrl.main_page_url)
        user_page.enter_login_to_account()
        assert main_page.authorized_user_and_order() == "Ваш заказ начали готовить"
        driver.quit()