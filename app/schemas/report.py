from pydantic import BaseModel
import datetime


class ReportBase(BaseModel):
    user_id: int
    animal_id: int
    location: str
    date_found: datetime.datetime
    description: str


class ReportCreate(ReportBase):
    pass


class Report(ReportBase):
    id: int

    class Config:
        orm_mode = True
