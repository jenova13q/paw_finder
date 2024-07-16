from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base
import datetime


class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    species = Column(String)
    breed = Column(String)
    color = Column(String)
    age = Column(Integer)
    description = Column(String)
    special_markings = Column(String)
    status = Column(String, default="shelter_resident")
    shelter_id = Column(Integer, ForeignKey("shelters.id"), nullable=True)
    is_searching = Column(Boolean, default=False)
    search_user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    shelter = relationship("Shelter", back_populates="animals")
    photos = relationship("Photo", back_populates="animal")
    history = relationship("AnimalHistory", back_populates="animal", cascade="all, delete-orphan")
    search_user = relationship("User", back_populates="search_animals")

    @property
    def is_old_resident(self):
        six_months_ago = datetime.datetime.utcnow() - datetime.timedelta(days=180)
        return self.status == "shelter_resident" and self.created_at < six_months_ago
