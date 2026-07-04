from employee_management_system.utils.constants import DEPARTMENTS

class Validation:
    def validate_emp_id(self, emp_id:str)->tuple[bool, str]:
        if not emp_id.strip():
          return False, "Employee ID cannot be empty"

        if not emp_id.isdigit():
            return False, "Employee ID should contain only numbers"

        return True, ""

    def validate_name(self, name :str)->tuple[bool, str]:
        if not name.strip():
            return False, "Employee name cannot be empty"
        if len(name) < 3:
            return False, "Name should contain at least 3 characters"

        if not name.replace(" ", "").isalpha():
            return False, "Name should contain only alphabets"
        return True, ""

    def validate_department(self, department:str)->tuple[bool, str]:
        department = department.strip()
        if department not in DEPARTMENTS:
         return False, "Invalid Department"

        return True, ""
    def validate_salary(self, salary:str)->tuple[bool, str]:

        try:

            salary_value = float(salary)

            if salary_value <= 0:
                return False, "Salary should be greater than zero"

            return True,""

        except ValueError:

            return False, "Salary should be numeric"

    def get_valid_input(self, prompt:str, validation_function)->str:

            while True:

                value = input(prompt)

                valid, message = validation_function(value)

                if valid:
                    return value

                print(f"\n❌ {message}\n")
