from sqlalchemy import create_engine, Column, Integer, String, JSON, TIMESTAMP, func, ForeignKey, Boolean, Date, TIME
from sqlalchemy.orm import sessionmaker, declarative_base
from pydantic import BaseModel, Field
from typing import Optional
from ....sports import baseball

Base = declarative_base()

class GameEvent(Base):
    __tablename__ = 'game_events'
    
    event_id = Column(Integer, primary_key=True, autoincrement=True,index=True)
    game_state_id = Column(Integer, ForeignKey('game_state.game_state_id'), nullable=False)
    event_type = Column(String(50), nullable=False)
    event_sequence = Column(Integer, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)


class PitchEvent(Base):
    __tablename__ = 'pitch_events'

    event_id = Column(Integer, ForeignKey('game_events.event_id'), nullable=False)
    pitch_event_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    pitcher_id = Column(Integer, ForeignKey('players.player_id'), nullable=False)
    pa_id = Column(Integer, ForeignKey('plate_appearances.pa_id'), nullable=False)
    pitch_data = Column(JSON, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    batter_chased = Column(Boolean, nullable=True)


class PlateAppearance(Base):
    __tablename__ = 'plate_appearances'

    pa_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    batter_id = Column(Integer, ForeignKey('players.player_id'), nullable=False)
    pitcher_id = Column(Integer, ForeignKey('players.player_id'), nullable=False)
    outcome_id = Column(Integer, ForeignKey('bat_event.bat_event_id'), nullable=False)
    rbi = Column(Integer, nullable=True)
    bases_gained = Column(Integer, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)

class BatEvent(Base):
    __tablename__ = 'bat_event'

    bat_event_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    pitch_id = Column(Integer, ForeignKey('pitch_events.pitch_event_id'), nullable=False)
    outcome = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    batter_id = Column(Integer, ForeignKey('players.player_id'), nullable=False)
    hit_location_x = Column(Integer, nullable=True)
    hit_location_y = Column(Integer, nullable=True)
    hit_type = Column(String(50), nullable=True)
    exit_velocity = Column(Integer, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)

class FieldingEvent(Base):
    __tablename__ = 'fielding_events'

    pitch_id = Column(Integer, ForeignKey('pitch_events.pitch_event_id'), nullable=False)
    baserunning_event_id = Column(Integer, ForeignKey('baserunning_events.baserunning_event_id'), nullable=True)
    fielder_id = Column(Integer, ForeignKey('players.player_id'), nullable=False)
    fielding_data = Column(JSON, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)

class BaserunningEvent(Base):
    __tablename__ = 'baserunning_events'

    baserunning_event_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    event_id = Column(Integer, ForeignKey('game_events.event_id'), nullable=False)
    runner_id = Column(Integer, ForeignKey('players.player_id'), nullable=False)
    baserunning_data = Column(JSON, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)

class Substitutions(Base):
    __tablename__ = 'substitutions'

    event_id = Column(Integer, ForeignKey('game_events.event_id'), nullable=False)
    substitution_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    player_in_id = Column(Integer, ForeignKey('players.player_id'), nullable=False)
    player_out_id = Column(Integer, ForeignKey('players.player_id'), nullable=False)    
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)