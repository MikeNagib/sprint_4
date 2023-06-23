import allure
from locators.questions_page_locators import QuestionsPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from data import  TIME_TO_WAIT_ELEMENTS, link_dzen
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Принять cookie')
    def accept_cookies(self):
        self.driver.find_element(*MainPageLocators.get_cookie_button).click()

    @allure.step('Клик на лого Яндекс')
    def click_to_yandex_works(self):
        self.navigate_to_link(MainPageLocators.logo_yandex, link_dzen)

    @allure.step('Клик на лого самоката')
    def click_scooter_logo(self):
        self.driver.find_element(*MainPageLocators.logo_scooter).click()

    @allure.step('Найти ответ')
    def check_answer(self, answer_locator):
        WebDriverWait(self.driver, TIME_TO_WAIT_ELEMENTS).until(
            expected_conditions.visibility_of_element_located(QuestionsPageLocators.open_response_text))
        assert self.driver.find_element(*QuestionsPageLocators.open_response_text).text == \
               answer_locator[1].split('\'')[
                   1]

    @allure.step('Найти вопрос')
    def find_question(self, question_locator):
        self.scrolling(question_locator)
        WebDriverWait(self.driver, TIME_TO_WAIT_ELEMENTS).until(
            expected_conditions.element_to_be_clickable(question_locator))
        self.driver.find_element(*question_locator).click()
