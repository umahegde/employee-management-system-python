import json
from employee_management_system.utils.constants import DATA_FILE

class EmployeeService:

    def load_data(self):
        try:
            with open(DATA_FILE) as json_file:
                return  json.load(json_file)


        except FileNotFoundError:
            print("File not found")
            return []


    def save_data(self,employees):

        with open(DATA_FILE, 'w') as outfile:
            json.dump(employees, outfile, indent = 4)

    def add_employee(self, employee):
        employees = self.load_data()
        employees.append(employee)
        self.save_data(employees)

    def get_all_employees(self):
       return  self.load_data()


    def search_employee(self,emp_id):
        employees = self.load_data()
        for emp in employees  :
            if emp["emp_id"] == emp_id:
                return  emp
        return None
    def sort_by_salary(self):
        employees = self.load_data()
        employees.sort(
            key=lambda employee: float(employee["salary"]),
            reverse=True
        )
        return employees
    def delete_employee(self,emp_id):
        employees = self.load_data()
        for emp in employees :
            if emp["emp_id"] == emp_id:
                employees.remove(emp)
                self.save_data(employees)
                return True
        return False


    def updated_employee(self, emp_id,update_employee):
        employees = self.load_data()
        for index, employee in enumerate(employees):

            if employee["emp_id"] == emp_id:
                employees[index] = update_employee

                self.save_data(employees)

                return True

        return False


