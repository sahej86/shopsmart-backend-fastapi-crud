from pydantic import BaseModel
from datetime import datetime

class Transaction(BaseModel):
    transaction_id: int
    customer_id: int
    product_id: int
    quantity: int
    transaction_date: datetime
