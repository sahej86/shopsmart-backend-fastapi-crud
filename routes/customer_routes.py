from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.customer import Customer
from database import SessionLocal

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_customers(db: Session = Depends(get_db)):
    return db.query(Customer).all()
