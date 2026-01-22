"""Integration tests for authentication endpoints"""

import pytest
from fastapi import status


def test_register_user(client):
    """Test user registration"""
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "username": "testuser",
            "password": "testpassword",
            "full_name": "Test User"
        }
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["username"] == "testuser"
    assert "hashed_password" not in data


def test_register_duplicate_email(client):
    """Test registering with duplicate email"""
    user_data = {
        "email": "test@example.com",
        "username": "testuser",
        "password": "testpassword"
    }
    
    # First registration
    response1 = client.post("/api/v1/auth/register", json=user_data)
    assert response1.status_code == status.HTTP_201_CREATED
    
    # Second registration with same email
    user_data["username"] = "testuser2"
    response2 = client.post("/api/v1/auth/register", json=user_data)
    assert response2.status_code == status.HTTP_400_BAD_REQUEST


def test_login(client):
    """Test user login"""
    # Register user first
    client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "username": "testuser",
            "password": "testpassword"
        }
    )
    
    # Login
    response = client.post(
        "/api/v1/auth/login",
        data={
            "username": "testuser",
            "password": "testpassword"
        }
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password(client):
    """Test login with wrong password"""
    # Register user first
    client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "username": "testuser",
            "password": "testpassword"
        }
    )
    
    # Login with wrong password
    response = client.post(
        "/api/v1/auth/login",
        data={
            "username": "testuser",
            "password": "wrongpassword"
        }
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_access_protected_endpoint(client):
    """Test accessing protected endpoint with token"""
    # Register and login
    client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "username": "testuser",
            "password": "testpassword"
        }
    )
    
    login_response = client.post(
        "/api/v1/auth/login",
        data={
            "username": "testuser",
            "password": "testpassword"
        }
    )
    token = login_response.json()["access_token"]
    
    # Access protected endpoint
    response = client.get(
        "/api/v1/users/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["username"] == "testuser"


def test_access_protected_endpoint_without_token(client):
    """Test accessing protected endpoint without token"""
    response = client.get("/api/v1/users/me")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
