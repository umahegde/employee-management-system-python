# This is a sample Python script.
# Press ⌃F5 to execute it or replace it with your code.
from handler.employee_handler import employee_menu
from handler.analytic_handler import analytics_menu

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
















