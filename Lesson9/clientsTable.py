from sqlalchemy import create_engine
from sqlalchemy import text


class ClientsTable:
    __scripts_company = {
        "select": "select * from company where deleted_at is Null",
        "select by id": text(
            "select * from company where deleted_at is Null and id = :select_id"),
        "select only active":
        "select * from company where deleted_at is Null and is_active = true",
        "delete by id": text("delete from company where id = :id_to_delete"),
        "insert new": text("insert into company(\"name\") values (:new_name)"),
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

    # помогаторы для компании
    def get_companies(self):
        return self.__db.execute(self.__scripts_company["select"]).fetchall()

    def get_company_by_id(self, id):
        return self.__db.execute(
            self.__scripts_company["select by id"],
            select_id=id).fetchall()

    def get_active_companies(self):
        return self.__db.execute(self.__scripts_company
                                 ["select only active"]).fetchall()

    def delete_company(self, id):
        self.__db.execute(self.__scripts_company
                          ["delete by id"], id_to_delete=id)

    def create(self, name):
        self.__db.execute(self.__scripts_company["insert new"], new_name=name)

    def get_max_id(self):
        return self.__db.execute(self.__scripts_company
                                 ["get max id"]).fetchall()[0][0]

    # помогаторы для сотрудников
    def get_employees(self, comp_id):
        return self.__db.execute(
            self.__scripts_employee["select all employees"],
            id=comp_id).fetchall()

    def create_employee(self, surname, name, phone_num, id):
        return self.__db.execute(
            self.__scripts_employee["insert new employee"],
            first_name=surname, last_name=name, phone=phone_num,
            company_id=id)

    def get_employee_by_id(self, id):
        return self.__db.execute(
            self.__scripts_employee["select employee by id"],
            employee_id=id).fetchall()

    def get_max_employee_id(self, id):
        return self.__db.execute(
            self.__scripts_employee["get employee max id"],
            max_company_id=id).fetchall()[0][0]

    def delete_employee(self, id):
        self.__db.execute(self.__scripts_employee["delete by id"],
                          id_to_delete=id)