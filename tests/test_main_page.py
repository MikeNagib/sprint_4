import pytest
import allure
from pages.main_page import MainPage
from data import questions_and_answers


@allure.suite('Набор тестов для проверки FAQ')
class TestQuestionPage:

    @allure.title('Проверка вопросов')
    @pytest.mark.parametrize('question, answer', questions_and_answers)
    def test_answer_matches_question_true(self, driver, question, answer):
        page = MainPage(driver)
        page.accept_cookies()
        page.find_question(question)
        page.find_answer(answer)

