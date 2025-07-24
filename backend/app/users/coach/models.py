from backend.models import user
from sqlalchemy import Integer, String, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Mapped, mapped_column
from typing import Optional

Base = declarative_base()

class Coaches(Base):
    __tablename__ = 'coaches'

    coach_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    f_name: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    l_name: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    team_id: Mapped[int] = mapped_column(ForeignKey('teams.team_id'))
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    updated_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)

    # Relationships
    coach = relationship('Users')

