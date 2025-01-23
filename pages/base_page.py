import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from data import TestUrl

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        driver.get(TestUrl.main_page_url)

    @allure.step('Поиск элемента с ожиданием')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator)

    @allure.step('Поиск элемента без ожидания')
    def find_element(self, locator):
        self.driver.find_element(*locator).is_displayed()

    @allure.step('Клик на элемент с ожиданием')
    def click_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).click()

    @allure.step('Клик на скрытый элемент')
    def click_invisibility_element_with_wait(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator).click()

    @allure.step('Клик на элемент без ожидания')
    def click_element(self, locator):
        return self.driver.find_element(*locator).click()

    @allure.step('Ввод текста в поле')
    def enter_text_to_field(self, locator, text):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).send_keys(text)

    @allure.step('Прокручивание до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Форматирование локаторов')
    def get_format_locators(self, data_locator, data):
        method, locator = data_locator
        locator = locator.format(data)
        return method, locator

    @allure.step('Получить url')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Ожидание элемента')
    def waiting_for_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Получить текст из элемента')
    def get_text_from_element(self, locator):
        element = self.driver.find_element(*locator).text
        return element

    @allure.step('Перетаскивание элемента, chrome')
    def move_the_element(self, locator_element, locator_target):
        element = self.driver.find_element(*locator_element)
        target = self.driver.find_element(*locator_target)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, target).perform()

    @allure.step('Ожидание исчезновения элемента')
    def wait_element_disappearing(self, locator, text):
        self.driver.find_element(*locator)
        WebDriverWait(self.driver, 5).until_not(expected_conditions.text_to_be_present_in_element(locator, text))
        element = self.driver.find_element(*locator)
        return element.text

    @allure.step('Перетаскивание элемента, добавление ингредиентов в заказ, firefox')
    def add_ingredients_in_order(self, locator_element, locator_target):
        element = self.driver.find_element(*locator_element)
        target = self.driver.find_element(*locator_target)
        script = """
                function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                var dataTransfer = new DataTransfer();
                var dragStartEvent = new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
                        });
                sourceNode.dispatchEvent(dragStartEvent);
                var dropEvent = new DragEvent('drop', {
                            bubbles: true,
                            cancelable: true,
                            dataTransfer: dataTransfer
                        });
                destinationNode.dispatchEvent(dropEvent);
                var dragEndEvent = new DragEvent('dragend', {
                            bubbles: true,
                            cancelable: true,
                            dataTransfer: dataTransfer
                        });
                        sourceNode.dispatchEvent(dragEndEvent);
                    }
                    simulateHTML5DragAndDrop(arguments[0], arguments[1]);
                    """
        self.driver.execute_script(script, element, target)