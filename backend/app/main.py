from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.planner_router import router as planner_router

app = FastAPI(title="Smart Task Planner", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(planner_router, prefix="/plan", tags=["AI Planner"])

@app.get("/")
async def root():
    return {"message": "Smart Task Planner Backend Active!"}
