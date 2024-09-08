from employeeApi import EmployeeApi
from clientsTable import ClientsTable
import allure

api = EmployeeApi("https://x-clients-be.onrender.com")
db = ClientsTable("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")

@allure.title("Получение полного списка сотрудников компании")
@allure.description("Создать новую компанию, получить ее id, в нее добавить нового сотрудника. Сравнить списки сотрудников через БД и API. Удалить сотрудника из компании и саму компанию.")
@allure.feature("GET")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_employees_list():
    api.create_company('Aviasales', 'Tickets')
    max_id = db.get_max_id()
    db.create_employee('Mur', 'Sally', '834922', max_id)
    db_result = db.get_employees(max_id)
    api_result = api.get_employee_list(max_id)

    employee_id = db.get_max_employee_id(max_id)
    db.delete_employee(employee_id)
    db.delete_company(max_id)

    with allure.step("Сравнить размеры двух списков"):
        assert len(api_result) == len(db_result)

@allure.title("Добавление нового сотрудника")
@allure.description("Добавить нового сотрудника и убедиться, что его id равны в БД и API.")
@allure.feature("ADD")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_new_employee():
    api.create_company('Aviasales', 'Tickets')
    max_company_id = db.get_max_id()
    new_employee = db.create_employee(
        'Parker', 'Peter', '8999666', max_company_id)
    
    with allure.step("Убедиться, что инфо о новом сотруднике не пустой список"):
        assert new_employee is not None
    max_employee_id = db.get_max_employee_id(max_company_id)
    new_employee_db = db.get_employee_by_id(max_employee_id)

    new_employee_api = api.get_employee_by_id(max_employee_id)

    db.delete_employee(max_employee_id)
    db.delete_company(max_company_id)

    with allure.step("Сравнить id"):
        assert new_employee_api["id"] == new_employee_db[0][0]

@allure.title("Изменение информации о сотруднике")
@allure.description("Добавить нового сотрудника, изменить информацию о нем.")
@allure.feature("CHANGE")
@allure.severity(allure.severity_level.CRITICAL)
def test_change_employee_info():
    api.create_company('Aviasales', 'Tickets')
    max_company_id = db.get_max_id()
    db.create_employee('Parker', 'Peter', '8999666', max_company_id)
    max_employee_id = db.get_max_employee_id(max_company_id)

    changed = api.change_info(max_employee_id, 'PARKER', '88005550000', False)

    db.delete_employee(max_employee_id)
    db.delete_company(max_company_id)

    with allure.step("Сравнить id, isActive"):
        assert changed["id"] == max_employee_id
        assert changed["isActive"] == False