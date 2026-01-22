# AI Holdings - Enterprise Company Management System

A professional Enterprise Company Management System with AI Agents built using Python, FastAPI, SQLAlchemy, and PostgreSQL.

## Features

- **Complete Project Structure**: Modular design with clear separation of concerns
- **Database Models**: Holdings, Companies, Departments, Agents, Users, and Tasks
- **RESTful API**: FastAPI with automatic OpenAPI documentation
- **Authentication**: JWT-based authentication and authorization
- **Error Handling**: Comprehensive error handling with proper HTTP status codes
- **Testing**: Unit and integration tests using pytest
- **Docker Support**: Full containerization with Docker and docker-compose
- **Environment Configuration**: Flexible configuration using environment variables

## Project Structure

```
AIHOLDINGS/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── auth.py          # Authentication endpoints
│   │       ├── users.py         # User endpoints
│   │       ├── holdings.py      # Holding endpoints
│   │       ├── companies.py     # Company endpoints
│   │       ├── departments.py   # Department endpoints
│   │       ├── agents.py        # Agent endpoints
│   │       ├── tasks.py         # Task endpoints
│   │       └── router.py        # API router
│   ├── core/
│   │   ├── auth.py              # Authentication dependencies
│   │   └── security.py          # Security utilities
│   ├── crud/
│   │   ├── user.py              # User CRUD operations
│   │   ├── holding.py           # Holding CRUD operations
│   │   ├── company.py           # Company CRUD operations
│   │   ├── department.py        # Department CRUD operations
│   │   ├── agent.py             # Agent CRUD operations
│   │   └── task.py              # Task CRUD operations
│   ├── db/
│   │   └── session.py           # Database session management
│   ├── models/
│   │   ├── user.py              # User model
│   │   ├── holding.py           # Holding model
│   │   ├── company.py           # Company model
│   │   ├── department.py        # Department model
│   │   ├── agent.py             # Agent model
│   │   └── task.py              # Task model
│   ├── schemas/
│   │   ├── user.py              # User schemas
│   │   ├── holding.py           # Holding schemas
│   │   ├── company.py           # Company schemas
│   │   ├── department.py        # Department schemas
│   │   ├── agent.py             # Agent schemas
│   │   └── task.py              # Task schemas
│   └── main.py                  # FastAPI application
├── config/
│   └── settings.py              # Application settings
├── tests/
│   ├── integration/             # Integration tests
│   ├── unit/                    # Unit tests
│   └── conftest.py              # Test configuration
├── .env.example                 # Example environment variables
├── docker-compose.yml           # Docker compose configuration
├── Dockerfile                   # Docker image configuration
└── requirements.txt             # Python dependencies

## Quick Start

### Using Docker (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/twonezerotwo-hue/AIHOLDINGS.git
cd AIHOLDINGS
```

2. Create environment file:
```bash
cp .env.example .env
```

3. Start the services:
```bash
docker-compose up -d
```

4. Access the application:
- API: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Manual Setup

1. Clone the repository:
```bash
git clone https://github.com/twonezerotwo-hue/AIHOLDINGS.git
cd AIHOLDINGS
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up PostgreSQL database:
```bash
# Create database
createdb aiholdings
```

5. Create environment file:
```bash
cp .env.example .env
# Edit .env with your database credentials
```

6. Run the application:
```bash
uvicorn app.main:app --reload
```

## API Documentation

Once the application is running, you can access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register a new user
- `POST /api/v1/auth/login` - Login and get access token

### Users
- `GET /api/v1/users/me` - Get current user
- `GET /api/v1/users/` - Get all users (admin only)
- `GET /api/v1/users/{user_id}` - Get specific user
- `PUT /api/v1/users/{user_id}` - Update user
- `DELETE /api/v1/users/{user_id}` - Delete user (admin only)

### Holdings
- `POST /api/v1/holdings/` - Create holding
- `GET /api/v1/holdings/` - Get all holdings
- `GET /api/v1/holdings/{holding_id}` - Get specific holding
- `PUT /api/v1/holdings/{holding_id}` - Update holding
- `DELETE /api/v1/holdings/{holding_id}` - Delete holding

### Companies
- `POST /api/v1/companies/` - Create company
- `GET /api/v1/companies/` - Get all companies
- `GET /api/v1/companies/{company_id}` - Get specific company
- `PUT /api/v1/companies/{company_id}` - Update company
- `DELETE /api/v1/companies/{company_id}` - Delete company

### Departments
- `POST /api/v1/departments/` - Create department
- `GET /api/v1/departments/` - Get all departments
- `GET /api/v1/departments/{department_id}` - Get specific department
- `PUT /api/v1/departments/{department_id}` - Update department
- `DELETE /api/v1/departments/{department_id}` - Delete department

### Agents
- `POST /api/v1/agents/` - Create agent
- `GET /api/v1/agents/` - Get all agents
- `GET /api/v1/agents/{agent_id}` - Get specific agent
- `PUT /api/v1/agents/{agent_id}` - Update agent
- `DELETE /api/v1/agents/{agent_id}` - Delete agent

### Tasks
- `POST /api/v1/tasks/` - Create task
- `GET /api/v1/tasks/` - Get all tasks
- `GET /api/v1/tasks/{task_id}` - Get specific task
- `PUT /api/v1/tasks/{task_id}` - Update task
- `DELETE /api/v1/tasks/{task_id}` - Delete task

## Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest tests/unit/test_user.py

# Run integration tests only
pytest tests/integration/
```

## Database Models

### User
- Authentication and authorization
- Email, username, password
- Admin flag for permissions

### Holding
- Top-level business entity
- Name, description, industry
- Headquarters, founded year

### Company
- Business entities under holdings
- Name, description, industry, location
- Foreign key to holding

### Department
- Organizational units within companies
- Name, description, location
- Foreign key to company

### Agent
- AI agents within departments
- Name, type, status
- Capabilities and configuration (JSON)
- Foreign key to department

### Task
- Work items assigned to agents or users
- Title, description, status, priority
- Due date, completion tracking
- Foreign keys to agent and user

## Environment Variables

See `.env.example` for all available environment variables:

- `DATABASE_URL` - PostgreSQL connection string
- `SECRET_KEY` - JWT secret key
- `ACCESS_TOKEN_EXPIRE_MINUTES` - Token expiration time
- `DEBUG` - Debug mode flag
- `CORS_ORIGINS` - Allowed CORS origins

## Security

- JWT-based authentication
- Password hashing using bcrypt
- Protected endpoints with authentication middleware
- Role-based access control (admin/user)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## Support

For issues and questions, please open an issue on GitHub.
