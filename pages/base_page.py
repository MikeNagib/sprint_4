import allure
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import link_main_page, TIME_TO_WAIT_ELEMENTS


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(link_main_page)

    def click(self, by_locator):
        WebDriverWait(self.driver, TIME_TO_WAIT_ELEMENTS).until(expected_conditions.
                                                                visibility_of_element_located(by_locator)).click()

    def send_data(self, by_locator, text):
        WebDriverWait(self.driver, TIME_TO_WAIT_ELEMENTS). \
            until(expected_conditions.visibility_of_element_located(by_locator)).send_keys(text)

    def navigate_to_link(self, by_locator, target):
        self.driver.find_element(*by_locator).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, TIME_TO_WAIT_ELEMENTS).until(expected_conditions.url_to_be(target))
        return self.driver.current_url

    def find_text(self, by_locator):
        WebDriverWait(self.driver, TIME_TO_WAIT_ELEMENTS).until(
            expected_conditions.visibility_of_element_located(by_locator))
        return self.driver.find_element(*by_locator).text

    def wait_element(self, locator):
        WebDriverWait(self.driver, TIME_TO_WAIT_ELEMENTS).until(
            expected_conditions.visibility_of_element_located(locator))

    def wait_page_is_loaded(self):
        self.wait_element(MainPageLocators.STATUS_BUTTON)

    @allure.step('Найти вопрос')
    def find_question(self, question_locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*question_locator))
        WebDriverWait(self.driver, TIME_TO_WAIT_ELEMENTS).until(
            expected_conditions.element_to_be_clickable(question_locator))
        self.driver.find_element(*question_locator).click()
