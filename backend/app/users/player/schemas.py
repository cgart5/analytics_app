from pydantic import BaseModel
from typing import Optional, Dict

class PlayerBase(BaseModel):
    f_name: Optional[str]
    l_name: Optional[str]
    attributes: Optional[Dict]
    user_id: int
    created_at: Optional[str]
    updated_at: Optional[str]

class PlayerModel(PlayerBase):
    player_id:int
    class Config:
        orm_mode = True