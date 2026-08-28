from fastapi import APIRouter,Depends
from services.employe_service import EmployeeService
from services.analytics_service import DataAnalytics
from schemas.employee_schema import EmployeeRequest,UpdateEmployeeRequest,EmployeeResponse,MessageResponse
from typing import List


router = APIRouter()

def get_employee_service():
    return EmployeeService()

def get_analytics_service():
    return DataAnalytics()


@router.get("/employees",response_model=List[EmployeeResponse])
def get_employees(
    service: EmployeeService = Depends(get_employee_service)
):
    return service.get_all_employees()
@router.get("/employees/count")
def get_total_employees(analytics :DataAnalytics = Depends(get_analytics_service)):
    return  analytics.total_employees()
@router.get("/employees/highest-salary")
def highest_salary(analytics :DataAnalytics = Depends(get_analytics_service)):
    return  analytics.highest_salary_employee()
@router.get("/employees/average-salary")
def average_salary(analytics :DataAnalytics = Depends(get_analytics_service)):
    return analytics.average_salary_employee()
@router.get("/employees/lowest-salary")
def lowest_salary(analytics :DataAnalytics = Depends(get_analytics_service)):
    return analytics.lowest_salary_employee()
@router.get("/employees/group-by-department")
def group_by_department(analytics :DataAnalytics = Depends(get_analytics_service)):
    return analytics.group_by_department()
@router.get("/employees/above-salary/{salary}")
def employee_above_salary(salary: str,analytics :DataAnalytics = Depends(get_analytics_service)):
    return analytics.employee_above_salary(salary)
@router.get("/employees/employee-by-department/{department}")
def get_employee_by_department(department: str,analytics :DataAnalytics = Depends(get_analytics_service)):
    return  analytics.employee_by_department(department)
@router.get("/employees/{emp_id}",response_model=EmployeeResponse)
def get_employee(emp_id: str,  service: EmployeeService = Depends(get_employee_service)):
    return service.search_employee(emp_id)


@router.get("/employees/sort-by-salary")
def sort_by_salary( service: EmployeeService = Depends(get_employee_service)):
    return service.sort_by_salary()



@router.post("/employees", status_code=201,response_model=MessageResponse)
def add_employee(employee: EmployeeRequest,  service: EmployeeService = Depends(get_employee_service)):

    service.add_employee(employee.model_dump())
    return {"message": "Employee added successfully"}



@router.put("/employees/{emp_id}", status_code=200,response_model=MessageResponse)
def update_employee(emp_id: str,employee: UpdateEmployeeRequest,  service: EmployeeService = Depends(get_employee_service)):

    employee_data = employee.model_dump()
    employee_data["emp_id"] = emp_id
    service.update_employee(emp_id,employee_data)
    return {"message": "Employee Updated successfully"}



@router.delete("/employees/{emp_id}", status_code=200,response_model=MessageResponse)
def delete_employee(emp_id: str,  service: EmployeeService = Depends(get_employee_service)):

    service.delete_employee(emp_id)
    return {"message": "Employee Deleted successfully"}



