from pydantic import BaseModel
import datetime


class AnimalBase(BaseModel):
    name: str
    species: str
    breed: str
    color: str
    age: int
    description: str
    special_markings: str
    status: str = "shelter_resident"
    is_searching: bool = False


class AnimalCreate(AnimalBase):
    pass


class Animal(AnimalBase):
    id: int
    shelter_id: int = None
    search_user_id: int = None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime = None

    class Config:
        orm_mode = True
