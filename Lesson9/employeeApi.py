import requests
from data import *


class EmployeeApi:

    def __init__(self, url):
        self.url = url

    # получение списка сотрудников компании
    def get_employee_list(self, company_id):
        resp = requests.get(self.url + '/employee?company=' + str(company_id))
        return resp.json()

    # авторизация
    def get_token(self, authorization):
        resp = requests.post(self.url + '/auth/login', json=authorization)
        return resp.json()["userToken"]
    # добавление нового сотрудника

    def create_employee(self, firstname, lastname,
                        companyId, email, phone, isActive):
        employee = {
            'firstName': firstname,
            'lastName': lastname,
            'companyId': companyId,
            'email': email,
            'phone': phone,
            'isActive': isActive
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token(authorization)
        resp = requests.post(self.url + '/employee',
                             json=employee, headers=my_headers)
        return resp.json()
    # получение сотрудника по id

    def get_employee_by_id(self, employee_id):
        resp = requests.get(self.url + '/employee/' + str(employee_id))
        return resp.json()
    # изменение информации о сотруднике

    def change_info(
            self, employee_id, new_lastname, new_phone, is_active):
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