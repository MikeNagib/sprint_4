import allure
from locators.questions_page_locators import QuestionsPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from data import link_main_page, TIME_TO_WAIT_ELEMENTS, link_dzen
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Принять cookie')
    def accept_cookies(self):
        self.driver.find_element(*MainPageLocators.get_cookie_button).click()

    @allure.step('Переход на Яндекс лого')
    def verify_if_link_to_yandex_works(self):
        self.driver.get(link_main_page)
        return self.navigate_to_link(MainPageLocators.logo_yandex, link_dzen)

    def click_scooter_logo(self):
        self.driver.find_element(*MainPageLocators.logo_scooter).click()

    @allure.step('Найти ответ')
    def find_answer(self, answer_locator):
        WebDriverWait(self.driver, TIME_TO_WAIT_ELEMENTS).until(
            expected_conditions.visibility_of_element_located(QuestionsPageLocators.open_response_text))
        assert self.driver.find_element(*QuestionsPageLocators.open_response_text).text == \
               answer_locator[1].split('\'')[
                   1]
