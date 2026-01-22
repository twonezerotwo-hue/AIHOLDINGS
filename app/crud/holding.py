"""CRUD operations for Holding model"""

from sqlalchemy.orm import Session
from app.models.holding import Holding
from app.schemas.holding import HoldingCreate, HoldingUpdate
from typing import Optional, List


def get_holding(db: Session, holding_id: int) -> Optional[Holding]:
    """Get a holding by ID"""
    return db.query(Holding).filter(Holding.id == holding_id).first()


def get_holding_by_name(db: Session, name: str) -> Optional[Holding]:
    """Get a holding by name"""
    return db.query(Holding).filter(Holding.name == name).first()


def get_holdings(db: Session, skip: int = 0, limit: int = 100) -> List[Holding]:
    """Get a list of holdings"""
    return db.query(Holding).offset(skip).limit(limit).all()


def create_holding(db: Session, holding: HoldingCreate) -> Holding:
    """Create a new holding"""
    db_holding = Holding(**holding.model_dump())
    db.add(db_holding)
    db.commit()
    db.refresh(db_holding)
    return db_holding


def update_holding(db: Session, holding_id: int, holding: HoldingUpdate) -> Optional[Holding]:
    """Update a holding"""
    db_holding = get_holding(db, holding_id)
    if not db_holding:
        return None
    
    update_data = holding.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_holding, field, value)
    
    db.commit()
    db.refresh(db_holding)
    return db_holding


def delete_holding(db: Session, holding_id: int) -> bool:
    """Delete a holding"""
    db_holding = get_holding(db, holding_id)
    if not db_holding:
        return False
    
    db.delete(db_holding)
    db.commit()
    return True
