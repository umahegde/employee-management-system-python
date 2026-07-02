from pip._internal.utils import deprecation

from services.analytics import DataAnalytics
from services.employe_service import EmployeeService

analytics = DataAnalytics()
service = EmployeeService()

def analytics_menu():

    while True:

        print("\nAnalytics Menu")

        print("1. Total Employees")
        print("2. Highest Salary")
        print("3. Lowest Salary")
        print("4. List Employee By Department")
        print("5. Employee Above Salary")
        print("6. Group Employee By Department")
        print("7. Average Salary of Employee")
        print("8. Back")

        choice = input("Enter Choice: ")


        if choice == "1":
            print(analytics.total_employees())
        elif choice == "2":
            print(analytics.highest_salary_employee())
        elif choice == "3":
            print(analytics.lowest_salary_employee())
        elif choice == "4":
            department = input("Enter Department: ")
            print(analytics.employee_by_department(department))
        elif choice == "5":
            salary = input("Enter Salary of Employee: ")
            print(analytics.employee_above_salary(salary))
        elif choice == "6":
            print(analytics.group_by_deparment())
        elif choice == "7":
            print(analytics.average_salary_employee())
        elif choice == "8":
            break
