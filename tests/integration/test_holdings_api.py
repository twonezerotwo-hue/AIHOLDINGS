"""Integration tests for holdings API"""

import pytest
from fastapi import status


def get_auth_token(client):
    """Helper function to register and login a user"""
    client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "username": "testuser",
            "password": "testpassword"
        }
    )
    
    response = client.post(
        "/api/v1/auth/login",
        data={
            "username": "testuser",
            "password": "testpassword"
        }
    )
    return response.json()["access_token"]


def test_create_holding(client):
    """Test creating a holding"""
    token = get_auth_token(client)
    
    response = client.post(
        "/api/v1/holdings/",
        json={
            "name": "Test Holding",
            "description": "Test Description",
            "industry": "Technology"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["name"] == "Test Holding"
    assert data["description"] == "Test Description"


def test_get_holdings(client):
    """Test getting all holdings"""
    token = get_auth_token(client)
    
    # Create a holding first
    client.post(
        "/api/v1/holdings/",
        json={"name": "Test Holding"},
        headers={"Authorization": f"Bearer {token}"}
    )
    
    # Get all holdings
    response = client.get(
        "/api/v1/holdings/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) > 0


def test_get_holding_by_id(client):
    """Test getting a specific holding"""
    token = get_auth_token(client)
    
    # Create a holding
    create_response = client.post(
        "/api/v1/holdings/",
        json={"name": "Test Holding"},
        headers={"Authorization": f"Bearer {token}"}
    )
    holding_id = create_response.json()["id"]
    
    # Get the holding
    response = client.get(
        f"/api/v1/holdings/{holding_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == holding_id


def test_update_holding(client):
    """Test updating a holding"""
    token = get_auth_token(client)
    
    # Create a holding
    create_response = client.post(
        "/api/v1/holdings/",
        json={"name": "Test Holding"},
        headers={"Authorization": f"Bearer {token}"}
    )
    holding_id = create_response.json()["id"]
    
    # Update the holding
    response = client.put(
        f"/api/v1/holdings/{holding_id}",
        json={"description": "Updated Description"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["description"] == "Updated Description"


def test_delete_holding(client):
    """Test deleting a holding"""
    token = get_auth_token(client)
    
    # Create a holding
    create_response = client.post(
        "/api/v1/holdings/",
        json={"name": "Test Holding"},
        headers={"Authorization": f"Bearer {token}"}
    )
    holding_id = create_response.json()["id"]
    
    # Delete the holding
    response = client.delete(
        f"/api/v1/holdings/{holding_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    
    # Verify it's deleted
    get_response = client.get(
        f"/api/v1/holdings/{holding_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert get_response.status_code == status.HTTP_404_NOT_FOUND
