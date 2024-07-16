from pydantic import BaseModel
import datetime


class UserBase(BaseModel):
    username: str
    email: str
    role: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_staff: bool
    is_blocked: bool
    shelter_id: int = None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime = None

    class Config:
        orm_mode = True
