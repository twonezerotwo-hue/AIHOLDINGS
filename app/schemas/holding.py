"""Pydantic schemas for Holding model"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


class HoldingBase(BaseModel):
    """Base holding schema"""
    name: str
    description: Optional[str] = None
    industry: Optional[str] = None
    headquarters: Optional[str] = None
    founded_year: Optional[int] = None


class HoldingCreate(HoldingBase):
    """Schema for creating a holding"""
    pass


class HoldingUpdate(BaseModel):
    """Schema for updating a holding"""
    name: Optional[str] = None
    description: Optional[str] = None
    industry: Optional[str] = None
    headquarters: Optional[str] = None
    founded_year: Optional[int] = None


class HoldingInDB(HoldingBase):
    """Schema for holding in database"""
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class Holding(HoldingInDB):
    """Schema for holding response"""
    pass
