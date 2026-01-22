"""Unit tests for User model and CRUD operations"""

import pytest
from app.models.user import User
from app.crud import user as crud_user
from app.schemas.user import UserCreate, UserUpdate


def test_create_user(db):
    """Test creating a user"""
    user_data = UserCreate(
        email="test@example.com",
        username="testuser",
        password="testpassword",
        full_name="Test User"
    )
    user = crud_user.create_user(db, user_data)
    
    assert user.email == "test@example.com"
    assert user.username == "testuser"
    assert user.full_name == "Test User"
    assert user.is_active is True
    assert user.is_admin is False
    assert user.hashed_password != "testpassword"


def test_get_user_by_email(db):
    """Test getting a user by email"""
    user_data = UserCreate(
        email="test@example.com",
        username="testuser",
        password="testpassword"
    )
    created_user = crud_user.create_user(db, user_data)
    
    retrieved_user = crud_user.get_user_by_email(db, "test@example.com")
    assert retrieved_user is not None
    assert retrieved_user.id == created_user.id
    assert retrieved_user.email == "test@example.com"


def test_authenticate_user(db):
    """Test user authentication"""
    user_data = UserCreate(
        email="test@example.com",
        username="testuser",
        password="testpassword"
    )
    crud_user.create_user(db, user_data)
    
    # Correct credentials
    authenticated = crud_user.authenticate_user(db, "testuser", "testpassword")
    assert authenticated is not None
    assert authenticated.username == "testuser"
    
    # Wrong password
    not_authenticated = crud_user.authenticate_user(db, "testuser", "wrongpassword")
    assert not_authenticated is None


def test_update_user(db):
    """Test updating a user"""
    user_data = UserCreate(
        email="test@example.com",
        username="testuser",
        password="testpassword"
    )
    user = crud_user.create_user(db, user_data)
    
    update_data = UserUpdate(full_name="Updated Name")
    updated_user = crud_user.update_user(db, user.id, update_data)
    
    assert updated_user is not None
    assert updated_user.full_name == "Updated Name"
    assert updated_user.email == "test@example.com"


def test_delete_user(db):
    """Test deleting a user"""
    user_data = UserCreate(
        email="test@example.com",
        username="testuser",
        password="testpassword"
    )
    user = crud_user.create_user(db, user_data)
    user_id = user.id
    
    success = crud_user.delete_user(db, user_id)
    assert success is True
    
    deleted_user = crud_user.get_user(db, user_id)
    assert deleted_user is None
