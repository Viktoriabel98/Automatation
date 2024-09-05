from sqlalchemy import create_engine
from sqlalchemy import text
import allure


class ClientsTable:
    """Класс предоставляет методы для работы с базой данных приложения"""
    __scripts_company = {
        "delete by id": text("delete from company where id = :id_to_delete"),
        "get max id": "select max(id) from company"
    }
    __scripts_employee = {
        "select all employees": text(
            "select * from employee where company_id = :id"),
        "insert new employee": text(
            "insert into employee (first_name, last_name, phone, company_id) values (:first_name, :last_name, :phone, :company_id)"),
        "select employee by id": text(
            "select * from employee where id = :employee_id"),
        "get employee max id": text(
            "select max(id) from employee where company_id = :max_company_id"),
        "delete by id": text("delete from employee where id = :id_to_delete")
    }

    def __init__(self, db_connection_string):
        self.__db = create_engine(db_connection_string)

    @allure.step("БД. Удалить компанию по {id}")
    def delete_company(self, id: int):
        self.__db.execute(self.__scripts_company
                          ["delete by id"], id_to_delete=id)

    @allure.step("БД. Получить максимальный id компании")
    def get_max_id(self) -> int:
        return self.__db.execute(self.__scripts_company
                                 ["get max id"]).fetchall()[0][0]

    @allure.step("БД. Получить список сотрудников компании с id {comp_id}")
    def get_employees(self, comp_id: int) -> dict:
        return self.__db.execute(
            self.__scripts_employee["select all employees"],
            id=comp_id).fetchall()

    @allure.step("БД. Добавить сотрудника с именем {surname} {name}, телефоном {phone_num}, {id}")
    def create_employee(self, surname: str, name: str, phone_num: str, id: int) -> list:
        return self.__db.execute(
            self.__scripts_employee["insert new employee"],
            first_name=surname, last_name=name, phone=phone_num,
            company_id=id)

    @allure.step("БД. Получить сотрудника по id {id}")
    def get_employee_by_id(self, id: int) -> list:
        return self.__db.execute(
            self.__scripts_employee["select employee by id"],
            employee_id=id).fetchall()

    @allure.step("БД. Получить максимальный id сотрудника")
    def get_max_employee_id(self, id: int) -> int:
        return self.__db.execute(
            self.__scripts_employee["get employee max id"],
            max_company_id=id).fetchall()[0][0]

    @allure.step("БД. Удалить сотрудника с id {id}")
    def delete_employee(self, id: int):
        self.__db.execute(self.__scripts_employee["delete by id"],
                          id_to_delete=id)