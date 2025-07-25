from pydantic import BaseModel
from typing import Optional

class TeamBase(BaseModel):
    head_coach_id: Optional[int]
    team_name: str
    year: int
    sport: str
    age: str
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    wins: int
    losses: int
    season_start: Optional[str]
    season_end: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]

class TeamModel(TeamBase):
    team_id:int

    class Config:
        orm_mode = True

class RosterBase(BaseModel):
    team_id: int
    player_id: int
    active: bool
    created_at: Optional[str]
    updated_at: Optional[str]

class RosterModel(RosterBase):
    roster_id: int
    class Config:
        orm_mode = True