from sqlalchemy import create_engine, Column, Integer, String, JSON, TIMESTAMP, func, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from pydantic import BaseModel, Field
from typing import Optional
from backend.models import user
from models.user_views import coach


Base = declarative_base()

class Players(Base):
    __tablename__ = 'players'

    player_id = Column(Integer, primary_key=True, autoincrement=True)
    f_name = Column(String(20))
    l_name = Column(String(20))
    attributes = Column(JSON)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)

    #Relationships
    player = relationship('Users')
    rostered = relationship('Roster')