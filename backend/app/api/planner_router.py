from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.llm_service import generate_plan

router = APIRouter()

class GoalInput(BaseModel):
    goal: str

@router.post("/")
async def create_plan(request: GoalInput):
    try:
        plan = generate_plan(request.goal)
        return {"goal": request.goal, "plan": plan}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
