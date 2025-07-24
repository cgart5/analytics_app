from sqlalchemy import Integer, String, TIMESTAMP, func
from sqlalchemy.orm import declarative_base, relationship, Mapped, mapped_column
from typing import Optional
from models.user_views import coach, fan, player

Base = declarative_base()

"""
This file contains all information for the user of any type
"""

class Users(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    role: Mapped[str] = mapped_column(String(20), nullable=False, default='fan')
    password_hash: Mapped[str] = mapped_column(String, nullable=False)
    subscription: Mapped[Optional[str]] = mapped_column(String(20), default='free')
    status: Mapped[Optional[str]] = mapped_column(String(20), default='active')
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    updated_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)
    last_login: Mapped[Optional[str]] = mapped_column(TIMESTAMP, nullable=True)

    # Relationships
    coach = relationship('Coaches')
    fan = relationship('Fans')
    player = relationship('Players')
