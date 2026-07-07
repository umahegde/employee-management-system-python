from services.employe_service import EmployeeService
from models.employee import Employee
from utils.validation import Validation
from utils.constants import DEPARTMENTS
from utils.display import display_employee_details
from utils.logger import logger
from exceptions.employee_exception import (
    EmployeeNotFoundError,
    DuplicateEmployeeError,
)
service = EmployeeService()
validation = Validation()


def get_employee_details(include_emp_id=True):
    emp_id = None

    if include_emp_id:
        emp_id = validation.get_valid_input(
            "Enter Employee ID: ",
             validation.validate_emp_id
        )

    employee_name = validation.get_valid_input(
        "Enter Employee Name: ",
        validation.validate_name
    )

    print("\nAvailable Departments:")
    for department in DEPARTMENTS:
        print(f"- {department}")

    department = validation.get_valid_input(
        "Enter Department: ",
        validation.validate_department
    )

    salary = validation.get_valid_input(
        "Enter Salary: ",
        validation.validate_salary
    )
    return  Employee(emp_id, employee_name, department, salary)

def employee_menu():
    while True:
        print('\nEmployee managemnet system')
        print('1. Add Employee')
        print('2. View Employee')
        print('3.', 'Search Employee')
        print('4.', 'Update Employee')
        print('5.', 'Sort by salary')
        print('6.',' Delete Employee')
        print('7.', 'Exit')

        choice = input('enter your choice: ')
        if choice == '1':

            employee = get_employee_details()

            try:
                service.add_employee(employee.to_dict())
                print("Employee Added Successfully")
                print("Employee Added Successfully")
                logger.info(f"Employee added successfully. Employee ID: {employee.emp_id}")

            except DuplicateEmployeeError as error:
                print(error)

        elif choice == '2':
            employees = service.get_all_employees()
            for emp in employees:
                display_employee_details(emp)

        elif choice == '3':
            emp_id = validation.get_valid_input("Enter Employee ID: ",validation.validate_emp_id)

            try:
                employee = service.search_employee(emp_id)
                display_employee_details(employee)

            except EmployeeNotFoundError as error:
                print(error)
                logger.warning(str(error))

        elif choice == '4':
            emp_id = validation.get_valid_input(
                "Enter Employee ID: ",
                validation.validate_emp_id
            )
            try:
                service.search_employee(emp_id)
                update_details = get_employee_details(False)
                updated_employee = {
                        "emp_id": emp_id,
                        "name": update_details.name,
                        "department": update_details.department,
                        "salary": update_details.salary
                }
                service.update_employee(emp_id, updated_employee)
                print("Employee Updated Successfully")
                logger.info(f"Employee {emp_id} Updated Successfully")

            except EmployeeNotFoundError as error:
                print(error)
                logger.warning(str(error))

        elif choice == '5':
            employee_list = service.sort_by_salary()
            for emp in employee_list:
                display_employee_details(emp)

        elif choice == '6':
            emp_id = validation.get_valid_input(
                "Enter Employee ID: ",
                validation.validate_emp_id
            )

            is_deleted = service.delete_employee(emp_id)
            if is_deleted:
                print(f"Employee {emp_id} Deleted Successfully")
                logger.info(f"Employee {emp_id} Deleted Successfully")
            else:
                print(f"Employee not found. Employee ID: {emp_id}.")
                logger.warning(f"Employee not found. Employee ID: {emp_id}.")

        elif choice == '7':
            print("Thank you for using this program")
            break
        else:
            print("Please enter a valid choice")

