import allure

from pages.order_page import OrderPage
from pages.user_page import UserPage
from pages.main_page import MainPage

class TestOrderPage:

    @allure.title('Открытие всплывающего окна с деталями')
    def test_popup_window_data_ingredient(self, driver):
        order_page = OrderPage(driver)
        assert order_page.popup_window_data_ingredient()

    @allure.title('Заказы пользователя из раздела "История заказов" отображаются на странице "Лента заказов"')
    def test_list_user_orders_in_order_feed(self, driver):
        order_page = OrderPage(driver)
        user_page = UserPage(driver)
        user_page.enter_login_to_account()
        assert order_page.list_user_orders_in_order_feed()

    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_counter_completed_for_all_time(self, driver):
        order_page = OrderPage(driver)
        user_page = UserPage(driver)
        main_page = MainPage(driver)
        user_page.enter_login_to_account()
        counter_before = int(order_page.counter_completed_for_all_time())
        main_page.authorized_user_and_order()
        counter_after = int(order_page.counter_completed_for_all_time())
        assert counter_after == counter_before + 1

    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_counter_completed_for_today(self, driver):
        order_page = OrderPage(driver)
        user_page = UserPage(driver)
        main_page = MainPage(driver)
        user_page.enter_login_to_account()
        counter_before = int(order_page.counter_completed_for_today())
        main_page.authorized_user_and_order()
        counter_after = int(order_page.counter_completed_for_today())
        assert counter_after == counter_before + 1

    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_order_number_in_progress(self, driver):
        order_page = OrderPage(driver)
        user_page = UserPage(driver)
        main_page = MainPage(driver)
        user_page.enter_login_to_account()
        number_order = int(main_page.get_order_number_in_popup_window())
        number_order_in_progress = int(order_page.order_number_in_progress())
        assert number_order == number_order_in_progress

