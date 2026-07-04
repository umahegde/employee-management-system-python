from services.analytics_service import DataAnalytics
from utils.display import display_employee_details
from employee_management_system.utils.logger import logger

analytics = DataAnalytics()


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
            employee = analytics.highest_salary_employee()
            display_employee_details(employee)
        elif choice == "3":
            employee = analytics.lowest_salary_employee()
            display_employee_details(employee)
        elif choice == "4":
            department = input("Enter Department: ")
            employees = analytics.employee_by_department(department)
            for employee in employees:
                display_employee_details(employee)
        elif choice == "5":
            salary = input("Enter Salary of Employee: ")
            print(analytics.employee_above_salary(salary))
        elif choice == "6":
            print(analytics.group_by_department())
            logger.info(f"User filtered employees by department")
        elif choice == "7":
            average = analytics.average_salary_employee()
            print(f"Average Salary: {average:.2f}")
            logger.info("User viewed average salary.")
        elif choice == "8":
            break
        else:
            print("❌ Invalid choice. Please try again.")