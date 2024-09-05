from selenium import webdriver
from pages.main_page import MainPage
from pages.result_page import ResultPage
import allure

@allure.title("Заполнение формы")
@allure.description("Заполнить форму, оставив поле zip-code пустым.")
@allure.feature("INPUT")
@allure.severity(allure.severity_level.CRITICAL)
def test_data_types_form():
    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    main_page.input_data()
    main_page.click_button_submit()

    result_page = ResultPage(driver)
    red = result_page.red_field()
    
    with allure.step("Проверить, что цвет поля красный"):
        assert red == 'rgba(132, 32, 41, 1)'
    green = result_page.green_fields()
    
    with allure.step("Проверить, что цвет полей зеленый"):
        assert green == 'rgba(15, 81, 50, 1)'
    driver.quit()