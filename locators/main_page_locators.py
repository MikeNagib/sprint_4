from selenium.webdriver.common.by import By


class MainPageLocators:
    get_cookie_button = (By.ID, 'rcc-confirm-button')
    order_button = (By.XPATH, ".//button[text()='Заказать']")
    logo_yandex = (By.XPATH, ".//img[@alt='Yandex']")
    logo_scooter = [By.XPATH, './/img[@alt="Scooter"]']
    button_header_order = (By.XPATH, "(//button[text()='Заказать'])[1]")
    button_middle_order = (By.XPATH, "(//button[text()='Заказать'])[2]")
