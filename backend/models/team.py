from sqlalchemy import create_engine, Column, Integer, String, JSON, TIMESTAMP, func, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from pydantic import BaseModel, Field
from typing import Optional
from models import user_views
from models import sports


Base = declarative_base()

class Teams(Base):
    __tablename__ = 'teams'

    team_id = Column(Integer, primary_key=True, autoincrement=True)
    head_coach_id = Column(Integer, ForeignKey('coaches.coach_id'), nullable=True)
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
    coaches = relationship('Coaches')
    team = relationship('Roster')
    follows = relationship('Fans')

class Roster(Base):
    __tablename__ = 'roster'
    team_id = Column(Integer, ForeignKey('teams.team_id'), primary_key=True)
    player_id = Column(Integer, ForeignKey('players.player_id'), primary_key=True)
    active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)

    rostered = relationship("Players")
    team = relationship('Teams')