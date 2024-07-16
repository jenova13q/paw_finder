from pydantic import BaseModel
import datetime


class ShelterAddressBase(BaseModel):
    address: str
    city: str
    state: str
    zip_code: str
    country: str
    latitude: float = None
    longitude: float = None


class ShelterAddressCreate(ShelterAddressBase):
    pass


class ShelterAddress(ShelterAddressBase):
    id: int
    shelter_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True
