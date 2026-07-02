from employee_management_system.services.employe_service import EmployeeService
from employee_management_system.models.employee import Employee
from employee_management_system.utils.validation import Validation

service = EmployeeService()
validation = Validation();


def employee_menu():
    while True:
        print('\nemployee managemnet system')
        print('1. Add Employee')
        print('2. View Employee')
        print('3', 'Search Employee')
        print('4', 'Update Employee')
        print('5', 'Sort by salary')
        print('6. Delete Employee')
        print('7. Exit')

        choice = input('enter your choice: ')
        if choice == '1':
            emp_id = validation.get_valid_input(
                "Enter Employee ID: ",
                validation.validate_emp_id
            )

            employe_name = validation.get_valid_input(
                "Enter Employee Name: ",
                validation.validate_name
            )

            departments = [
                "IT",
                "HR",
                "Finance",
                "Admin",
                "Marketing"
            ]

            print("\nAvailable Departments:")

            for department in departments:
                print(f"- {department}")

            department = validation.get_valid_input(
                "Enter Department: ",
                validation.validate_department
            )

            salary = validation.get_valid_input(
                "Enter Salary: ",
                validation.validate_salary
            )

            employee = Employee(emp_id, employe_name, department, salary)

            service.add_employee(employee.to_dict())

            print("Employee Added Successfully")

        elif choice == '2':
            employees = service.get_all_employees()
            print("Employee List:", employees)

            for emp in employees:
                print("---------------------")
                print("ID :", emp["emp_id"])
                print("Name :", emp["name"])
                print("Department :", emp["department"])
                print("Salary :", emp["salary"])


        elif choice == '3':
            emp_id = validation.get_valid_input("Enter Employee ID: ",validation.validate_emp_id)

            employee = service.employee_search(emp_id)
            if employee:
                print("Employee Details:", employee['emp_id'])
                print("Employee Details:", employee['name'])
            else:
                print("employee not found")

        elif choice == '4':
            emp_id = validation.get_valid_input(
                "Enter Employee ID: ",
                validation.validate_emp_id
            )

            employee = service.employee_search(emp_id)
            if employee:
                name = validation.get_valid_input(
                    "Enter Employee Name: ",
                    validation.validate_name
                )

                departments = [
                    "IT",
                    "HR",
                    "Finance",
                    "Admin",
                    "Marketing"
                ]

                print("\nAvailable Departments:")

                for department in departments:
                    print(f"- {department}")

                department = validation.get_valid_input(
                    "Enter Department: ",
                    validation.validate_department
                )

                salary = validation.get_valid_input(
                    "Enter Salary: ",
                    validation.validate_salary
                )

                updated_employee = {
                    "emp_id": emp_id,
                    "name": name,
                    "department": department,
                    "salary": salary
                }
                service.update_employee(emp_id, updated_employee)
                print("Employee Updated Successfully")
            else:
                print("employee not found")

        elif choice == '5':
            employee_list = service.sort_by_salary()
            for emp in employee_list:
                print("ID", emp['emp_id'])
                print("Name", emp['name'])
                print("Department", emp['department'])
                print("Salary", emp['salary'])

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
            print("thank you for using this program")
            break
        else:
            print("please enter a valid choice")
