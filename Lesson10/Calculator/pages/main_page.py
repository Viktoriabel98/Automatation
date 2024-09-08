from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:
    """Класс предоставляет методы для работы на главное странице приложения"""
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.maximize_window()

    @allure.step("Установить время ожидания {delay}")
    def calculator_waits(self, delay: int) -> None:
        self._driver.find_element(By.ID, "delay").clear()
        self._driver.find_element(By.ID, "delay").send_keys(delay)

    @allure.step("Посчитать сумму")
    def sum(self, first_num: str, second_num: str, 
            operator: str, equal: str, wait_time: str, result: str) -> str:
        self._driver.find_element(By.XPATH, f'//span[text()="{first_num}"]').click()
        self._driver.find_element(By.XPATH, f'//span[text()="{operator}"]').click()
        self._driver.find_element(By.XPATH, f'//span[text()="{second_num}"]').click()
        self._driver.find_element(By.XPATH, f'//span[text()="{equal}"]').click()
        waiter = WebDriverWait(self._driver, wait_time)
        waiter.until(EC.text_to_be_present_in_element(
            (By.XPATH, f'//div[text()="{result}"]'), result))