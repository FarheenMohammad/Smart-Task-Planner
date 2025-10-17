# backend/models.py
from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Plan(Base):
    __tablename__ = "plans"
    id = Column(Integer, primary_key=True, index=True)
    goal = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    tasks = Column(JSON, nullable=False)
