from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Lesson7.const import Test_URL
from Lesson7.Data_types.data import *

class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(Test_URL)

    def filling_in_the_fields(self):
        self.browser.find_element(By.NAME, "first-name").send_keys(first_name)
        self.browser.find_element(By.NAME, "last-name").send_keys(last_name)
        self.browser.find_element(By.NAME, "address").send_keys(address)
        self.browser.find_element(By.NAME, "e-mail").send_keys(email)
        self.browser.find_element(By.NAME, "phone").send_keys(phone)
        self.browser.find_element(By.NAME, "zip-code").send_keys(zip_code)
        self.browser.find_element(By.NAME, "city").send_keys(city)
        self.browser.find_element(By.NAME, "country").send_keys(country)
        self.browser.find_element(By.NAME, "job-position").send_keys(job_position)
        self.browser.find_element(By.NAME, "company").send_keys(company)

    def click_submit_button(self):
        WebDriverWait(self.browser, 40, 0.1).until(EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()    
    



