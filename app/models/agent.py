"""Agent model for AI agents within departments"""

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.session import Base


class Agent(Base):
    """AI Agent model"""
    __tablename__ = "agents"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(Text)
    agent_type = Column(String, nullable=False)  # e.g., "customer_service", "data_analysis", "automation"
    status = Column(String, default="active")  # active, inactive, maintenance
    capabilities = Column(JSON)  # JSON field for flexible capability storage
    configuration = Column(JSON)  # JSON field for agent configuration
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    department = relationship("Department", back_populates="agents")
    tasks = relationship("Task", back_populates="assigned_to_agent")
