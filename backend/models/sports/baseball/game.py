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




class GameState(Base):
    __tablename__ = "game_state"

    game_state_id = Column(Integer, primary_key=True, autoincrement=True)
    game_id = Column(Integer, ForeignKey('game.game_id'))
    inning = Column(Integer)
    top_of_inning = Column(Boolean)
    users_lineup_id = Column(Integer, ForeignKey('lineup_state.lineup_id'))
    opponent_lineup_id = Column(Integer, ForeignKey('lineup_state.lineup_id'))
    users_score = Column(Integer)
    opponents_score = Column(Integer)
    outs = Column(Integer)
    balls = Column(Integer)
    strikes = Column(Integer)
    batter_id = Column(Integer, ForeignKey('player.player_id'))
    pitcher_id = Column(Integer, ForeignKey('player.player_id'))
    runner_on_1 = Column(Integer, ForeignKey('player.player_id'), nullable=True)
    runner_on_2 = Column(Integer, ForeignKey('player.player_id'), nullable=True)
    runner_on_3 = Column(Integer, ForeignKey('player.player_id'), nullable=True)
    batter_on_deck = Column(Integer, ForeignKey('player.player_id'))
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)



class LineupState(Base):
    __tablename__ = "lineup_state"

    game_id = Column(Integer, ForeignKey('game.game_id'))
    lineup_id = Column(Integer, primary_key=True, autoincrement=True)
    event_created = Column(Integer, """ForeignKey(null)""")
    team_id = Column(Integer, ForeignKey('teams.team_id'))
    starting_lineup = Column(Boolean)
    defensive_lineup = Column(JSON)
    offensive_lineup = Column(JSON)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)

    
    
    