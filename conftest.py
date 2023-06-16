import pytest
from selenium import webdriver
from data import link_main_page
@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(link_main_page)

    yield driver

    driver.quit()
