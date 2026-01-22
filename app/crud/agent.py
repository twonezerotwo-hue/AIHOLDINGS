"""CRUD operations for Agent model"""

from sqlalchemy.orm import Session
from app.models.agent import Agent
from app.schemas.agent import AgentCreate, AgentUpdate
from typing import Optional, List


def get_agent(db: Session, agent_id: int) -> Optional[Agent]:
    """Get an agent by ID"""
    return db.query(Agent).filter(Agent.id == agent_id).first()


def get_agents(db: Session, skip: int = 0, limit: int = 100) -> List[Agent]:
    """Get a list of agents"""
    return db.query(Agent).offset(skip).limit(limit).all()


def get_agents_by_department(db: Session, department_id: int) -> List[Agent]:
    """Get agents by department ID"""
    return db.query(Agent).filter(Agent.department_id == department_id).all()


def get_agents_by_type(db: Session, agent_type: str) -> List[Agent]:
    """Get agents by type"""
    return db.query(Agent).filter(Agent.agent_type == agent_type).all()


def get_agents_by_status(db: Session, status: str) -> List[Agent]:
    """Get agents by status"""
    return db.query(Agent).filter(Agent.status == status).all()


def create_agent(db: Session, agent: AgentCreate) -> Agent:
    """Create a new agent"""
    db_agent = Agent(**agent.model_dump())
    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)
    return db_agent


def update_agent(db: Session, agent_id: int, agent: AgentUpdate) -> Optional[Agent]:
    """Update an agent"""
    db_agent = get_agent(db, agent_id)
    if not db_agent:
        return None
    
    update_data = agent.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_agent, field, value)
    
    db.commit()
    db.refresh(db_agent)
    return db_agent


def delete_agent(db: Session, agent_id: int) -> bool:
    """Delete an agent"""
    db_agent = get_agent(db, agent_id)
    if not db_agent:
        return False
    
    db.delete(db_agent)
    db.commit()
    return True
