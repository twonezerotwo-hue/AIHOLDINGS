"""Department API endpoints"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.schemas.department import Department, DepartmentCreate, DepartmentUpdate
from app.crud import department as crud_department
from app.crud import company as crud_company
from app.core.auth import get_current_user
from app.models.user import User

router = APIRouter()


@router.post("/", response_model=Department, status_code=status.HTTP_201_CREATED)
def create_department(
    department: DepartmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new department"""
    # Verify company exists
    company = crud_company.get_company(db, company_id=department.company_id)
    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found"
        )
    return crud_department.create_department(db=db, department=department)


@router.get("/", response_model=List[Department])
def read_departments(
    skip: int = 0,
    limit: int = 100,
    company_id: int = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all departments or filter by company"""
    if company_id:
        departments = crud_department.get_departments_by_company(db, company_id=company_id)
    else:
        departments = crud_department.get_departments(db, skip=skip, limit=limit)
    return departments


@router.get("/{department_id}", response_model=Department)
def read_department(
    department_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get a specific department"""
    db_department = crud_department.get_department(db, department_id=department_id)
    if db_department is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Department not found"
        )
    return db_department


@router.put("/{department_id}", response_model=Department)
def update_department(
    department_id: int,
    department: DepartmentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update a department"""
    db_department = crud_department.update_department(db, department_id=department_id, department=department)
    if db_department is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Department not found"
        )
    return db_department


@router.delete("/{department_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_department(
    department_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete a department"""
    success = crud_department.delete_department(db, department_id=department_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Department not found"
        )
    return None
