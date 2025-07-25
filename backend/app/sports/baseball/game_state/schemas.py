from pydantic import BaseModel
from typing import Optional, Dict

class GameStateBase(BaseModel):
    game_id: int
    inning: int
    top_of_inning: bool
    users_lineup_id: int
    opponent_lineup_id: int
    users_score: int
    opponents_score: int
    outs: int
    balls: int
    strikes: int
    batter_id: int
    pitcher_id: int
    runner_on_1: Optional[int]
    runner_on_2: Optional[int]
    runner_on_3: Optional[int]
    batter_on_deck: int
    updated_at: Optional[str]

class GameStateModel(GameStateBase):
    game_state_id: int

    class Config:
        orm_mode = True

class LineupStateBase(BaseModel):
    game_id: int
    event_created: Optional[int]
    team_id: int
    starting_lineup: bool
    defensive_lineup: Dict
    offensive_lineup: Dict
    created_at: Optional[str]

class LineupStateModel(LineupStateBase):
    lineup_id: int

    class Config:
        orm_mode = True