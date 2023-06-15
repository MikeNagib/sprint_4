import pytest
import allure
from pages.main_page import MainPage
from conftest import questions_and_answers, link_dzen, link_main_page


@allure.suite('Набор тестов для проверки QA')
class TestQuestionPage:

    @allure.title('Проверка вопросов')
    @pytest.mark.parametrize('question, answer', questions_and_answers)
    def test_answer_matches_question_true(self, driver, question, answer):
        page = MainPage(driver)
        page.accept_cookies()
        page.find_question(question)
        page.find_answer(answer)

    @allure.title('Проверка логотипов')
    def test_click_logo(self, driver):
        page = MainPage(driver)
        assert link_dzen == page.verify_if_link_to_yandex_works()
        assert link_main_page == page.verify_if_link_to_base_page_works()
