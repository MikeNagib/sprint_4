import allure
from locators.questions_page_locators import QuestionsPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from conftest import link_main_page, TIME_TO_WAIT_ELEMENTS, link_dzen


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(link_main_page)

    @allure.step('Принять cookie')
    def accept_cookies(self):
        self.driver.find_element(*MainPageLocators.get_cookie_button).click()

    def click(self, by_locator):
        WebDriverWait(self.driver, TIME_TO_WAIT_ELEMENTS).until(expected_conditions.
                                                                visibility_of_element_located(by_locator)).click()

    def send_data(self, by_locator, text):
        WebDriverWait(self.driver, TIME_TO_WAIT_ELEMENTS). \
            until(expected_conditions.visibility_of_element_located(by_locator)).send_keys(text)

    def find_text(self, by_locator):
        WebDriverWait(self.driver, TIME_TO_WAIT_ELEMENTS).until(
            expected_conditions.visibility_of_element_located(by_locator))
        return self.driver.find_element(*by_locator).text

    def navigate_to_link(self, by_locator, target):
        self.driver.find_element(*by_locator).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, TIME_TO_WAIT_ELEMENTS).until(expected_conditions.url_to_be(target))
        return self.driver.current_url

    @allure.step('Переход на Яндекс лого')
    def verify_if_link_to_yandex_works(self):
        self.driver.get(link_main_page)
        return self.navigate_to_link(MainPageLocators.logo_yandex, link_dzen)

    @allure.step('Переход на Самокат лого')
    def verify_if_link_to_base_page_works(self):
        self.driver.get(link_main_page)
        return self.navigate_to_link(MainPageLocators.logo_scooter, link_main_page)

    @allure.step('Найти вопрос')
    def find_question(self, question_locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*question_locator))
        WebDriverWait(self.driver, TIME_TO_WAIT_ELEMENTS).until(
            expected_conditions.element_to_be_clickable(question_locator))
        self.driver.find_element(*question_locator).click()

    @allure.step('Найти ответ')
    def find_answer(self, answer_locator):
        WebDriverWait(self.driver, TIME_TO_WAIT_ELEMENTS).until(
            expected_conditions.visibility_of_element_located(QuestionsPageLocators.open_response_text))
        assert self.driver.find_element(*QuestionsPageLocators.open_response_text).text == \
               answer_locator[1].split('\'')[
                   1]
