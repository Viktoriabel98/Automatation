from selenium.webdriver.common.by import By
import allure


class OverviewPage:
    """Класс предоставляет метод для получения стоимости покупки"""
    def __init__(self, driver):
        self._driver = driver

    @allure.step("Получить сумму покупки")
    def get_price(self):
        return self._driver.find_element(
            By.CSS_SELECTOR, '.summary_total_label').text