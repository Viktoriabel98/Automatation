import requests
from data import *
import allure


class EmployeeApi:
    """Класс предоставляет методы для работы с сервером приложения"""
    def __init__(self, url):
        self.url = url
    
    @allure.step("API.Создать компанию {name} ({description})")
    def create_company(self, name: str, description: str) -> int:
        company = {
            'name': name,
            'description': description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token(authorization)
        resp = requests.post(
            self.url + '/company', json=company, headers=my_headers)
        return resp.json()['id']
    
    @allure.step("API. Получить список сотрудников компании с id = {company_id}")
    def get_employee_list(self, company_id: int) -> list:
        resp = requests.get(self.url + '/employee?company=' + str(company_id))
        return resp.json()

    @allure.step(
            "API.Получить токен авторизации для пользователя {authorization}")
    def get_token(self, authorization: dict) -> str:
        resp = requests.post(self.url + '/auth/login', json=authorization)
        return resp.json()["userToken"]
    
    @allure.step("API. Получить инфо о сотруднике по id {employee_id}")
    def get_employee_by_id(self, employee_id: int) -> dict:
        resp = requests.get(self.url + '/employee/' + str(employee_id))
        return resp.json()
    
    @allure.step("API. Изменить инфо о сотруднике по id = {employee_id}")
    def change_info(
            self, employee_id: int, new_lastname: str, new_phone: str, is_active: bool) -> dict:
        my_headers = {}
        my_headers["x-client-token"] = self.get_token(authorization)
        new_employee = {
            "lastName": new_lastname,
            "phone": new_phone,
            "isActive": is_active
            }
        resp = requests.patch(self.url + '/employee/' + str(employee_id),
                              headers=my_headers, json=new_employee)
        return resp.json()

    