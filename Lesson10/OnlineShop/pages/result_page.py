from selenium.webdriver.common.by import By
import allure


class ResultPage:
    """Класс предоставляет метод для добавления товаров"""
    def __init__(self, driver):
        self._driver = driver

    @allure.step("Добавить товары")
    def add_products(self):
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()