from employee_management_system.services.employe_service import EmployeeService


employee_service = EmployeeService()

class DataAnalytics:


    def total_employees(self):
        employees = employee_service.load_data()
        print("Employees : ", employees)
        total_employees = len(employees)
        print("total Employeess",total_employees)
        return total_employees
        return total_employees

    def employee_by_department(self, department):
        employees = employee_service.load_data()
        department_employee = [employee for employee in employees if employee["department"] == department]
        return department_employee

    def highest_salary_employee(self):
        employees = employee_service.load_data()
        highest_paid_employee = sorted(employees,key = lambda emp: emp["salary"], reverse=True)
        return highest_paid_employee[0]

    def lowest_salary_employee(self):
        employees = employee_service.load_data()
        lowest_paid_employee = sorted(employees, key= lambda emp: emp["salary"])
        return lowest_paid_employee[0]

    def average_salary_employee(self):
        employees = employee_service.load_data()
        if not employees:
            return 0
        salary = [int(employee["salary"]) for employee in employees ]
        average_salary = sum(salary)/len(employees)
        return average_salary

    def employee_above_salary(self, salary):
        employees = employee_service.load_data()
        print(employees)
        above_salary = [employee for employee in employees if employee["salary"] > salary ]
        print(above_salary)
        return above_salary
        return above_salary

    def group_by_deparment(self):
        employees = employee_service.load_data()
        department_count = {}
        for employee in employees:
            if employee["department"] not in department_count:
                department_count[employee["department"]] = 1
            else:
                department_count[employee["department"]] += 1
        return department_count;




