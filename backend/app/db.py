from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./smartplanner.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class TaskPlan(Base):
    __tablename__ = "task_plans"
    id = Column(Integer, primary_key=True)
    goal = Column(String)
    plan = Column(Text)

Base.metadata.create_all(bind=engine)
