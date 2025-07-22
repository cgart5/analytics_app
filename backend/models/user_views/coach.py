from sqlalchemy import create_engine, Column, Integer, String, JSON, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from pydantic import BaseModel, Field
from typing import Optional
from models.user_model import Users

Base = declarative_base()


class Teams(Base):
    __tablename__ = 'teams'

    team_id = Column(Integer, primary_key=True, autoincrement=True)
    coach_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    team_name = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    sport = Column(String(50), nullable=False)
    age = Column(String(20), nullable=False)
    city = Column(String(100))
    state = Column(String(50))
    country = Column(String(50))
    wins = Column(Integer, default=0)
    losses = Column(Integer, default=0)
    season_start = Column(TIMESTAMP)
    season_end = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)
    
    coach = relationship('Users') 
