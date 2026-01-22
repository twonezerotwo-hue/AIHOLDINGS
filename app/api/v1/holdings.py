"""Holding API endpoints"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.schemas.holding import Holding, HoldingCreate, HoldingUpdate
from app.crud import holding as crud_holding
from app.core.auth import get_current_user
from app.models.user import User

router = APIRouter()


@router.post("/", response_model=Holding, status_code=status.HTTP_201_CREATED)
def create_holding(
    holding: HoldingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new holding"""
    # Check if holding with same name exists
    db_holding = crud_holding.get_holding_by_name(db, name=holding.name)
    if db_holding:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Holding with this name already exists"
        )
    return crud_holding.create_holding(db=db, holding=holding)


@router.get("/", response_model=List[Holding])
def read_holdings(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all holdings"""
    holdings = crud_holding.get_holdings(db, skip=skip, limit=limit)
    return holdings


@router.get("/{holding_id}", response_model=Holding)
def read_holding(
    holding_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get a specific holding"""
    db_holding = crud_holding.get_holding(db, holding_id=holding_id)
    if db_holding is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Holding not found"
        )
    return db_holding


@router.put("/{holding_id}", response_model=Holding)
def update_holding(
    holding_id: int,
    holding: HoldingUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update a holding"""
    db_holding = crud_holding.update_holding(db, holding_id=holding_id, holding=holding)
    if db_holding is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Holding not found"
        )
    return db_holding


@router.delete("/{holding_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_holding(
    holding_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete a holding"""
    success = crud_holding.delete_holding(db, holding_id=holding_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Holding not found"
        )
    return None
