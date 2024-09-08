from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import *
import allure


class MainPage:
    """Класс предоставляет методы для заполнения полей формы"""
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.maximize_window()

    @allure.step("Заполнить все поля данными")
    def input_data(self):
        self._driver.find_element(By.CSS_SELECTOR,
                                  "input[name='first-name']").send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR,
                                  "input[name='last-name']"
                                  ).send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR,
                                  "input[name='address']"
                                  ).send_keys(address)
        self._driver.find_element(By.CSS_SELECTOR,
                                  "input[name='e-mail']"
                                  ).send_keys(email)
        self._driver.find_element(By.CSS_SELECTOR,
                                  "input[name='phone']"
                                  ).send_keys(phone_number)
        self._driver.find_element(By.CSS_SELECTOR,
                                  "input[name='city']").send_keys(city)
        self._driver.find_element(By.CSS_SELECTOR,
                                  "input[name='country']"
                                  ).send_keys(country)
        self._driver.find_element(By.CSS_SELECTOR,
                                  "input[name='job-position']").send_keys(job_position)
        self._driver.find_element(By.CSS_SELECTOR,
                                  "input[name='company']").send_keys(company)
        waiter = WebDriverWait(self._driver, 15)
        waiter.until(EC.element_to_be_clickable(
            (By.TAG_NAME, "button")))

    @allure.step("Нажать на кнопку Submit")
    def click_button_submit(self):
        self._driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']").click()