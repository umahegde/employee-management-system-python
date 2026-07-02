class Validation:
    def validate_emp_id(self,emp_id):
        if not emp_id.strip():
          return False, "Employee ID cannot be empty"

        if not emp_id.isdigit():
            return False, "Employee ID should contain only numbers"

        return True, ""

    def validate_name(self,name):
        if not name.strip():
            return False, "Employee name cannot be empty"
        if len(name) < 3:
            return False, "Name should contain at least 3 characters"

        if not name.replace(" ", "").isalpha():
            return False, "Name should contain only alphabets"
        return True,""

    def validate_department(self,department):

        departments = [
        "IT",
        "HR",
        "Finance",
        "Admin",
        "Marketing"
        ]

        if department not in departments:
         return False, "Invalid Department"

        return True, ""
    def validate_salary(self,salary):

        try:

            salary = float(salary)

            if salary <= 0:
                return False, "Salary should be greater than zero"

            return True,""

        except ValueError:

            return False, "Salary should be numeric"

    def get_valid_input(self,prompt, validation_function):

            while True:

                value = input(prompt)

                valid, message = validation_function(value)

                if valid:
                    return value

                print(f"\n❌ {message}\n")
