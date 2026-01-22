"""Agent API endpoints"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.schemas.agent import Agent, AgentCreate, AgentUpdate
from app.crud import agent as crud_agent
from app.crud import department as crud_department
from app.core.auth import get_current_user
from app.models.user import User

router = APIRouter()


@router.post("/", response_model=Agent, status_code=status.HTTP_201_CREATED)
def create_agent(
    agent: AgentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new agent"""
    # Verify department exists
    department = crud_department.get_department(db, department_id=agent.department_id)
    if not department:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Department not found"
        )
    return crud_agent.create_agent(db=db, agent=agent)


@router.get("/", response_model=List[Agent])
def read_agents(
    skip: int = 0,
    limit: int = 100,
    department_id: int = None,
    agent_type: str = None,
    status: str = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all agents or filter by department/type/status"""
    if department_id:
        agents = crud_agent.get_agents_by_department(db, department_id=department_id)
    elif agent_type:
        agents = crud_agent.get_agents_by_type(db, agent_type=agent_type)
    elif status:
        agents = crud_agent.get_agents_by_status(db, status=status)
    else:
        agents = crud_agent.get_agents(db, skip=skip, limit=limit)
    return agents


@router.get("/{agent_id}", response_model=Agent)
def read_agent(
    agent_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get a specific agent"""
    db_agent = crud_agent.get_agent(db, agent_id=agent_id)
    if db_agent is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agent not found"
        )
    return db_agent


@router.put("/{agent_id}", response_model=Agent)
def update_agent(
    agent_id: int,
    agent: AgentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update an agent"""
    db_agent = crud_agent.update_agent(db, agent_id=agent_id, agent=agent)
    if db_agent is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agent not found"
        )
    return db_agent


@router.delete("/{agent_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_agent(
    agent_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete an agent"""
    success = crud_agent.delete_agent(db, agent_id=agent_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agent not found"
        )
    return None
