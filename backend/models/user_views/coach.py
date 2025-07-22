from backend.models import user
from sqlalchemy import create_engine, Column, Integer, String, JSON, TIMESTAMP, func, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from pydantic import BaseModel, Field
from typing import Optional
from models import team
from models.user_views import player, fan

Base = declarative_base()

class Coaches(Base):
    __tablename__ = 'coaches'

    coach_id = Column(Integer, primary_key=True, autoincrement=True)
    f_name = Column(String(20))
    l_name = Column(String(20))
    user_id = Column(Integer, ForeignKey('users.user_id'))
    team_id = Column(Integer, ForeignKey('teams.team_id'))
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)

    #Relationships
    coach = relationship('Users')
    coaches = relationship('Teams')

