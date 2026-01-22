"""Pydantic schemas for Company model"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CompanyBase(BaseModel):
    """Base company schema"""
    name: str
    description: Optional[str] = None
    industry: Optional[str] = None
    location: Optional[str] = None
    holding_id: int


class CompanyCreate(CompanyBase):
    """Schema for creating a company"""
    pass


class CompanyUpdate(BaseModel):
    """Schema for updating a company"""
    name: Optional[str] = None
    description: Optional[str] = None
    industry: Optional[str] = None
    location: Optional[str] = None
    holding_id: Optional[int] = None


class CompanyInDB(CompanyBase):
    """Schema for company in database"""
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class Company(CompanyInDB):
    """Schema for company response"""
    pass
