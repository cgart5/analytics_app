from pydantic import BaseModel
from typing import Optional, Dict

class GameEventBase(BaseModel):
    game_state_id: int
    event_type: str
    event_sequence: Optional[int]
    created_at: Optional[str]

class GameEventModel(GameEventBase):
    game_event_id: int

    class Config:
        orm_mode = True

class PitchEventBase(BaseModel):
    event_id: int
    pitcher_id: int
    pa_id: int
    pitch_data: Dict
    created_at: Optional[str]
    batter_chased: Optional[bool]

class PitchEventModel(PitchEventBase):
    pitch_event_id: int

    class Config:
        orm_mode = True

class PlateAppearanceBase(BaseModel):
    batter_id: int
    pitcher_id: int
    outcome_id: int
    rbi: Optional[int]
    bases_gained: Optional[int]
    created_at: Optional[str]

class PlateAppearanceModel(PlateAppearanceBase):
    pa_id: int

    class Config:
        orm_mode = True

class BatEventBase(BaseModel):
    pitch_id: int
    outcome: str
    description: Optional[str]
    batter_id: int
    hit_location_x: Optional[int]
    hit_location_y: Optional[int]
    hit_type: Optional[str]
    exit_velocity: Optional[int]
    created_at: Optional[str]

class BatEventModel(BatEventBase):
    bat_event_id: int

    class Config:
        orm_mode = True

class FieldingEventBase(BaseModel):
    pitch_id: int
    baserunning_event_id: Optional[int]
    fielder_id: int
    fielding_data: Dict
    created_at: Optional[str]

class FieldingEventModel(FieldingEventBase):
    fielding_event_id:int
    class Config:
        orm_mode = True

class BaserunningEventBase(BaseModel):
    event_id: int
    runner_id: int
    baserunning_data: Dict
    created_at: Optional[str]

class BaserunningEventModel(BaserunningEventBase):
    baserunning_event_id: int
    class Config:
        orm_mode = True

class SubstitutionsBase(BaseModel):
    event_id: int
    player_in_id: int
    player_out_id: int
    created_at: Optional[str]


class SubstitutionsModel(SubstitutionsBase):
    substitution_id: int
    class Config:
        orm_mode = True