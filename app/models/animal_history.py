from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base
import datetime

class AnimalHistory(Base):
    __tablename__ = "animal_history"

    id = Column(Integer, primary_key=True, index=True)
    animal_id = Column(Integer, ForeignKey("animals.id"))
    status = Column(String)
    shelter_id = Column(Integer, ForeignKey("shelters.id"), nullable=True)
    new_shelter_id = Column(Integer, ForeignKey("shelters.id"), nullable=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    details = Column(String, nullable=True)  # Дополнительные детали

    animal = relationship("Animal", back_populates="history")
    old_shelter = relationship("Shelter", foreign_keys=[shelter_id])
    new_shelter = relationship("Shelter", foreign_keys=[new_shelter_id])