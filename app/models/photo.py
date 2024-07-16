from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base
import datetime


class Photo(Base):
    __tablename__ = "photos"

    id = Column(Integer, primary_key=True, index=True)
    animal_id = Column(Integer, ForeignKey("animals.id"))
    image = Column(String)
    uploaded_at = Column(DateTime, default=datetime.datetime.utcnow)

    animal = relationship("Animal", back_populates="photos")
