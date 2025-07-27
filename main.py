from fastapi import FastAPI
from routes.customer_routes import router as customer_router
from routes.product_routes import router as product_router
from routes.transaction_routes import router as transaction_router
from database import Base, engine

# Create all tables from models
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="ShopSmart Backend API",
    description="FastAPI CRUD system for Customers, Products, and Transactions",
    version="1.0.0"
)

# Register routes
app.include_router(customer_router, prefix="/customers", tags=["Customers"])
app.include_router(product_router, prefix="/products", tags=["Products"])
app.include_router(transaction_router, prefix="/transactions", tags=["Transactions"])
