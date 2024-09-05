from selenium.webdriver.common.by import By
import allure

class ResultPage:
    """Класс предоставляет методы для определения цвета полей формы"""
    def __init__(self, driver):
        self._driver = driver

    @allure.step("Определить цвет поля 'zip-code'")
    def red_field(self) -> str:
        return self._driver.find_element(
            By.CSS_SELECTOR, "#zip-code").value_of_css_property("color")

    @allure.step("Определить цвета остальных полей")
    def green_fields(self) -> str:
        locators = [
            "#first-name",
            "#last-name",
            "#address",
            "#city",
            "#country",
            "#e-mail",
            "#phone",
            "#job-position",
            "#company"
            ]
        for green in locators:
            return self._driver.find_element(By.CSS_SELECTOR, green
                                             ).value_of_css_property("color")