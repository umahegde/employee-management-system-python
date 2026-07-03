from employee_management_system.services.employe_service import EmployeeService
from employee_management_system.models.employee import Employee
from employee_management_system.utils.validation import Validation
from employee_management_system.utils.constants import DEPARTMENTS
from utils.display import display_employee_details

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
        print('\nemployee managemnet system')
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

            service.add_employee(employee.to_dict())

            print("Employee Added Successfully")

        elif choice == '2':
            employees = service.get_all_employees()
            for emp in employees:
                display_employee_details(emp)

        elif choice == '3':
            emp_id = validation.get_valid_input("Enter Employee ID: ",validation.validate_emp_id)

            employee = service.employee_search(emp_id)
            if employee:
                display_employee_details(employee)
            else:
                print("employee not found")

        elif choice == '4':
            emp_id = validation.get_valid_input(
                "Enter Employee ID: ",
                validation.validate_emp_id
            )

            employee = service.search_employee(emp_id)
            if employee:
                update_details = get_employee_details(False)
                updated_employee = {
                    "emp_id": emp_id,
                    "name": update_details.name,
                    "department": update_details.department,
                    "salary": update_details.salary
                }
                service.updated_employee(emp_id, updated_employee)
                print("Employee Updated Successfully")
            else:
                print("employee not found")

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
                print("Employee Deleted Successfully")
            else:
                print("employee not found")

        elif choice == '7':
            print("Thank you for using this program")
            break
        else:
            print("please enter a valid choice")
