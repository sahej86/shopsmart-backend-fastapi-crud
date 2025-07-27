from fastapi import APIRouter, HTTPException
from models.transaction import Transaction
from database import cursor, conn

router = APIRouter()

# GET all transactions
@router.get("/", response_model=list[Transaction])
def get_transactions():
    try:
        cursor.execute("SELECT * FROM transactions")
        transactions = cursor.fetchall()
        return transactions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# GET transaction by ID
@router.get("/{transaction_id}", response_model=Transaction)
def get_transaction(transaction_id: int):
    cursor.execute("SELECT * FROM transactions WHERE transaction_id = %s", (transaction_id,))
    txn = cursor.fetchone()
    if not txn:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return txn

# POST create transaction
@router.post("/", response_model=dict)
def create_transaction(transaction: Transaction):
    try:
        cursor.execute("SELECT * FROM customers WHERE customer_id = %s", (transaction.customer_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Customer not found")

        cursor.execute("SELECT * FROM products WHERE product_id = %s", (transaction.product_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Product not found")

        query = """
            INSERT INTO transactions (transaction_id, customer_id, product_id, quantity, transaction_date)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            transaction.transaction_id,
            transaction.customer_id,
            transaction.product_id,
            transaction.quantity,
            transaction.transaction_date,
        )
        cursor.execute(query, values)
        conn.commit()
        return {"message": "Transaction created successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
