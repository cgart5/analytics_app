from sqlalchemy import create_engine, Column, Integer, String, JSON, TIMESTAMP, func
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from pydantic import BaseModel, Field
from typing import Optional
from models.user_views import coach, fan, player
Base = declarative_base()

"""
This fie contains all information for the user of any type

"""

class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    role = Column(String(20), nullable=False, default='fan')
    password_hash = Column(String, nullable=False)
    subscription = Column(String(20), default='free')
    status = Column(String(20), default='active')
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)
    last_login = Column(TIMESTAMP, nullable=True)

    # Relationships
    coach = relationship('Coaches')
    fan = relationship('Fans')
    player = relationship('Players')
