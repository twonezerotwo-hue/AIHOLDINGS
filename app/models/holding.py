"""Holding model for top-level business entities"""

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.session import Base


class Holding(Base):
    """Holding company model"""
    __tablename__ = "holdings"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(Text)
    industry = Column(String)
    headquarters = Column(String)
    founded_year = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    companies = relationship("Company", back_populates="holding", cascade="all, delete-orphan")
