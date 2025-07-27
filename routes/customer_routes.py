from fastapi import APIRouter, HTTPException
from database import conn, cursor
from models.customer import Customer
from typing import List

router = APIRouter()

# GET: Fetch all customers
@router.get("/", response_model=List[Customer])
def get_customers():
    try:
        cursor.execute("SELECT * FROM customers")
        rows = cursor.fetchall()
        customers = [
            Customer(
                customer_id=row['customer_id'],
                name=row['name'],
                email=row['email'],
                phone_number=row['phone_number'],
                location=row['location'],
            )
            for row in rows
        ]
        return customers
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# POST: Create a new customer
@router.post("/", response_model=Customer)
def create_customer(customer: Customer):
    try:
        cursor.execute("""
            INSERT INTO customers (customer_id, name, email, phone_number, location)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            customer.customer_id,
            customer.name,
            customer.email,
            customer.phone_number,
            customer.location
        ))
        conn.commit()
        return customer
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# PUT: Update an existing customer
@router.put("/{customer_id}", response_model=Customer)
def update_customer(customer_id: int, customer: Customer):
    try:
        cursor.execute("""
            UPDATE customers SET name=%s, email=%s, phone_number=%s, location=%s
            WHERE customer_id=%s
        """, (
            customer.name,
            customer.email,
            customer.phone_number,
            customer.location,
            customer_id
        ))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Customer not found")
        conn.commit()
        return customer
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# DELETE: Delete a customer
@router.delete("/{customer_id}")
def delete_customer(customer_id: int):
    try:
        cursor.execute("DELETE FROM customers WHERE customer_id=%s", (customer_id,))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Customer not found")
        conn.commit()
        return {"message": "Customer deleted successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
