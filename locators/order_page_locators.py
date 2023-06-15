from selenium.webdriver.common.by import By


class OrderPageLocators:
    field_firstname = (By.XPATH, "//input[@placeholder='* Имя']")
    field_lastname = (By.XPATH, "//input[@placeholder='* Фамилия']")
    field_address = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    field_station = (By.XPATH, "//input[@placeholder='* Станция метро']")
    field_phone = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    selected_station = (By.CSS_SELECTOR, '[class="select-search__select"]')
    button_next = (By.XPATH, "//button[text()='Далее']")
    button_order = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    button_confirm = (By.XPATH, "//button[text()='Да']")

    field_date = [By.XPATH, ".//*[@placeholder='* Когда привезти самокат']"]
    dropdown_arrow = [By.XPATH, ".//*[@class='Dropdown-arrow']"]
    field_dropdown_option = {
        1: [By.XPATH, "(//div[@class='Dropdown-option'])[1]"],
        2: [By.XPATH, "(//div[@class='Dropdown-option'])[2]"],
        3: [By.XPATH, "(//div[@class='Dropdown-option'])[3]"],
        4: [By.XPATH, "(//div[@class='Dropdown-option'])[4]"],
        5: [By.XPATH, "(//div[@class='Dropdown-option'])[5]"],
        6: [By.XPATH, "(//div[@class='Dropdown-option'])[6]"],
        7: [By.XPATH, "(//div[@class='Dropdown-option'])[7]"]
    }
    field_scooter_colors = {
        "black": [By.ID, 'black'],
        "grey": [By.ID, 'grey']
            }
    field_comment = (By.XPATH, ".//*[@placeholder='Комментарий для курьера']")
    modal_window_with_oder_number = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
