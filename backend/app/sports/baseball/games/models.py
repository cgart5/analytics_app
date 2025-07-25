from sqlalchemy import create_engine, String, JSON, TIMESTAMP, func, ForeignKey, Boolean, Date, TIME, Integer
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from ....teams import models

Base = declarative_base()

class Game(Base):
    __tablename__ = "game"

    game_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    scheduled_date: Mapped[str] = mapped_column(Date, nullable=False)
    street_address: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    city: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    state: Mapped[Optional[str]] = mapped_column(String(16), nullable=True)
    zip_code: Mapped[Optional[str]] = mapped_column(String(9), nullable=True)
    field_num: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    user_team_id: Mapped[int] = mapped_column(ForeignKey('teams.team_id'))
    opponent_team_id: Mapped[int] = mapped_column(ForeignKey('teams.team_id'))
    home: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    start_time: Mapped[Optional[str]] = mapped_column(TIME, nullable=True)
    end_time: Mapped[Optional[str]] = mapped_column(TIME, nullable=True)
    game_status: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    weather: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    field_conditions: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)

