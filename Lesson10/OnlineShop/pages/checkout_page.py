from selenium.webdriver.common.by import By
from data_shop import *
import allure


class CheckoutPage:
    """Класс предоставляет метод для заполнения формы с информацией о покупателе"""
    def __init__(self, driver):
        self._driver = driver

    @allure.step("Заполнить форму и нажать на кнопку Continue")
    def input_data(self):
        self._driver.find_element(By.ID, "first-name").send_keys(first_name)
        self._driver.find_element(By.ID, "last-name").send_keys(last_name)
        self._driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self._driver.find_element(By.ID, "continue").click()