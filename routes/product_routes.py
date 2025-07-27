from fastapi import APIRouter, HTTPException
from database import cursor, conn
from models.product import Product

router = APIRouter()

# GET all products
@router.get("/", response_model=list[Product])
def get_products():
    try:
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# GET product by ID
@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):
    cursor.execute("SELECT * FROM products WHERE product_id = %s", (product_id,))
    product = cursor.fetchone()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# POST create product
@router.post("/", response_model=dict)
def create_product(product: Product):
    try:
        query = "INSERT INTO products (product_id, name, category, price) VALUES (%s, %s, %s, %s)"
        values = (product.product_id, product.name, product.category, product.price)
        cursor.execute(query, values)
        conn.commit()
        return {"message": "Product created successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# DELETE product
@router.delete("/{product_id}", response_model=dict)
def delete_product(product_id: int):
    cursor.execute("SELECT * FROM products WHERE product_id = %s", (product_id,))
    product = cursor.fetchone()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    cursor.execute("DELETE FROM products WHERE product_id = %s", (product_id,))
    conn.commit()
    return {"message": "Product deleted successfully"}
