from employee_management_system.services.employe_service import EmployeeService


employee_service = EmployeeService()

class DataAnalytics:


    def total_employees(self)->int:
        employees = employee_service.get_all_employees()
        return len(employees)


    def employee_by_department(self, department:str)->list[dict]:
        employees = employee_service.get_all_employees()
        department_employee = [employee for employee in employees if employee["department"] == department]
        return department_employee

    def highest_salary_employee(self)->dict | None:
        employees = employee_service.get_all_employees()
        return max(employees, key=lambda emp: float(emp["salary"]))


    def lowest_salary_employee(self)->dict | None:
        employees = employee_service.get_all_employees()
        return min(employees, key=lambda emp: float(emp["salary"]))

    def average_salary_employee(self)->float:
        employees = employee_service.get_all_employees()
        if not employees:
            return 0
        salary = [int(employee["salary"]) for employee in employees ]
        return sum(salary)/len(employees)


    def employee_above_salary(self, salary:str)->list[dict]:
        employees = employee_service.get_all_employees()
        return  [employee for employee in employees if float(employee["salary"]) > float(salary) ]


    def group_by_department(self)->dict[str,int]:
        employees = employee_service.get_all_employees()
        department_count = {}
        for employee in employees:
            if employee["department"] not in department_count:
                department_count[employee["department"]] = 1
            else:
                department_count[employee["department"]] += 1
        return department_count




