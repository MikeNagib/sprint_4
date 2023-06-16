
from datetime import datetime, timedelta
from locators.questions_page_locators import QuestionsPageLocators
from locators.main_page_locators import MainPageLocators

link_main_page = 'https://qa-scooter.praktikum-services.ru/'
link_dzen = "https://dzen.ru/?yredirect=true"

TIME_TO_WAIT_ELEMENTS = 15
TEXT_ORDER_IS_DONE = "Заказ оформлен"

orders = [{"by_button": MainPageLocators.button_middle_order,
           "firstname": 'Иван',
           "lastname": 'Иванов',
           "address": 'Москва, ул. Ленина, 111 - 12',
           "phone": '+79260114523',
           "subway_station": 'Черкизовская',
           "date": (datetime.now() + timedelta(days=7)).strftime("%d.%m.%Y"),
           "duration": 3,
           "color": 'grey',
           "comment": 'Подъезд 3'
           },
          {"by_button": MainPageLocators.button_header_order,
           "firstname": 'Михаил',
           "lastname": 'Нагибин',
           "address": 'Москва, ул. Гагарина, 10Б - 21',
           "phone": '+79011111222',
           "subway_station": 'Сокол ',
           "date": (datetime.now() + timedelta(days=3)).strftime("%d.%m.%Y"),
           "duration": 5,
           "color": 'black',
           "comment": 'Позвонить заранее!'
           }
          ]

questions_and_answers = [[QuestionsPageLocators.question_1, QuestionsPageLocators.response_1],
                         [QuestionsPageLocators.question_2, QuestionsPageLocators.response_2],
                         [QuestionsPageLocators.question_3, QuestionsPageLocators.response_3],
                         [QuestionsPageLocators.question_4, QuestionsPageLocators.response_4],
                         [QuestionsPageLocators.question_5, QuestionsPageLocators.response_5],
                         [QuestionsPageLocators.question_6, QuestionsPageLocators.response_6],
                         [QuestionsPageLocators.question_7, QuestionsPageLocators.response_7],
                         [QuestionsPageLocators.question_8, QuestionsPageLocators.response_8]]
