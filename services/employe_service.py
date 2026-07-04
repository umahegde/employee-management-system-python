import json
from employee_management_system.utils.constants import DATA_FILE
from employee_management_system.utils.logger import logger

class EmployeeService:

    def load_data(self)->list[dict]:
        try:
            with open(DATA_FILE) as json_file:
                return  json.load(json_file)

        except FileNotFoundError:
            logger.exception("Employee data file not found.")
            return []


    def save_data(self,employees:list[dict])->None:
        try:
            with open(DATA_FILE, 'w') as outfile:
                json.dump(employees, outfile, indent=4)
            logger.info("Employee data saved successfully.")
        except Exception:
            logger.exception("Failed to save employee data.")

    def add_employee(self, employee:dict)->None:
        employees = self.load_data()
        employees.append(employee)
        self.save_data(employees)

    def get_all_employees(self)->list[dict]:
       return  self.load_data()


    def search_employee(self,emp_id:str)->dict | None:
        employees = self.load_data()
        for emp in employees  :
            if emp["emp_id"] == emp_id:
                return  emp
        return None

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
        return False


    def update_employee(self, emp_id:str,update_employee)->bool:
        employees = self.load_data()
        for index, employee in enumerate(employees):

            if employee["emp_id"] == emp_id:
                employees[index] = update_employee

                self.save_data(employees)

                return True

        return False


