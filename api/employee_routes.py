from fastapi import APIRouter,Depends
from services.employe_service import EmployeeService
from services.analytics_service import DataAnalytics
from schemas.employee_schema import EmployeeRequest,UpdateEmployeeRequest,EmployeeResponse,MessageResponse
from typing import List
from data.database import get_db
from sqlalchemy.orm import Session
from fastapi import Query

router = APIRouter()
page: int = Query(1, ge=1)
page_size: int = Query(5, ge=1, le=100)

def get_employee_service():
    return EmployeeService()

def get_analytics_service():
    return DataAnalytics()


@router.get("/employees",response_model=List[EmployeeResponse])
def get_employees( db: Session = Depends(get_db),
    service: EmployeeService = Depends(get_employee_service),page: int = Query(1, ge=1),
page_size: int = Query(5, ge=1, le=100)):
    return service.get_all_employees(db,page,page_size)

@router.get("/employees/count")
def get_total_employees( db: Session = Depends(get_db),analytics :DataAnalytics = Depends(get_analytics_service)):
    return  analytics.total_employees(db)

@router.get("/employees/highest-salary")
def highest_salary(db: Session = Depends(get_db),analytics :DataAnalytics = Depends(get_analytics_service)):
    return  analytics.highest_salary_employee(db)

@router.get("/employees/average-salary")
def average_salary(db: Session = Depends(get_db),analytics :DataAnalytics = Depends(get_analytics_service)):
    return analytics.average_salary_employee(db)

@router.get("/employees/lowest-salary")
def lowest_salary(db: Session = Depends(get_db),analytics :DataAnalytics = Depends(get_analytics_service)):
    return analytics.lowest_salary_employee(db)

@router.get("/employees/group-by-department")
def group_by_department(db: Session = Depends(get_db),analytics :DataAnalytics = Depends(get_analytics_service)):
    return analytics.group_by_department(db)

@router.get("/employees/above-salary/{salary}")
def employee_above_salary(salary: str,db: Session = Depends(get_db),analytics :DataAnalytics = Depends(get_analytics_service)):
    return analytics.employee_above_salary(db,salary)

@router.get("/employees/employee-by-department/{department}")
def get_employee_by_department(department: str,db: Session = Depends(get_db),analytics :DataAnalytics = Depends(get_analytics_service)):
    return  analytics.employee_by_department(db,department)

@router.get("/employees/sort-by-salary")
def sort_by_salary(db: Session = Depends(get_db), analytics :DataAnalytics = Depends(get_analytics_service)):
    return analytics.sort_by_salary(db)

@router.get("/employees/{emp_id}",response_model=EmployeeResponse)
def get_employee(emp_id: str,  db: Session = Depends(get_db),  service: EmployeeService = Depends(get_employee_service)):
    return service.search_employee(db,emp_id)


@router.post("/employees", status_code=201,response_model=MessageResponse)
def add_employee(employee: EmployeeRequest, db: Session = Depends(get_db), service: EmployeeService = Depends(get_employee_service)):

    service.add_employee(db,employee.model_dump())
    return {"message": "Employee added successfully"}



@router.put("/employees/{emp_id}", status_code=200,response_model=MessageResponse)
def update_employee(emp_id: str,employee: UpdateEmployeeRequest, db: Session = Depends(get_db),  service: EmployeeService = Depends(get_employee_service)):
    service.update_employee(db,emp_id,employee)
    return {"message": "Employee Updated successfully"}



@router.delete("/employees/{emp_id}", status_code=200,response_model=MessageResponse)
def delete_employee(emp_id: str, db: Session = Depends(get_db), service: EmployeeService = Depends(get_employee_service)):

    service.delete_employee(db,emp_id)
    return {"message": "Employee Deleted successfully"}



