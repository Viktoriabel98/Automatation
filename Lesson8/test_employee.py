from employeeAPI import Employee
from companyAPI import CompanyAPI


comp = CompanyAPI("https://x-clients-be.onrender.com")
api = Employee("https://x-clients-be.onrender.com")

company_id = comp.create_company('Yamal', 'Helicopter')

def test_get_employees_list():
    body = api.get_employee_list(company_id)
    assert len(body) > 0


def test_add_new_employee():
    # создание нового сотрудника
    result = api.create_employee('Peter', 'Petrov', company_id,
                                 'api@kio.com', '88005554545', True)
    employee_id = result['id']
    assert employee_id is not None
    # получить сотрудника по id
    new_employee = api.get_employee_by_id(employee_id)
    assert new_employee['id'] == employee_id


def test_change_employee_info():
    result = api.create_employee('Smith', 'qwe@rty.ru', company_id,
                                 'api@kio.com', '88005554545', True)
    employee_id = result['id']
    changed = api.change_info(employee_id, 'Johns', 'kdl@nndn.ru', '88005550000')
    assert changed["id"] == employee_id
    assert changed["isActive"] == True