from selenium.webdriver.common.by import By
import data_response


class QuestionsPageLocators:
    question_1 = (By.ID, 'accordion__heading-0')
    question_2 = (By.ID, 'accordion__heading-1')
    question_3 = (By.ID, 'accordion__heading-2')
    question_4 = (By.ID, 'accordion__heading-3')
    question_5 = (By.ID, 'accordion__heading-4')
    question_6 = (By.ID, 'accordion__heading-5')
    question_7 = (By.ID, 'accordion__heading-6')
    question_8 = (By.ID, 'accordion__heading-7')

    response_1 = (By.XPATH, data_response.response_1)
    response_2 = (By.XPATH, data_response.response_2)
    response_3 = (By.XPATH, data_response.response_3)
    response_4 = (By.XPATH, data_response.response_4)
    response_5 = (By.XPATH, data_response.response_5)
    response_6 = (By.XPATH, data_response.response_6)
    response_7 = (By.XPATH, data_response.response_7)
    response_8 = (By.XPATH, data_response.response_8)

    open_response_text = (By.XPATH, ".//div[@role='region' and not(@hidden)]/p")
