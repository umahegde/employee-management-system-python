from models.employee_model import Employee
from sqlalchemy import func, select

class AnalyticsRepository:

    def total_employees(self, db):
        statement = select(func.count(Employee.emp_id))

        result = db.execute(statement)

        return result.scalar()

    def highest_salary_employee(self,db):
        statement = select(func.max(Employee.salary))
        result = db.execute(statement)
        return result.scalar()

    def lowest_salary_employee(self, db):
        statement = select(func.min(Employee.salary))
        result = db.execute(statement)
        return result.scalar()

    def average_salary_employee(self,db):
        statement = select(func.avg(Employee.salary))
        result = db.execute(statement)
        return result.scalar()

    def group_by_department(self,db) :
        statement = select(
            Employee.department,
            func.count(Employee.emp_id)
        ).group_by(Employee.department)
        result = db.execute(statement)
        return result.all()

    def sort_by_salary(self, db):
        statement = select(Employee).order_by(Employee.salary.desc())
        result = db.execute(statement)
        return result.scalars().all()

    def employee_by_department(self,db,department):
        statement = select(Employee).where(Employee.department == department)
        result = db.execute(statement)
        return result.scalars().all()
    def employee_above_salary(self,db,salary):
        statement = select(Employee).where(Employee.salary > salary)
        result = db.execute(statement)
        return result.scalars().all()

#