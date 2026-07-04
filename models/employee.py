class Employee:
    def __init__(self, emp_id:str, name:str, department:str, salary:float)->None:
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def to_dict(self) -> dict:
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "department": self.department,
            "salary": self.salary
        }



