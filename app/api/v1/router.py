"""API v1 router combining all endpoints"""

from fastapi import APIRouter
from app.api.v1 import auth, users, holdings, companies, departments, agents, tasks

api_router = APIRouter()

# Include all routers with their prefixes and tags
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(holdings.router, prefix="/holdings", tags=["holdings"])
api_router.include_router(companies.router, prefix="/companies", tags=["companies"])
api_router.include_router(departments.router, prefix="/departments", tags=["departments"])
api_router.include_router(agents.router, prefix="/agents", tags=["agents"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
