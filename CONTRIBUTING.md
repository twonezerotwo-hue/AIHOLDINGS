# Contributing to AI Holdings

Thank you for your interest in contributing to the AI Holdings Enterprise Management System!

## Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/AIHOLDINGS.git
   cd AIHOLDINGS
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up the database:
   ```bash
   # Using Docker (recommended)
   docker-compose up -d db
   
   # Or manually with PostgreSQL
   createdb aiholdings
   createdb aiholdings_test
   ```

6. Copy the environment file:
   ```bash
   cp .env.example .env
   ```

## Running the Application

### Development Mode
```bash
uvicorn app.main:app --reload
```

### Using Docker
```bash
docker-compose up
```

## Running Tests

### All Tests
```bash
pytest
```

### With Coverage
```bash
pytest --cov=app --cov-report=html
```

### Unit Tests Only
```bash
pytest tests/unit/
```

### Integration Tests Only
```bash
pytest tests/integration/
```

## Code Style

This project follows Python best practices:

- Use type hints where possible
- Follow PEP 8 style guide
- Write docstrings for all functions and classes
- Keep functions small and focused

## Adding New Features

### Adding a New Model

1. Create the model in `app/models/`
2. Create schemas in `app/schemas/`
3. Create CRUD operations in `app/crud/`
4. Create API endpoints in `app/api/v1/`
5. Add the router to `app/api/v1/router.py`
6. Write tests in `tests/`

### Example: Adding a Project Model

1. **Model** (`app/models/project.py`):
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.session import Base

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    company_id = Column(Integer, ForeignKey("companies.id"))
```

2. **Schema** (`app/schemas/project.py`):
```python
from pydantic import BaseModel

class ProjectBase(BaseModel):
    name: str
    company_id: int

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    
    class Config:
        from_attributes = True
```

3. **CRUD** (`app/crud/project.py`):
```python
from sqlalchemy.orm import Session
from app.models.project import Project
from app.schemas.project import ProjectCreate

def create_project(db: Session, project: ProjectCreate) -> Project:
    db_project = Project(**project.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project
```

4. **Router** (`app/api/v1/projects.py`):
```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.crud import project as crud_project
from app.schemas.project import Project, ProjectCreate

router = APIRouter()

@router.post("/", response_model=Project)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    return crud_project.create_project(db=db, project=project)
```

5. **Update Router** (`app/api/v1/router.py`):
```python
from app.api.v1 import projects

api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
```

## Testing Guidelines

- Write tests for all new features
- Ensure tests are isolated and don't depend on external state
- Use fixtures from `tests/conftest.py`
- Mock external dependencies

## Pull Request Process

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit:
   ```bash
   git add .
   git commit -m "Add your feature"
   ```

3. Run tests:
   ```bash
   pytest
   ```

4. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

5. Create a Pull Request on GitHub

## Code Review Process

- All submissions require review
- Address reviewer feedback
- Ensure CI/CD passes
- Squash commits if requested

## Questions?

Feel free to open an issue for questions or discussions!
