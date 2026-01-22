"""CRUD operations for Task model"""

from sqlalchemy.orm import Session
from app.models.task import Task, TaskStatus
from app.schemas.task import TaskCreate, TaskUpdate
from typing import Optional, List
from datetime import datetime


def get_task(db: Session, task_id: int) -> Optional[Task]:
    """Get a task by ID"""
    return db.query(Task).filter(Task.id == task_id).first()


def get_tasks(db: Session, skip: int = 0, limit: int = 100) -> List[Task]:
    """Get a list of tasks"""
    return db.query(Task).offset(skip).limit(limit).all()


def get_tasks_by_agent(db: Session, agent_id: int) -> List[Task]:
    """Get tasks by agent ID"""
    return db.query(Task).filter(Task.assigned_to_agent_id == agent_id).all()


def get_tasks_by_user(db: Session, user_id: int) -> List[Task]:
    """Get tasks by user ID"""
    return db.query(Task).filter(Task.assigned_to_user_id == user_id).all()


def get_tasks_by_status(db: Session, status: TaskStatus) -> List[Task]:
    """Get tasks by status"""
    return db.query(Task).filter(Task.status == status).all()


def create_task(db: Session, task: TaskCreate) -> Task:
    """Create a new task"""
    db_task = Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(db: Session, task_id: int, task: TaskUpdate) -> Optional[Task]:
    """Update a task"""
    db_task = get_task(db, task_id)
    if not db_task:
        return None
    
    update_data = task.model_dump(exclude_unset=True)
    
    # If status is being updated to completed, set completed_at
    if "status" in update_data and update_data["status"] == TaskStatus.COMPLETED:
        if db_task.status != TaskStatus.COMPLETED:
            update_data["completed_at"] = datetime.utcnow()
    
    for field, value in update_data.items():
        setattr(db_task, field, value)
    
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int) -> bool:
    """Delete a task"""
    db_task = get_task(db, task_id)
    if not db_task:
        return False
    
    db.delete(db_task)
    db.commit()
    return True
