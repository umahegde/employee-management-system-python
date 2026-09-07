from data.database import SessionLocal
from models.employee_model import Employee
from sqlalchemy import select
from repositories.employee_repository import EmployeeRepository

repository = EmployeeRepository()
db = SessionLocal()

employee = Employee(
    emp_id="108",
    name="Tanmayi",
    department="HR",
    salary=45000
)

repository.add_employee(db, employee)

print("Employee added successfully!")
repository.update_employee(db,103,45000)
print("Employee updated successfully!")

db.close()



# def add_employee(emp_id, name, department, salary):
#     db = SessionLocal()
#
#     employee = Employee(
#         emp_id=emp_id,
#         name=name,
#         department=department,
#         salary=salary
#     )
#
#     db.add(employee)
#     db.commit()
#
#     print("Employee added successfully!")
#
#     db.close()
# #
# def update_employee(emp_id, salary):
#     db = SessionLocal()

    # statement = select(Employee).where(
    #     Employee.emp_id == emp_id
    # )
    #
    # employee = db.execute(statement).scalar_one_or_none()
    #
    # if employee is None:
    #     print("Employee not found!")
    #     db.close()
    #     return
    #
    # employee.salary = salary
    #
    # db.commit()

#     print("Employee updated successfully!")
#
#     db.close()
#
#
# def get_employee(emp_id):
#     db = SessionLocal()
#
#     statement = select(Employee).where(
#         Employee.emp_id == emp_id
#     )
#
#     employee = db.execute(statement).scalar_one_or_none()
#
#     db.close()
#
#     return employee
# def delete_employee(emp_id):
#     db = SessionLocal()
#
#     statement = select(Employee).where(
#         Employee.emp_id == emp_id
#     )
#
#     employee = db.execute(statement).scalar_one_or_none()
#
#     if employee is None:
#         print("Employee not found!")
#         db.close()
#         return
#
#     db.delete(employee)
#     db.commit()

#     print("Employee deleted successfully!")
#
#     db.close()
