"""Task API endpoints"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.schemas.task import Task, TaskCreate, TaskUpdate
from app.crud import task as crud_task
from app.models.task import TaskStatus
from app.core.auth import get_current_user
from app.models.user import User

router = APIRouter()


@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new task"""
    return crud_task.create_task(db=db, task=task)


@router.get("/", response_model=List[Task])
def read_tasks(
    skip: int = 0,
    limit: int = 100,
    agent_id: int = None,
    user_id: int = None,
    status: TaskStatus = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all tasks or filter by agent/user/status"""
    if agent_id:
        tasks = crud_task.get_tasks_by_agent(db, agent_id=agent_id)
    elif user_id:
        tasks = crud_task.get_tasks_by_user(db, user_id=user_id)
    elif status:
        tasks = crud_task.get_tasks_by_status(db, status=status)
    else:
        tasks = crud_task.get_tasks(db, skip=skip, limit=limit)
    return tasks


@router.get("/{task_id}", response_model=Task)
def read_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get a specific task"""
    db_task = crud_task.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return db_task


@router.put("/{task_id}", response_model=Task)
def update_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update a task"""
    db_task = crud_task.update_task(db, task_id=task_id, task=task)
    if db_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return db_task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete a task"""
    success = crud_task.delete_task(db, task_id=task_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return None
