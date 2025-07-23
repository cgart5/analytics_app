from sqlalchemy import create_engine, Column, Integer, String, JSON, TIMESTAMP, func, ForeignKey, Boolean, Date, TIME
from sqlalchemy.orm import sessionmaker, declarative_base
from pydantic import BaseModel, Field
from typing import Optional
from models import team

Base = declarative_base()

class Game(Base):
    __tablename__ = "game"

    game_id = Column(Integer, primary_key=True, autoincrement=True)
    scheduled_date = Column(Date, nullable=False)
    street_address = Column(String(30))
    city = Column(String(20))
    state = Column(String(16))
    zip_code = Column(String(9))
    field_num = Column(Integer)
    team_id = Column(Integer, ForeignKey('teams.team_id'))
    opponent_id = Column(Integer, ForeignKey('teams.team_id'))
    home = Column(Boolean)
    start_time = Column(TIME)
    end_time = Column(TIME)
    game_status = Column(String(20))
    weather = Column(String(20))
    field_conditions = Column(String(50))
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)