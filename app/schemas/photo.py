from pydantic import BaseModel
import datetime


class PhotoBase(BaseModel):
    image: str


class PhotoCreate(PhotoBase):
    pass


class Photo(PhotoBase):
    id: int
    animal_id: int
    uploaded_at: datetime.datetime

    class Config:
        orm_mode = True
