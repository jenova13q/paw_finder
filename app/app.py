from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.models.database import SessionLocal, engine
from . import models

# Create all tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def read_root():
    return {"message": "Hello, PawFinder!"}
