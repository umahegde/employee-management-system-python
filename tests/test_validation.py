from utils.validation import Validation
validation = Validation()


def test_validate_name_success():
    assert validation.validate_name("Uma") == (True, "")


def test_validate_name_empty():
    assert validation.validate_name("") == (False, "Employee name cannot be empty")


def test_validate_name_less_than_three_characters():
    assert validation.validate_name("Um") == (False, "Name should contain at least 3 characters")


def test_validate_name_with_name_numbers():
    assert validation.validate_name("Um34") == (
        False,
        "Name should contain only alphabets"
    )


def test_validate_emp_id_success():
    assert validation.validate_emp_id("10") == (True, "")


def test_validate_emp_id_empty():
    assert validation.validate_emp_id("") == (False, "Employee ID cannot be empty")


def test_validate_emp_id_with_string():
    assert validation.validate_emp_id("Uma") == (False, "Employee ID should contain only numbers")


def test_validate_emp_id_with_number_name():
    assert validation.validate_emp_id("12ih") == (False, "Employee ID should contain only numbers")


def test_validate_salary_success():
    assert validation.validate_salary("50000") == (True, "")


def test_validate_salary_negative():
    assert validation.validate_salary("-98") == (False, "Salary should be greater than zero")


def test_validate_salary_with_string():
    assert validation.validate_salary("abc") == (False, "Salary should be numeric")


def test_validate_department_success():
    assert validation.validate_department("IT") == (True, "")


def test_validate_department_empty():
    assert validation.validate_department("Software") == (False, "Invalid Department")
