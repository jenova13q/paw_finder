from pydantic import BaseModel
import datetime


class ShelterBase(BaseModel):
    name: str
    phone: str
    email: str
    website: str = None


class ShelterCreate(ShelterBase):
    pass


class Shelter(ShelterBase):
    id: int
    approved: bool
    is_blocked: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime = None

    class Config:
        orm_mode = True
