from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
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

@app.post("/add/")
async def add_test(name: str, db: Session = Depends(get_db)):
    test_entry = models.TestTable(name=name)
    db.add(test_entry)
    db.commit()
    db.refresh(test_entry)
    return {"id": test_entry.id, "name": test_entry.name}