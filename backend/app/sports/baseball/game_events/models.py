from sqlalchemy import JSON, TIMESTAMP, func, ForeignKey, Boolean, String, Integer
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from typing import Optional

Base = declarative_base()

class GameEvent(Base):
    __tablename__ = 'game_events'

    event_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    game_state_id: Mapped[int] = mapped_column(ForeignKey('game_state.game_state_id'), nullable=False)
    event_type: Mapped[str] = mapped_column(String(50), nullable=False)
    event_sequence: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)

class PitchEvent(Base):
    __tablename__ = 'pitch_events'

    pitch_event_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    event_id: Mapped[int] = mapped_column(ForeignKey('game_events.event_id'), nullable=False)
    pitcher_id: Mapped[int] = mapped_column(ForeignKey('players.player_id'), nullable=False)
    pa_id: Mapped[int] = mapped_column(ForeignKey('plate_appearances.pa_id'), nullable=False)
    pitch_data: Mapped[dict] = mapped_column(JSON, nullable=False)
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    batter_chased: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)

class PlateAppearance(Base):
    __tablename__ = 'plate_appearances'

    pa_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    batter_id: Mapped[int] = mapped_column(ForeignKey('players.player_id'), nullable=False)
    pitcher_id: Mapped[int] = mapped_column(ForeignKey('players.player_id'), nullable=False)
    outcome_id: Mapped[int] = mapped_column(ForeignKey('bat_event.bat_event_id'), nullable=False)
    rbi: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    bases_gained: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)

class BatEvent(Base):
    __tablename__ = 'bat_event'

    bat_event_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    pitch_id: Mapped[int] = mapped_column(ForeignKey('pitch_events.pitch_event_id'), nullable=False)
    outcome: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    batter_id: Mapped[int] = mapped_column(ForeignKey('players.player_id'), nullable=False)
    hit_location_x: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    hit_location_y: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    hit_type: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    exit_velocity: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)

class FieldingEvent(Base):
    __tablename__ = 'fielding_events'

    pitch_id: Mapped[int] = mapped_column(ForeignKey('pitch_events.pitch_event_id'), nullable=False)
    baserunning_event_id: Mapped[Optional[int]] = mapped_column(ForeignKey('baserunning_events.baserunning_event_id'), nullable=True)
    fielder_id: Mapped[int] = mapped_column(ForeignKey('players.player_id'), nullable=False)
    fielding_data: Mapped[dict] = mapped_column(JSON, nullable=False)
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)

class BaserunningEvent(Base):
    __tablename__ = 'baserunning_events'

    baserunning_event_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    event_id: Mapped[int] = mapped_column(ForeignKey('game_events.event_id'), nullable=False)
    runner_id: Mapped[int] = mapped_column(ForeignKey('players.player_id'), nullable=False)
    baserunning_data: Mapped[dict] = mapped_column(JSON, nullable=False)
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)

class Substitutions(Base):
    __tablename__ = 'substitutions'

    substitution_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    event_id: Mapped[int] = mapped_column(ForeignKey('game_events.event_id'), nullable=False)
    player_in_id: Mapped[int] = mapped_column(ForeignKey('players.player_id'), nullable=False)
    player_out_id: Mapped[int] = mapped_column(ForeignKey('players.player_id'), nullable=False)
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)