"""Company model for business entities under holdings"""

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.session import Base


class Company(Base):
    """Company model"""
    __tablename__ = "companies"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(Text)
    industry = Column(String)
    location = Column(String)
    holding_id = Column(Integer, ForeignKey("holdings.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    holding = relationship("Holding", back_populates="companies")
    departments = relationship("Department", back_populates="company", cascade="all, delete-orphan")
