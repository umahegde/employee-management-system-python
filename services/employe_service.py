from exceptions.employee_exception import (
    EmployeeNotFoundError,
    DuplicateEmployeeError,

)
from repositories.employee_repository import EmployeeRepository
from models.employee_model import Employee

class EmployeeService:
    def __init__(self):
        self.repository = EmployeeRepository()


    def add_employee(self, db, employee_data):
        if self.repository.employee_exists(db, employee_data["emp_id"]):
            raise DuplicateEmployeeError(
                f"Employee {employee_data['emp_id']} already exists."
            )

        employee = Employee(**employee_data)

        return self.repository.add_employee(db, employee)

    def get_all_employees(self,db)->list[dict]:
        employees = self.repository.get_all_employees(db)
        return employees


    def search_employee(self, db, emp_id):
        employee = self.repository.get_employee(db, emp_id)

        if employee is None:
            raise EmployeeNotFoundError(
                f"Employee {emp_id} not found."
            )

        return employee

    def delete_employee(self,db,emp_id:str):
        employee = self.repository.delete_employee(db, emp_id)

        if employee is None:
            raise EmployeeNotFoundError(
                f"Employee {emp_id} not found."
            )
        return employee

    def update_employee(self,db, emp_id:str,update_employee):
        employee = self.repository.update_employee(db,emp_id,update_employee.salary)
        return employee


