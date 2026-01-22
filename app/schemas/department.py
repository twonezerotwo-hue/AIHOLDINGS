"""Pydantic schemas for Department model"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class DepartmentBase(BaseModel):
    """Base department schema"""
    name: str
    description: Optional[str] = None
    location: Optional[str] = None
    company_id: int


class DepartmentCreate(DepartmentBase):
    """Schema for creating a department"""
    pass


class DepartmentUpdate(BaseModel):
    """Schema for updating a department"""
    name: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    company_id: Optional[int] = None


class DepartmentInDB(DepartmentBase):
    """Schema for department in database"""
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class Department(DepartmentInDB):
    """Schema for department response"""
    pass
