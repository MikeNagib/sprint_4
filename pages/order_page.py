import allure
from locators.order_page_locators import OrderPageLocators

from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Нажать кнопку для заказа')
    def click_order_button(self, by_button):
        self.click(by_button)

    @allure.step('Заполнение данных клиента')
    def fill_customer_data(self, firstname, lastname, address, station, phone):
        self.send_data(OrderPageLocators.field_firstname, firstname)
        self.send_data(OrderPageLocators.field_lastname, lastname)
        self.send_data(OrderPageLocators.field_address, address)
        self.send_data(OrderPageLocators.field_station, station)
        self.click(OrderPageLocators.selected_station)
        self.send_data(OrderPageLocators.field_phone, phone)

    @allure.step('Кнопка дальше')
    def click_button_next(self):
        self.click(OrderPageLocators.button_next)

    @allure.step('Детали заказа')
    def fill_order_data(self, date, duration, color, comment):
        self.send_data(OrderPageLocators.field_date, date)
        self.click(OrderPageLocators.dropdown_arrow)
        self.click(OrderPageLocators.field_dropdown_option[duration])
        self.click(OrderPageLocators.field_scooter_colors[color])
        self.send_data(OrderPageLocators.field_comment, comment)

    @allure.step('Кнопку для заказа')
    def click_button_to_submit(self):
        self.click(OrderPageLocators.button_order)

    @allure.step('Потверждение заказа')
    def click_button_confirm(self):
        self.click(OrderPageLocators.button_confirm)

    @allure.step('Всплывающее окно с сообщением об успешном создании заказа.')
    def verify_if_order_is_created(self):
        return self.find_text(OrderPageLocators.modal_window_with_oder_number)
