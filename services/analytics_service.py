
from repositories.analytics_repository import AnalyticsRepository
from exceptions.employee_exception import (
    EmployeeNotFoundError,

)

class DataAnalytics:
    def __init__(self):
        self.repository = AnalyticsRepository()

    def total_employees(self, db):
        return self.repository.total_employees(db)

    def highest_salary_employee(self,db) :
        return self.repository.highest_salary_employee(db)


    def lowest_salary_employee(self,db) :
        return self.repository.lowest_salary_employee(db)

    def average_salary_employee(self,db) :
        return self.repository.average_salary_employee(db)

    def group_by_department(self,db) :
        rows = self.repository.group_by_department(db)

        return {
            department: count
            for department, count in rows
        }

    def sort_by_salary(self,db) :
        return  self.repository.sort_by_salary(db)


    def employee_by_department(self,db, department):
        employees = self.repository.employee_by_department(
            db, department
        )

        if not employees:
            raise EmployeeNotFoundError(
                f"No employees found in department {department}."
            )

        return employees

    def employee_above_salary(self, db, salary):
        employees = self.repository.employee_above_salary(
            db, salary
        )
        print("Employees:", employees)
        if not employees:
            raise EmployeeNotFoundError(
                f"No employees found above salary {salary}."
            )

        return employees