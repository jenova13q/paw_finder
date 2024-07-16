from pydantic import BaseModel
import datetime


class AnimalHistoryBase(BaseModel):
    status: str
    details: str = None


class AnimalHistoryCreate(AnimalHistoryBase):
    shelter_id: int = None
    new_shelter_id: int = None


class AnimalHistory(AnimalHistoryBase):
    id: int
    animal_id: int
    shelter_id: int = None
    new_shelter_id: int = None
    timestamp: datetime.datetime

    class Config:
        orm_mode = True
