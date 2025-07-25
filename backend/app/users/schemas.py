from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    email: str
    username: str
    role: str
    password_hash: str
    subscription: Optional[str]
    status: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]
    last_login: Optional[str]

class UserModel(UserBase):
    user_id: int

    class Config:
        orm_mode = True