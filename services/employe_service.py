import json
from utils.constants import JSON_FILE
from utils.logger import logger
from exceptions.employee_exception import (
    EmployeeNotFoundError,
    DuplicateEmployeeError,
    EmployeeDataFileError
)
class EmployeeService:

    def load_data(self)->list[dict]:
        try:
            with open(JSON_FILE) as json_file:
                return  json.load(json_file)

        except FileNotFoundError:
            logger.exception("Employee data file not found.")
            raise EmployeeDataFileError("Employee data file not found.")


    def save_data(self,employees:list[dict])->None:
        try:
            with open(JSON_FILE, 'w') as outfile:
                json.dump(employees, outfile, indent=4)
            logger.info("Employee data saved successfully.")
        except Exception:
            logger.exception("Failed to save employee data.")

    def add_employee(self, employee:dict):
        employees = self.load_data()
        for emp in employees:
            if emp["emp_id"] == employee["emp_id"]:
                raise DuplicateEmployeeError(
                    f"Employee ID {employee['emp_id']} already exists."
                )
        employees.append(employee)
        self.save_data(employees)

    def get_all_employees(self)->list[dict]:
       return  self.load_data()


    def search_employee(self,emp_id:str)->dict:
        employees = self.load_data()
        for emp in employees  :
            if emp["emp_id"] == emp_id:
                return  emp

        raise EmployeeNotFoundError(
                f"Employee {emp_id} not found."
            )

    def sort_by_salary(self)->list[dict]:
        employees = self.load_data()
        employees.sort(
            key=lambda employee: float(employee["salary"]),
            reverse=True
        )
        return employees
    def delete_employee(self,emp_id:str)->bool:
        employees = self.load_data()
        for emp in employees :
            if emp["emp_id"] == emp_id:
                employees.remove(emp)
                self.save_data(employees)
                return True

        raise EmployeeNotFoundError(
                f"Employee {emp_id} not found."
            )


    def update_employee(self, emp_id:str,update_employee):
        employees = self.load_data()
        for index, employee in enumerate(employees):

            if employee["emp_id"] == emp_id:
                employees[index] = update_employee

                self.save_data(employees)

                return True

        raise EmployeeNotFoundError(
                f"Employee {emp_id} not found."
            )


