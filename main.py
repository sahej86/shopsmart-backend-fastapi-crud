from fastapi import FastAPI
from routes.customer_routes import router as customer_router
from routes.product_routes import router as product_router
from routes.transaction_routes import router as transaction_router

# Initialize FastAPI app
app = FastAPI(
    title="ShopSmart Backend API",
    description="FastAPI CRUD system for Customers, Products, and Transactions",
    version="1.0.0"
)

# Root route to show a welcome message
@app.get("/")
def read_root():
    return {"message": "Welcome to ShopSmart Backend API"}

# Register routes
app.include_router(customer_router, prefix="/customers", tags=["Customers"])
app.include_router(product_router, prefix="/products", tags=["Products"])
app.include_router(transaction_router, prefix="/transactions", tags=["Transactions"])
