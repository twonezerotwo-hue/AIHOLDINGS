"""Unit tests for Holding model and CRUD operations"""

import pytest
from app.crud import holding as crud_holding
from app.schemas.holding import HoldingCreate, HoldingUpdate


def test_create_holding(db):
    """Test creating a holding"""
    holding_data = HoldingCreate(
        name="Test Holding",
        description="Test Description",
        industry="Technology",
        headquarters="San Francisco",
        founded_year=2020
    )
    holding = crud_holding.create_holding(db, holding_data)
    
    assert holding.name == "Test Holding"
    assert holding.description == "Test Description"
    assert holding.industry == "Technology"
    assert holding.headquarters == "San Francisco"
    assert holding.founded_year == 2020


def test_get_holding(db):
    """Test getting a holding by ID"""
    holding_data = HoldingCreate(name="Test Holding")
    created_holding = crud_holding.create_holding(db, holding_data)
    
    retrieved_holding = crud_holding.get_holding(db, created_holding.id)
    assert retrieved_holding is not None
    assert retrieved_holding.id == created_holding.id
    assert retrieved_holding.name == "Test Holding"


def test_get_holding_by_name(db):
    """Test getting a holding by name"""
    holding_data = HoldingCreate(name="Test Holding")
    created_holding = crud_holding.create_holding(db, holding_data)
    
    retrieved_holding = crud_holding.get_holding_by_name(db, "Test Holding")
    assert retrieved_holding is not None
    assert retrieved_holding.id == created_holding.id


def test_update_holding(db):
    """Test updating a holding"""
    holding_data = HoldingCreate(name="Test Holding")
    holding = crud_holding.create_holding(db, holding_data)
    
    update_data = HoldingUpdate(description="Updated Description")
    updated_holding = crud_holding.update_holding(db, holding.id, update_data)
    
    assert updated_holding is not None
    assert updated_holding.description == "Updated Description"
    assert updated_holding.name == "Test Holding"


def test_delete_holding(db):
    """Test deleting a holding"""
    holding_data = HoldingCreate(name="Test Holding")
    holding = crud_holding.create_holding(db, holding_data)
    holding_id = holding.id
    
    success = crud_holding.delete_holding(db, holding_id)
    assert success is True
    
    deleted_holding = crud_holding.get_holding(db, holding_id)
    assert deleted_holding is None
