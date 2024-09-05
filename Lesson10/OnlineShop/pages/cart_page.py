from selenium.webdriver.common.by import By
import allure


class CartPage:
    """Класс предоставляет метод для работы с корзиной товаров"""
    def __init__(self, driver):
        self._driver = driver

    @allure.step("Зайти на сайт корзины")
    def get(self):
        self._driver.get("https://www.saucedemo.com/cart.html")

    @allure.step("Нажать кнопку Checkout")
    def checkout(self):
        self._driver.find_element(By.ID, "checkout").click()