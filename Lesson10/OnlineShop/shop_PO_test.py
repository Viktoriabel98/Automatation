from selenium import webdriver
from pages.main_page import MainPage
from pages.result_page import ResultPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage
import allure

@allure.title("Онлайн-магазин")
@allure.description("Авторизоваться, выбрать товары, добаить их в корзину, заполнить данные о покупателе и проверить итоговую стоимость.")
@allure.feature("GET")
@allure.severity(allure.severity_level.BLOCKER)
def test_data_types_form():
    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    main_page.authorization()

    product_page = ResultPage(driver)
    product_page.add_products()

    cart_page = CartPage(driver)
    cart_page.get()
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.input_data()

    overwiew_page = OverviewPage(driver)
    price = overwiew_page.get_price()

    with allure.step("Проверить итоговую стоимость"):
        assert price == "Total: $58.29"
    
    driver.quit()