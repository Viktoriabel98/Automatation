from selenium.webdriver.common.by import By

class DataFild:
    def __init__(self, browser):
        self.browser = browser

# Поиск полей для заполнения
    def find_fields(self):
        self.class_first_name = (By.ID, "first-name")
        self.class_last_name = (By.ID, "last-name")
        self.class_address = (By.ID, "address")
        self.class_email = (By.ID, "e-mail")
        self.class_phone = (By.ID, "phone")
        self.class_zip_code = (By.ID, "zip-code")
        self.class_city = (By.ID, "city")
        self.class_country = (By.ID, "country")
        self.class_job_position = (By.ID, "job-position")
        self.class_company = (By.ID, "company")

# получаем значения классов полей
    def get_class_first_name(self):
        return self.browser.find_element(By.ID, "first-name").get_attribute("class")

    def get_class_last_name(self):
        return self.browser.find_element(By.ID, "last-name").get_attribute("class")

    def get_class_address(self):
        return self.browser.find_element(By.ID, "address").get_attribute("class")

    def get_class_email(self):
        return self.browser.find_element(By.ID, "email").get_attribute("class")
    
    def get_class_phone(self):
        return self.browser.find_element(By.ID, "phone").get_attribute("class")

    def get_class_zip_code(self):
        return self.browser.find_element(By.ID, "zip-code").get_attribute("class")

    def get_class_city(self):
        return self.browser.find_element(By.ID, "city").get_attribute("class")

    def get_class_country(self):
        return self.browser.find_element(By.ID, "country").get_attribute("class")

    def get_class_job_position(self):
        return self.browser.find_element(By.ID, "job_position").get_attribute("class")

    def get_class_company(self):
        return self.browser.find_element(By.ID, "company").get_attribute("class")