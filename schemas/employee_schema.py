from pydantic import BaseModel

class EmployeeRequest(BaseModel):
    emp_id: str
    name: str
    department: str
    salary: int