import allure
from locators.order_locators import TestOrderPageLocators
from selenium.common import NoSuchElementException
from pages.base_page import BasePage

class OrderPage(BasePage):

    @allure.step('Всплывающее окно с деталями заказа')
    def popup_window_data_ingredient(self):
        self.find_element_with_wait(TestOrderPageLocators.ELEMENTS_MAIN_PAGE)
        self.waiting_for_element(TestOrderPageLocators.ORDER_FEED)
        self.find_element_with_wait(TestOrderPageLocators.HEADER_ORDER_FEED)
        self.waiting_for_element(TestOrderPageLocators.INGREDIENT_ORDER_FEED)
        try:
            self.find_element_with_wait(TestOrderPageLocators.WINDOW_DATA_INGREDIENT)
            return True
        except NoSuchElementException:
            return False

    @allure.step('Заказы пользователя из раздела "История заказов" отображаются на странице "Лента заказов"')
    def list_user_orders_in_order_feed(self):
        self.waiting_for_element(TestOrderPageLocators.BUTTON_HISTORY_ORDERS)
        self.find_element_with_wait(TestOrderPageLocators.LIST_USER_ORDERS)
        self.scroll_to_element(TestOrderPageLocators.NUMBER_USER_ORDER)
        number_user_order = self.get_text_from_element(TestOrderPageLocators.NUMBER_USER_ORDER)
        self.waiting_for_element(TestOrderPageLocators.ORDER_FEED)
        self.find_element_with_wait(TestOrderPageLocators.LIST_ORDERS)
        for number in range(1, 1000):
            order_locator = self.get_format_locators(TestOrderPageLocators.NUMBERS_ORDERS, number)
            self.scroll_to_element(order_locator)
            order = self.get_text_from_element(order_locator)
            if order == number_user_order:
                return True
            else:
                continue

    @allure.step('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def counter_completed_for_all_time(self):
        self.waiting_for_element(TestOrderPageLocators.ORDER_FEED)
        self.find_element_with_wait(TestOrderPageLocators.LIST_ORDERS)
        counter = self.get_text_from_element(TestOrderPageLocators.COUNTER_COMPLETED_FOR_ALL_TIME)
        return counter

    @allure.step('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def counter_completed_for_today(self):
        self.waiting_for_element(TestOrderPageLocators.ORDER_FEED)
        self.find_element_with_wait(TestOrderPageLocators.LIST_ORDERS)
        self.find_element_with_wait(TestOrderPageLocators.COUNTER_COMPLETED_FOR_TODAY)
        counter = self.get_text_from_element(TestOrderPageLocators.COUNTER_COMPLETED_FOR_TODAY)
        return counter

    @allure.step('После оформления заказа его номер появляется в разделе "В работе"')
    def order_number_in_progress(self):
        self.waiting_for_element(TestOrderPageLocators.ORDER_FEED)
        self.find_element_with_wait(TestOrderPageLocators.LIST_ORDERS)
        self.find_element_with_wait(TestOrderPageLocators.ORDER_IN_PROGRESS)
        element = self.get_text_from_element(TestOrderPageLocators.ORDER_IN_PROGRESS)
        return element


