from sqlalchemy import Integer, String, TIMESTAMP, func, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship, Mapped, mapped_column
from typing import Optional

Base = declarative_base()

class Teams(Base):
    __tablename__ = 'teams'

    team_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    head_coach_id: Mapped[Optional[int]] = mapped_column(ForeignKey('coaches.coach_id'), nullable=True)
    team_name: Mapped[str] = mapped_column(String(100), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    sport: Mapped[str] = mapped_column(String(50), nullable=False)
    age: Mapped[str] = mapped_column(String(20), nullable=False)
    city: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    state: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    country: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    wins: Mapped[int] = mapped_column(Integer, default=0)
    losses: Mapped[int] = mapped_column(Integer, default=0)
    season_start: Mapped[Optional[str]] = mapped_column(TIMESTAMP, nullable=True)
    season_end: Mapped[Optional[str]] = mapped_column(TIMESTAMP, nullable=True)
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    updated_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)
    
    coach = relationship('Users')
    coaches = relationship('Coaches')
    team = relationship('Roster')
    follows = relationship('Fans')

class Roster(Base):
    __tablename__ = 'roster'
    team_id: Mapped[int] = mapped_column(ForeignKey('teams.team_id'), primary_key=True)
    player_id: Mapped[int] = mapped_column(ForeignKey('players.player_id'), primary_key=True)
    active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    updated_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)

    rostered = relationship("Players")
    team = relationship('Teams')