"""Company API endpoints"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.schemas.company import Company, CompanyCreate, CompanyUpdate
from app.crud import company as crud_company
from app.crud import holding as crud_holding
from app.core.auth import get_current_user
from app.models.user import User

router = APIRouter()


@router.post("/", response_model=Company, status_code=status.HTTP_201_CREATED)
def create_company(
    company: CompanyCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new company"""
    # Verify holding exists
    holding = crud_holding.get_holding(db, holding_id=company.holding_id)
    if not holding:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Holding not found"
        )
    return crud_company.create_company(db=db, company=company)


@router.get("/", response_model=List[Company])
def read_companies(
    skip: int = 0,
    limit: int = 100,
    holding_id: int = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all companies or filter by holding"""
    if holding_id:
        companies = crud_company.get_companies_by_holding(db, holding_id=holding_id)
    else:
        companies = crud_company.get_companies(db, skip=skip, limit=limit)
    return companies


@router.get("/{company_id}", response_model=Company)
def read_company(
    company_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get a specific company"""
    db_company = crud_company.get_company(db, company_id=company_id)
    if db_company is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found"
        )
    return db_company


@router.put("/{company_id}", response_model=Company)
def update_company(
    company_id: int,
    company: CompanyUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update a company"""
    db_company = crud_company.update_company(db, company_id=company_id, company=company)
    if db_company is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found"
        )
    return db_company


@router.delete("/{company_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_company(
    company_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete a company"""
    success = crud_company.delete_company(db, company_id=company_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found"
        )
    return None
