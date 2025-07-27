from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.transaction import Transaction
from models.customer import Customer
from models.product import Product

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET all transactions
@router.get("/")
def get_transactions(db: Session = Depends(get_db)):
    return db.query(Transaction).all()

# POST create transaction
@router.post("/")
def create_transaction(transaction: Transaction, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.customer_id == transaction.customer_id).first()
    product = db.query(Product).filter(Product.product_id == transaction.product_id).first()

    if not customer or not product:
        raise HTTPException(status_code=404, detail="Customer or Product not found")

    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction

# GET transaction by ID
@router.get("/{transaction_id}")
def get_transaction(transaction_id: int, db: Session = Depends(get_db)):
    txn = db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
    if not txn:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return txn
