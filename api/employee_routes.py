from http import server

from fastapi import APIRouter
from services.employe_service import EmployeeService
from services.analytics_service import DataAnalytics
from exceptions.employee_exception import EmployeeNotFoundError, DuplicateEmployeeError
from fastapi import HTTPException
from schemas.employee_schema import EmployeeRequest,UpdateEmployeeRequest

router = APIRouter()
service = EmployeeService()
analytics = DataAnalytics()


@router.get("/employees")
def get_employees():
   return service.get_all_employees()
@router.get("/employees/count")
def get_total_employees():
    return  analytics.total_employees()
@router.get("/employees/highest-salary")
def highest_salary():
    return  analytics.highest_salary_employee()
@router.get("/employees/average-salary")
def average_salary():
    return analytics.average_salary_employee()
@router.get("/employees/lowest-salary")
def average_salary():
    return analytics.lowest_salary_employee()
@router.get("/employees/group-by-department")
def group_by_department():
    return analytics.group_by_department()
@router.get("/employees/above-salary/{salary}")
def group_by_department(salary: str):
    return analytics.employee_above_salary(salary)
@router.get("/employees/employee-by-department/{department}")
def get_employee_by_department(department: str):
    return  analytics.employee_by_department(department)
@router.get("/employees/{emp_id}")
def get_employee(emp_id: str):
    try:
        return service.search_employee(emp_id)
    except EmployeeNotFoundError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )

@router.get("/employees/sort-by-salary")
def sort_by_salary():
    return service.sort_by_salary()



@router.post("/employees", status_code=200)
def add_employee(employee: EmployeeRequest):
    try:
        service.add_employee(employee.model_dump())
        return {"message": "Employee added successfully"}

    except DuplicateEmployeeError as error:
        raise HTTPException(
            status_code=409,
            detail=str(error)
        )


@router.put("/employees/{emp_id}", status_code=200)
def update_employee(emp_id: str,employee: UpdateEmployeeRequest):
    try:
        employee_data = employee.model_dump()
        employee_data["emp_id"] = emp_id
        service.update_employee(emp_id,employee_data)
        return {"message": "Employee Updated successfully"}

    except EmployeeNotFoundError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )

@router.delete("/employees/{emp_id}", status_code=200)
def delete_employee(emp_id: str):
    try:
        service.delete_employee(emp_id)
        return {"message": "Employee Deleted successfully"}
    except EmployeeNotFoundError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )



