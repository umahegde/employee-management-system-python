from sqlalchemy import select
from models.employee_model import Employee
class EmployeeRepository:

    def add_employee(self, db, employee):
        db.add(employee)
        db.commit()
        db.refresh(employee)

        return employee

    def update_employee(self, db, emp_id, salary):
        statement = select(Employee).where(
            Employee.emp_id == emp_id
        )

        employee = db.execute(statement).scalar_one_or_none()

        if employee is None:
            return None

        employee.salary = salary

        db.commit()

        db.refresh(employee)
        return employee

    def delete_employee(self, db, emp_id):
            statement = select(Employee).where(
                Employee.emp_id == emp_id
            )

            employee = db.execute(statement).scalar_one_or_none()

            if employee is None:
                return None

            db.delete(employee)
            db.commit()
            return employee

    def get_employee(self, db, emp_id):

        statement = select(Employee).where(
                Employee.emp_id == emp_id
            )

        employee = db.execute(statement).scalar_one_or_none()

        return employee

    def get_all_employees(self, db,page, page_size):
        statement = select(Employee).order_by(
            Employee.emp_id
        ).offset((page - 1) * page_size).limit(page_size)
        result = db.execute(statement)
        employees = result.scalars().all()
        return employees

    def employee_exists(self, db, emp_id):
        statement = select(Employee).where(
            Employee.emp_id == emp_id
        )

        employee = db.execute(statement).scalar_one_or_none()

        return employee is not None


