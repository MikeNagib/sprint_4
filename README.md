
**автотесты для учебного сервиса «Яндекс.Самокат»**

Содержимое проекта:

* README.md - этот файл
* requirements.txt - зависимости, основные
* ./conftest.py - конфигурация тестов
* ./tests/ - каталог с тестами
* ./tests/test_order_page.py - тесты для проверки создания заказа
* ./tests/test_questions_page.py - тесты для проверки вопросов и ответов, и навигации по лого
* ./locators/ - каталог с локаторами
* ./locators/main_page_locators.py - локаторы на главной странице
* ./locators/order_page_locators.py - локаторы для создания заказа
* ./locators/questions_page_locators.py - локаторы для проверки вопросов и ответов
* ./pages/ - каталог с классами страниц
* ./pages/main_page.py - класс для главной страницы
* ./pages/order_page.py - класс для страницы оформления заказа
* ./pages/questions_page.py - класс для страницы с вопросами
* ./allure_result_folder/ - каталог с Allure отчетом