from selenium.webdriver.common.by import By
import allure


class ResultPage:
    """Класс предоставляет метод для работы с результатом работы приложения"""
    def __init__(self, driver):
        self._driver = driver

    @allure.step("Получить результат выражения")
    def sum_result(self) -> str:
        return self._driver.find_element(
            By.CSS_SELECTOR, 'div.screen').text