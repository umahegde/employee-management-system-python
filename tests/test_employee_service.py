from unittest import result

from services.employe_service import EmployeeService
from models.employee import Employee
from exceptions.employee_exception import EmployeeNotFoundError, DuplicateEmployeeError,EmployeeDataFileError
import pytest


@pytest.fixture
def service():
    return EmployeeService()

class TestEmployeeService:

    def test_add_employee(self,service):
        employee = Employee('23',"Krish",'IT',20000)
        service.add_employee(employee.to_dict() )
        result = service.search_employee("23")
        assert result["name"] == "Krish"

    def test_add_duplicate_employee(self,service):
        employee = Employee('23', "Krishna", 'IT', 20000)
        with pytest.raises(DuplicateEmployeeError):
            service.add_employee(employee.to_dict())

    def test_get_all_employees(self,service):

        result = service.get_all_employees()
        assert result[0]["emp_id"] == "29"
        assert result[0]["salary"] == 10000
        assert result[0]["department"] == "IT"
        assert result[0]["name"] == "Dyuti"

    def test_search_employee_success(self,service):
        result = service.search_employee("1")
        assert result["name"] == "Raj"
        assert result["salary"] == 25000
        assert result['department'] == "Marketing"
        assert result["emp_id"] == "1"

    def test_search_employee_not_found(self,service):
        with pytest.raises(EmployeeNotFoundError) :
            service.search_employee("60")

    def test_sort_by_salary(self,service):
        result = service.sort_by_salary()
        assert result[0]["salary"] >= result[1]["salary"]

    def test_delete_employee_success(self,service):
        assert service.delete_employee("23")

    def test_delete_employee_not_found(self,service):

        with pytest.raises(EmployeeNotFoundError):
            service.delete_employee("60")

    def test_update_employee_success(self,service):
        update_employee = Employee('1', "Rajendra", 'Marketing', 25000)
        status = service.update_employee('1',update_employee.to_dict())
        assert status is True

    def test_update_employee_not_found(self,service):
        update_employee = Employee('100', "Raj", 'Marketing', 67687)

        with pytest.raises(EmployeeNotFoundError):
             service.update_employee('100', update_employee.to_dict())



