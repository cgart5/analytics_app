from sqlalchemy import JSON, TIMESTAMP, func, ForeignKey, Boolean, Integer
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from typing import Optional

Base = declarative_base()

class GameState(Base):
    __tablename__ = "game_state"

    game_state_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    game_id: Mapped[int] = mapped_column(ForeignKey('game.game_id'))
    inning: Mapped[int] = mapped_column(Integer)
    top_of_inning: Mapped[bool] = mapped_column(Boolean)
    users_lineup_id: Mapped[int] = mapped_column(ForeignKey('lineup_state.lineup_id'))
    opponent_lineup_id: Mapped[int] = mapped_column(ForeignKey('lineup_state.lineup_id'))
    users_score: Mapped[int] = mapped_column(Integer)
    opponents_score: Mapped[int] = mapped_column(Integer)
    outs: Mapped[int] = mapped_column(Integer)
    balls: Mapped[int] = mapped_column(Integer)
    strikes: Mapped[int] = mapped_column(Integer)
    batter_id: Mapped[int] = mapped_column(ForeignKey('player.player_id'))
    pitcher_id: Mapped[int] = mapped_column(ForeignKey('player.player_id'))
    runner_on_1: Mapped[Optional[int]] = mapped_column(ForeignKey('player.player_id'), nullable=True)
    runner_on_2: Mapped[Optional[int]] = mapped_column(ForeignKey('player.player_id'), nullable=True)
    runner_on_3: Mapped[Optional[int]] = mapped_column(ForeignKey('player.player_id'), nullable=True)
    batter_on_deck: Mapped[int] = mapped_column(ForeignKey('player.player_id'))
    updated_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)

class LineupState(Base):
    __tablename__ = "lineup_state"

    game_id: Mapped[int] = mapped_column(ForeignKey('game.game_id'))
    lineup_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    event_created: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)  # ForeignKey removed, set nullable
    team_id: Mapped[int] = mapped_column(ForeignKey('teams.team_id'))
    starting_lineup: Mapped[bool] = mapped_column(Boolean)
    defensive_lineup: Mapped[dict] = mapped_column(JSON)
    offensive_lineup: Mapped[dict] = mapped_column(JSON)
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)


    

