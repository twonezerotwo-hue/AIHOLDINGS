"""CRUD operations for Company model"""

from sqlalchemy.orm import Session
from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate
from typing import Optional, List


def get_company(db: Session, company_id: int) -> Optional[Company]:
    """Get a company by ID"""
    return db.query(Company).filter(Company.id == company_id).first()


def get_companies(db: Session, skip: int = 0, limit: int = 100) -> List[Company]:
    """Get a list of companies"""
    return db.query(Company).offset(skip).limit(limit).all()


def get_companies_by_holding(db: Session, holding_id: int) -> List[Company]:
    """Get companies by holding ID"""
    return db.query(Company).filter(Company.holding_id == holding_id).all()


def create_company(db: Session, company: CompanyCreate) -> Company:
    """Create a new company"""
    db_company = Company(**company.model_dump())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


def update_company(db: Session, company_id: int, company: CompanyUpdate) -> Optional[Company]:
    """Update a company"""
    db_company = get_company(db, company_id)
    if not db_company:
        return None
    
    update_data = company.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_company, field, value)
    
    db.commit()
    db.refresh(db_company)
    return db_company


def delete_company(db: Session, company_id: int) -> bool:
    """Delete a company"""
    db_company = get_company(db, company_id)
    if not db_company:
        return False
    
    db.delete(db_company)
    db.commit()
    return True
