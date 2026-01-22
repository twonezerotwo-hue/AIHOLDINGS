#!/usr/bin/env python3
"""
Quick start script for AI Holdings Enterprise Management System
This script demonstrates basic usage without requiring a running database
"""

def print_section(title):
    """Print a section header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")


def main():
    print_section("AI Holdings Enterprise Management System")
    
    # Import the application
    from app.main import app
    from config.settings import settings
    
    print("✅ Application loaded successfully!")
    print(f"   Name: {settings.APP_NAME}")
    print(f"   Version: {settings.APP_VERSION}")
    
    print_section("Available API Endpoints")
    
    endpoints = {
        "Documentation": [
            "GET /docs - Swagger UI documentation",
            "GET /redoc - ReDoc documentation",
            "GET /health - Health check endpoint",
        ],
        "Authentication": [
            "POST /api/v1/auth/register - Register new user",
            "POST /api/v1/auth/login - Login and get JWT token",
        ],
        "Users": [
            "GET /api/v1/users/me - Get current user",
            "GET /api/v1/users/ - List all users (admin)",
            "GET /api/v1/users/{id} - Get user by ID",
            "PUT /api/v1/users/{id} - Update user",
            "DELETE /api/v1/users/{id} - Delete user (admin)",
        ],
        "Holdings": [
            "POST /api/v1/holdings/ - Create holding",
            "GET /api/v1/holdings/ - List all holdings",
            "GET /api/v1/holdings/{id} - Get holding by ID",
            "PUT /api/v1/holdings/{id} - Update holding",
            "DELETE /api/v1/holdings/{id} - Delete holding",
        ],
        "Companies": [
            "POST /api/v1/companies/ - Create company",
            "GET /api/v1/companies/ - List all companies",
            "GET /api/v1/companies/{id} - Get company by ID",
            "PUT /api/v1/companies/{id} - Update company",
            "DELETE /api/v1/companies/{id} - Delete company",
        ],
        "Departments": [
            "POST /api/v1/departments/ - Create department",
            "GET /api/v1/departments/ - List all departments",
            "GET /api/v1/departments/{id} - Get department by ID",
            "PUT /api/v1/departments/{id} - Update department",
            "DELETE /api/v1/departments/{id} - Delete department",
        ],
        "Agents": [
            "POST /api/v1/agents/ - Create agent",
            "GET /api/v1/agents/ - List all agents",
            "GET /api/v1/agents/{id} - Get agent by ID",
            "PUT /api/v1/agents/{id} - Update agent",
            "DELETE /api/v1/agents/{id} - Delete agent",
        ],
        "Tasks": [
            "POST /api/v1/tasks/ - Create task",
            "GET /api/v1/tasks/ - List all tasks",
            "GET /api/v1/tasks/{id} - Get task by ID",
            "PUT /api/v1/tasks/{id} - Update task",
            "DELETE /api/v1/tasks/{id} - Delete task",
        ],
    }
    
    for category, routes in endpoints.items():
        print(f"📁 {category}")
        for route in routes:
            print(f"   {route}")
        print()
    
    print_section("Quick Start Commands")
    
    print("🐳 Using Docker (Recommended):")
    print("   docker-compose up -d")
    print("   # Access at http://localhost:8000")
    print()
    
    print("🐍 Manual Setup:")
    print("   1. Create virtual environment:")
    print("      python -m venv venv")
    print("      source venv/bin/activate")
    print()
    print("   2. Install dependencies:")
    print("      pip install -r requirements.txt")
    print()
    print("   3. Set up database:")
    print("      createdb aiholdings")
    print()
    print("   4. Create .env file:")
    print("      cp .env.example .env")
    print()
    print("   5. Run the application:")
    print("      uvicorn app.main:app --reload")
    print()
    
    print_section("Testing")
    
    print("Run all tests:")
    print("   pytest")
    print()
    print("Run with coverage:")
    print("   pytest --cov=app")
    print()
    print("Run specific tests:")
    print("   pytest tests/unit/")
    print("   pytest tests/integration/")
    print()
    
    print_section("Example Usage")
    
    print("1. Register a user:")
    print('   curl -X POST "http://localhost:8000/api/v1/auth/register" \\')
    print('     -H "Content-Type: application/json" \\')
    print('     -d \'{"email":"user@example.com","username":"user","password":"pass123"}\'')
    print()
    
    print("2. Login:")
    print('   curl -X POST "http://localhost:8000/api/v1/auth/login" \\')
    print('     -H "Content-Type: application/x-www-form-urlencoded" \\')
    print('     -d "username=user&password=pass123"')
    print()
    
    print("3. Create a holding (with token):")
    print('   curl -X POST "http://localhost:8000/api/v1/holdings/" \\')
    print('     -H "Authorization: Bearer YOUR_TOKEN" \\')
    print('     -H "Content-Type: application/json" \\')
    print('     -d \'{"name":"Tech Holdings","industry":"Technology"}\'')
    print()
    
    print_section("Database Schema")
    
    print("📊 Entity Relationships:")
    print("   Holding (1) --> (N) Company")
    print("   Company (1) --> (N) Department")
    print("   Department (1) --> (N) Agent")
    print("   Agent (1) --> (N) Task")
    print("   User (1) --> (N) Task")
    print()
    
    print("✅ System ready! Access the API documentation at:")
    print("   http://localhost:8000/docs")
    print()


if __name__ == "__main__":
    main()
