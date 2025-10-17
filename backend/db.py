# backend/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import os

_engine = None
_SessionLocal = None

def init_db(database_url: str):
    global _engine, _SessionLocal
    _engine = create_engine(database_url, connect_args={"check_same_thread": False})
    _SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)
    Base.metadata.create_all(bind=_engine)

def get_session():
    global _SessionLocal
    if _SessionLocal is None:
        raise RuntimeError("DB not initialized. Call init_db first.")
    return _SessionLocal()
