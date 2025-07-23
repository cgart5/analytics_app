from sqlalchemy import create_engine, Column, Integer, String, JSON, TIMESTAMP, func, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from pydantic import BaseModel, Field
from typing import Optional
from backend.models import user
from models import team

Base = declarative_base()

"""
This file declares the model that shows which teams
the fan follows and wants to be notified about

"""

class Fans(Base):
    __tablename__ = 'fan'

    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True, nullable=False)
    team_id = Column(Integer, ForeignKey('teams.team_id'), primary_key=True, nullable=False)
    push_notifications = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)

    #Relationships
    fan = relationship('Users')
    follows = relationship('Teams')