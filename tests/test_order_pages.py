import allure
import pytest

from data import TestUrl
from pages.order_page import OrderPage
from pages.user_page import UserPage
from pages.main_page import MainPage
from helpers import WebdriverFactory

class TestOrderPage:

    @allure.title('Открытие всплывающего окна с деталями')
    @pytest.mark.parametrize('browser_name', ['chrome', 'firefox'])
    def test_popup_window_data_ingredient(self, browser_name):
        driver = WebdriverFactory().web_driver(browser_name)
        order_page = OrderPage(driver)
        driver.get(TestUrl.main_page_url)
        assert order_page.popup_window_data_ingredient() == True
        driver.quit()

    @allure.title('Заказы пользователя из раздела "История заказов" отображаются на странице "Лента заказов"')
    @pytest.mark.parametrize('browser_name', ['chrome', 'firefox'])
    def test_list_user_orders_in_order_feed(self, browser_name):
        driver = WebdriverFactory().web_driver(browser_name)
        order_page = OrderPage(driver)
        user_page = UserPage(driver)
        driver.get(TestUrl.main_page_url)
        user_page.enter_login_to_account()
        assert order_page.list_user_orders_in_order_feed() == True
        driver.quit()

    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    @pytest.mark.parametrize('browser_name', ['chrome', 'firefox'])
    def test_counter_completed_for_all_time(self, browser_name):
        driver = WebdriverFactory().web_driver(browser_name)
        order_page = OrderPage(driver)
        user_page = UserPage(driver)
        main_page = MainPage(driver)
        driver.get(TestUrl.main_page_url)
        user_page.enter_login_to_account()
        counter_before = int(order_page.counter_completed_for_all_time())
        main_page.authorized_user_and_order()
        counter_after = int(order_page.counter_completed_for_all_time())
        assert counter_after == counter_before + 1
        driver.quit()

    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    @pytest.mark.parametrize('browser_name', ['chrome', 'firefox'])
    def test_counter_completed_for_today(self, browser_name):
        driver = WebdriverFactory().web_driver(browser_name)
        order_page = OrderPage(driver)
        user_page = UserPage(driver)
        main_page = MainPage(driver)
        driver.get(TestUrl.main_page_url)
        user_page.enter_login_to_account()
        counter_before = int(order_page.counter_completed_for_today())
        main_page.authorized_user_and_order()
        counter_after = int(order_page.counter_completed_for_today())
        assert counter_after == counter_before + 1
        driver.quit()

    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    @pytest.mark.parametrize('browser_name', ['chrome', 'firefox'])
    def test_order_number_in_progress(self, browser_name):
        driver = WebdriverFactory().web_driver(browser_name)
        order_page = OrderPage(driver)
        user_page = UserPage(driver)
        main_page = MainPage(driver)
        driver.get(TestUrl.main_page_url)
        user_page.enter_login_to_account()
        main_page.authorized_user_and_order()
        number_order = int(main_page.get_order_number_in_popup_window())
        number_order_in_progress = int(order_page.order_number_in_progress())
        assert number_order == number_order_in_progress
        driver.quit()

