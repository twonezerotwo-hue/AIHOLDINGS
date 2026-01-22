"""Pydantic schemas for Agent model"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any


class AgentBase(BaseModel):
    """Base agent schema"""
    name: str
    description: Optional[str] = None
    agent_type: str
    status: Optional[str] = "active"
    capabilities: Optional[Dict[str, Any]] = None
    configuration: Optional[Dict[str, Any]] = None
    department_id: int


class AgentCreate(AgentBase):
    """Schema for creating an agent"""
    pass


class AgentUpdate(BaseModel):
    """Schema for updating an agent"""
    name: Optional[str] = None
    description: Optional[str] = None
    agent_type: Optional[str] = None
    status: Optional[str] = None
    capabilities: Optional[Dict[str, Any]] = None
    configuration: Optional[Dict[str, Any]] = None
    department_id: Optional[int] = None


class AgentInDB(AgentBase):
    """Schema for agent in database"""
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class Agent(AgentInDB):
    """Schema for agent response"""
    pass
