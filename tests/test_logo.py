import allure
from pages.main_page import MainPage
from data import link_dzen, link_main_page, link_order


@allure.suite('Тесты проверки логотипов')
class TestClickLogo:


    @allure.title('Проверка логотипа Яндекс дзен')
    def test_click_logo_dzen(self, driver):
        page = MainPage(driver)
        driver.get(link_order)
        page.click_to_yandex_works()
        assert link_dzen == driver.current_url

    @allure.title('Проверка логотипа самоката')
    def test_click_scooter_logo(self, driver):
        page = MainPage(driver)
        driver.get(link_order)
        page.click_scooter_logo()
        assert driver.current_url == link_main_page



