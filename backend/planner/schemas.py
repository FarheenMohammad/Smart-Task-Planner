# backend/planner/schemas.py
from pydantic import BaseModel
from typing import Optional

class PlanInput(BaseModel):
    goal: str
    deadline: Optional[str] = None  # ISO date e.g. 2025-10-31
    team_size: Optional[int] = 1
    priority: Optional[str] = "medium"
