import allure
from pages.main_page import MainPage
from data import link_dzen, link_main_page


@allure.suite('Тесты проверки логотипов')
class TestClickLogo:

    @allure.title('Проверка логотипа самоката')
    def test_click_scooter_logo(self, driver):
        page = MainPage(driver)
        page.click_scooter_logo()
        assert driver.current_url == link_main_page

    @allure.title('Проверка логотипа Яндекс дзен')
    def test_click_logo_dzen(self, driver):
        page = MainPage(driver)
        assert link_dzen == page.verify_if_link_to_yandex_works()
