from sqlalchemy import create_engine, Column, Integer, String, JSON, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, Mapped, mapped_column
from typing import Optional
from backend.models import user
from models.user_views import coach


Base = declarative_base()

class Players(Base):
    __tablename__ = 'players'

    player_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    f_name: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    l_name: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    attributes: Mapped[dict] = mapped_column(JSON, nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    updated_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)

    # Relationships
    player = relationship('Users')
    rostered = relationship('Roster')