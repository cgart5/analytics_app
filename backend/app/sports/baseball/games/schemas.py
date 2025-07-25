from pydantic import BaseModel
from typing import Optional

class GameBase(BaseModel):
    scheduled_date: str
    street_address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip_code: Optional[str]
    field_num: Optional[int]
    team_id: int
    opponent_id: int
    home: Optional[bool]
    start_time: Optional[str]
    end_time: Optional[str]
    game_status: Optional[str]
    weather: Optional[str]
    field_conditions: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]

class GameModel(GameBase):
    game_id: int

    class Config:
        orm_mode = True 