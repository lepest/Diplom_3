from selenium.webdriver.common.by import By

class TestOrderPageLocators:

    ELEMENTS_MAIN_PAGE = By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2"  # Для проверки загрузки главной страницы
    ORDER_FEED = By.XPATH, ".//ul[@class='AppHeader_header__list__3oKJj']/li[@class='undefined ml-2']/a[@href='/feed']"  # Кнопка "Лента заказов"
    HEADER_ORDER_FEED = By.XPATH, ".//h1[text()='Лента заказов']"  # Заголовок "Лента заказов"
    LIST_ORDERS = By.XPATH, ".//div[@class='OrderFeed_contentBox__3-tWb']/ul[@class='OrderFeed_list__OLh59']"  # Список заказов
    INGREDIENT_ORDER_FEED = By.XPATH, ".//li[1]/a[@class='OrderHistory_link__1iNby']"
    WINDOW_DATA_INGREDIENT = By.XPATH, ".//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']/h2"
    INGREDIENT_NAME_ORDER_FEED = By.XPATH, ".//li[1]/a[@class='OrderHistory_link__1iNby']/h2"
    BUTTON_ENTER_TO_ACCOUNT = By.XPATH, ".//div[@class='BurgerConstructor_basket__container__2fUl3 mt-10']/button[text()='Войти в аккаунт']"  # Кнопка "Войти в аккаунт"
    LIST_BUTTONS_PERSONAL_ACCOUNT = By.XPATH, ".//ul[@class='Account_list__3KQQf mb-20']"  # Список кнопок в личном кабинете
    BUTTON_HISTORY_ORDERS = By.XPATH, ".//ul/li[2]/a[text()='История заказов']"  # Кнопка "История заказов"
    LIST_USER_ORDERS = By.XPATH, ".//ul[@class='OrderHistory_profileList__374GU OrderHistory_list__KcLDB']/li[1]/a"  # Список заказов
    NUMBER_USER_ORDER = By.XPATH, ".//ul[@class='OrderHistory_profileList__374GU OrderHistory_list__KcLDB']/li[last()]/a/div[@class='OrderHistory_textBox__3lgbs mb-6']/p[@class='text text_type_digits-default']" #Номер последнего заказа пользователя
    NUMBERS_ORDERS = By.XPATH, ".//ul[@class='OrderFeed_list__OLh59']/li[{}]/a/div[@class='OrderHistory_textBox__3lgbs mb-6']/p[@class='text text_type_digits-default']" #Номера всех заказов
    COUNTER_COMPLETED_FOR_ALL_TIME = By.XPATH, ".//div[@class='OrderFeed_ordersData__1L6Iv']/div[@class='undefined mb-15']/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']" #Счётчик "Выполнено за всё время"
    FORM_ENTER_TO_PERSONAL_ACCOUNT = By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']"  # Форма для входа в личный кабинет
    COUNTER_COMPLETED_FOR_TODAY = By.XPATH, ".//div[@class='OrderFeed_ordersData__1L6Iv']/div[3]/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']" #Счётчик "Выполнено за сегодня"
    ORDER_IN_PROGRESS = By.XPATH, ".//div[@class='OrderFeed_orderStatusBox__1d4q2 mb-15']//li[@class='text text_type_digits-default mb-2']"
    BUTTON_CLOSE_POPUP_WINDOW = By.XPATH, ".//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"

