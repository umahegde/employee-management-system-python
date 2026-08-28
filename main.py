# This is a sample Python script.
# Press ⌃F5 to execute it or replace it with your code.


from fastapi import FastAPI
from api.employee_routes import get_employees
from api.employee_routes import router
from exceptions.employee_exception import EmployeeNotFoundError, DuplicateEmployeeError
from exceptions.exception_handler import employee_not_found_handler,duplicate_employee_handler

app = FastAPI()
app.add_exception_handler(
    EmployeeNotFoundError,
    employee_not_found_handler
)
app.add_exception_handler(
    DuplicateEmployeeError,
    duplicate_employee_handler
)


@app.get("/")
def home():
    return {"message": "Welcome to Employee Management System"}

app.include_router(router)

'''
def main():
    """Main menu for Employee Management System."""

    while True:

        print("\nMain Menu")
        print("1. Employee")
        print("2. Analytics")
        print("3. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
         employee_menu()

        elif choice == "2":
            analytics_menu()

        elif choice == "3":
            print("Thank You!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

'''














