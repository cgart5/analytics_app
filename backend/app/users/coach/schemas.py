from pydantic import BaseModel
from typing import Optional

class CoachBase(BaseModel):
    f_name: Optional[str]
    l_name: Optional[str]
    user_id: int
    team_id: int
    created_at: Optional[str]
    updated_at: Optional[str]

class CoachModel(CoachBase):
    coach_id: int
    class Config:
        orm_mode = True