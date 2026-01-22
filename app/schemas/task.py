"""Pydantic schemas for Task model"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.task import TaskStatus, TaskPriority


class TaskBase(BaseModel):
    """Base task schema"""
    title: str
    description: Optional[str] = None
    status: Optional[TaskStatus] = TaskStatus.PENDING
    priority: Optional[TaskPriority] = TaskPriority.MEDIUM
    assigned_to_agent_id: Optional[int] = None
    assigned_to_user_id: Optional[int] = None
    due_date: Optional[datetime] = None


class TaskCreate(TaskBase):
    """Schema for creating a task"""
    pass


class TaskUpdate(BaseModel):
    """Schema for updating a task"""
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    assigned_to_agent_id: Optional[int] = None
    assigned_to_user_id: Optional[int] = None
    due_date: Optional[datetime] = None


class TaskInDB(TaskBase):
    """Schema for task in database"""
    id: int
    completed_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class Task(TaskInDB):
    """Schema for task response"""
    pass
