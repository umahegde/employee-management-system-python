import sqlite3


def create_table(connection):
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            emp_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            salary INTEGER NOT NULL
        )
    """)

    connection.commit()
    print("Table created")


def add_employee(connection):
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO employees (emp_id, name, department, salary)
        VALUES (?, ?, ?, ?)
    """, ("3", "Anu", "IT", 40000))

    connection.commit()
    print("Employee added")


def get_employees(connection):
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM employees")

    employees = cursor.fetchall()

    for employee in employees:
        print(employee)


def update_employee(connection):
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE employees
        SET salary = ?
        WHERE emp_id = ?
    """, (45000, "3"))

    connection.commit()
    print("Employee updated")


def delete_employee(connection):
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE emp_id = ?",
        ("3",)
    )

    connection.commit()
    print("Employee deleted")

connection = sqlite3.connect("employee.db")
get_employees(connection)

connection.close()