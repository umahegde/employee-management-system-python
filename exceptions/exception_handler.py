from fastapi import Request
from fastapi.responses import JSONResponse

from exceptions.employee_exception import EmployeeNotFoundError,DuplicateEmployeeError


async def employee_not_found_handler(
    request: Request,
    exc: EmployeeNotFoundError
):
    return JSONResponse(
        status_code=404,
        content={"detail": str(exc)}
    )

async def duplicate_employee_handler(
    request: Request,
    exc: DuplicateEmployeeError
):
    return JSONResponse(
        status_code=409,
        content={"detail": str(exc)}
    )