from pydantic import BaseModel
from typing import Optional

class FanBase(BaseModel):
    team_id: int
    push_notifications: bool
    created_at: Optional[str]

class FanModel(FanBase):
    user_id: int
    class Config:
        orm_mode = True