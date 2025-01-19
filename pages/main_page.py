import allure
from locators.main_locators import TestMainPageLocators
from selenium.common import NoSuchElementException
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step('Переход по клику на "Конструктор"')
    def constructor(self):
        self.find_element_with_wait(TestMainPageLocators.ELEMENTS_MAIN_PAGE)
        self.click_element_with_wait(TestMainPageLocators.BUTTON_ENTER_TO_ACCOUNT)
        self.waiting_for_element(TestMainPageLocators.BUTTON_CONSTRUCTOR)
        return self.get_url()

    @allure.step('Переход по клику на "Лента заказов"')
    def order_feed(self):
        self.find_element_with_wait(TestMainPageLocators.ELEMENTS_MAIN_PAGE)
        self.click_element_with_wait(TestMainPageLocators.ORDER_FEED)
        self.find_element_with_wait(TestMainPageLocators.HEADER_ORDER_FEED)
        try:
            self.find_element_with_wait(TestMainPageLocators.LIST_ORDERS)
            return True
        except NoSuchElementException:
            return False

    @allure.step('Появление окна с деталями при клике на ингредиент')
    def click_ingredient(self):
        self.find_element_with_wait(TestMainPageLocators.ELEMENTS_MAIN_PAGE)
        self.click_element_with_wait(TestMainPageLocators.INGREDIENT_CONSTRUCTOR)
        try:
            self.find_element_with_wait(TestMainPageLocators.POPUP_WINDOW)
            return True
        except NoSuchElementException:
            return False

    @allure.step('Всплывающее окно закрывается кликом по крестику')
    def close_popup_window(self):
        self.find_element_with_wait(TestMainPageLocators.CONSTRUCTOR_LIST)
        self.click_element_with_wait(TestMainPageLocators.INGREDIENT_CONSTRUCTOR)
        self.find_element_with_wait(TestMainPageLocators.POPUP_WINDOW)
        self.click_element(TestMainPageLocators.BUTTON_CLOSE_POPUP_WINDOW)
        element = self.get_text_from_element(TestMainPageLocators.HEADER_CONSTRUCTOR)
        return element

    @allure.step('Увеличение каунтера ингредиента при добавлении в заказ, хром')
    def increase_count_ingredient_chrome(self):
        self.find_element_with_wait(TestMainPageLocators.CONSTRUCTOR_LIST)
        self.move_the_element(TestMainPageLocators.INGREDIENT_CONSTRUCTOR, TestMainPageLocators.CONSTRUCTOR_BASKET)
        self.scroll_to_element(TestMainPageLocators.COUNTER_INGREDIENT_CONSTRUCTOR)
        counter = self.get_text_from_element(TestMainPageLocators.COUNTER_INGREDIENT_CONSTRUCTOR)
        return counter

    @allure.step('Увеличение каунтера ингредиента при добавлении в заказ, фокс')
    def increase_count_ingredient_firefox(self):
        self.find_element_with_wait(TestMainPageLocators.CONSTRUCTOR_LIST)
        self.add_ingredients_in_order(TestMainPageLocators.INGREDIENT_CONSTRUCTOR, TestMainPageLocators.CONSTRUCTOR_BASKET)
        self.scroll_to_element(TestMainPageLocators.COUNTER_INGREDIENT_CONSTRUCTOR)
        counter = self.get_text_from_element(TestMainPageLocators.COUNTER_INGREDIENT_CONSTRUCTOR)
        return counter
    
    @allure.step('Залогиненный пользователь может оформить заказ')
    def authorized_user_and_order(self):
        self.waiting_for_element(TestMainPageLocators.BUTTON_CONSTRUCTOR)
        self.find_element_with_wait(TestMainPageLocators.CONSTRUCTOR_LIST)
        self.add_ingredients_in_order(TestMainPageLocators.INGREDIENT_CONSTRUCTOR,TestMainPageLocators.CONSTRUCTOR_BASKET)
        self.click_element(TestMainPageLocators.BUTTON_PLACE_AN_ORDER)
        self.find_element_with_wait(TestMainPageLocators.POPUP_WINDOW)
        element = self.get_text_from_element(TestMainPageLocators.WINDOW_SUCCESSFUL_ORDER)
        self.waiting_for_element(TestMainPageLocators.MODAL_WINDOW)
        return element

    @allure.step('Получить номер заказа из всплывающего окна')
    def get_order_number_in_popup_window(self):
        self.waiting_for_element(TestMainPageLocators.BUTTON_CONSTRUCTOR)
        self.find_element_with_wait(TestMainPageLocators.CONSTRUCTOR_LIST)
        self.move_the_element(TestMainPageLocators.INGREDIENT_CONSTRUCTOR, TestMainPageLocators.CONSTRUCTOR_BASKET)
        self.waiting_for_element(TestMainPageLocators.BUTTON_PLACE_AN_ORDER)
        self.find_element_with_wait(TestMainPageLocators.POPUP_WINDOW)
        element = self.wait_element_disappearing(TestMainPageLocators.NUMBER_ORDER_IN_POPUP_WINDOW)
        self.waiting_for_element(TestMainPageLocators.MODAL_WINDOW)
        return element







