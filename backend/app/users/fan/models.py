from sqlalchemy import Integer, TIMESTAMP, func, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship, Mapped, mapped_column
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

    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'), primary_key=True, nullable=False)
    team_id: Mapped[int] = mapped_column(ForeignKey('teams.team_id'), primary_key=True, nullable=False)
    push_notifications: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)

    # Relationships
    fan = relationship('Users')
    follows = relationship('Teams')