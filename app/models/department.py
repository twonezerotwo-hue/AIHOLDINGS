"""Department model for organizational units within companies"""

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.session import Base


class Department(Base):
    """Department model"""
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(Text)
    location = Column(String)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    company = relationship("Company", back_populates="departments")
    agents = relationship("Agent", back_populates="department", cascade="all, delete-orphan")
