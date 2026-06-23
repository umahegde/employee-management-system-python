# This is a sample Python script.
import employe_service
# Press ⌃F5 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from employee import Employee
from employe_service import EmployeeService
from validation import validate_emp_id
from validation import validate_name
from validation import validate_department
from validation import validate_salary
from validation import  get_valid_input


service = EmployeeService()

while  True:
     print('\nemployee managemnet system')
     print('1. Add Employee')
     print('2. View Employee')
     print('3','Search Employee')
     print('4','Update Employee')
     print('5', 'Sort by salary')
     print('6. Delete Employee')
     print('7. Exit')

     choice =  input('enter your choice: ')
     if choice == '1':
         emp_id = get_valid_input(
             "Enter Employee ID: ",
             validate_emp_id
         )

         name = get_valid_input(
             "Enter Employee Name: ",
             validate_name
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

         department = get_valid_input(
             "Enter Department: ",
             validate_department
         )

         salary = get_valid_input(
             "Enter Salary: ",
             validate_salary
         )

         employee = Employee(emp_id, name, department, salary)

         service.add_employee(employee.to_dict())

         print("Employee Added Successfully")

     elif choice == '2':
         employees = service.get_all_employees()
         print("Employee List:",employees)

         for emp in employees:
             print("---------------------")
             print("ID :", emp["emp_id"])
             print("Name :", emp["name"])
             print("Department :", emp["department"])
             print("Salary :", emp["salary"])


     elif choice == '3':
         emp_id = get_valid_input(
             "Enter Employee ID: ",
             validate_emp_id
         )

         employee = service.employee_search(emp_id)
         if employee:
             print("Employee Details:" ,employee['emp_id'])
             print("Employee Details:" ,employee['name'])
         else:
             print("employee not found")

     elif choice == '4':
         emp_id = get_valid_input(
             "Enter Employee ID: ",
             validate_emp_id
         )

         employee = service.employee_search(emp_id)
         if employee:
             name = get_valid_input(
                 "Enter Employee Name: ",
                 validate_name
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

             department = get_valid_input(
                 "Enter Department: ",
                 validate_department
             )

             salary = get_valid_input(
                 "Enter Salary: ",
                 validate_salary
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
         employees = service.get_all_employees()
         employee_list = service.sort_by_salary()
         for emp in employee_list:
             print("ID",emp['emp_id'])
             print("Name",emp['name'])
             print("Department",emp['department'])
             print("Salary",emp['salary'])
     elif choice == '6':
         emp_id = get_valid_input(
             "Enter Employee ID: ",
             validate_emp_id
         )

         isDeleted = service.delete_employee(emp_id)
         if isDeleted: print("Employee Deleted Successfully")
         else : print("employee not found")

     elif choice == '7':
        print("thank you for using this program")
        break
     else:
         print("please enter a valid choice")







