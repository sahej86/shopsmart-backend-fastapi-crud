# 🛒 ShoppersSmart – E-commerce Backend (Flask + MySQL)

**ShoppersSmart** is a Flask-based backend application designed to manage **Customers**, **Products**, and **Transactions** for an e-commerce platform. It also sets the foundation for integrating a future **machine learning recommendation system**.

---

## 🔍 Features

- 🧑‍💼 Manage customer records (CRUD)
- 📦 Add and fetch product details
- 💳 Track customer transactions
- 🔗 MySQL database with raw SQL (no ORM)
- 🔥 Built using Python Flask
- 📮 REST API tested with Postman
- 📈 ML-ready structure for future recommendations

---

## 🧰 Tech Stack

| Layer          | Technology                |
|----------------|---------------------------|
| 🐍 Language     | Python 3.x                |
| ⚙️ Framework    | Flask                     |
| 🛢️ Database     | MySQL                     |
| 🔌 DB Driver    | mysql-connector-python    |
| 🧪 API Testing | Postman                   |
| 🤖 ML (Future) | pandas, scikit-learn      |

---

## 📁 Project Structure

shopsmart_app/
│
├── models/
│ ├── customer.py
│ ├── product.py
│ └── transaction.py
│
├── routes/
│ ├── customer_routes.py
│ ├── product_routes.py
│ └── transaction_routes.py
│
├── database.py
├── main.py
├── requirements.txt
└── README.md



---

## 🗄️ Database Setup (MySQL)

```sql
CREATE DATABASE shopsmart;

USE shopsmart;

CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  phone_number VARCHAR(20),
  location VARCHAR(100)
);

CREATE TABLE products (
  product_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  description TEXT,
  price DECIMAL(10,2)
);

CREATE TABLE transactions (
  transaction_id INT AUTO_INCREMENT PRIMARY KEY,
  customer_id INT,
  product_id INT,
  purchase_date DATE,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);



🚀 How to Run the App
bash

# Clone the repository
git clone https://github.com/yourusername/shopsmart-backend.git
cd shopsmart-backend

# Create virtual environment (optional)
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run the Flask app
python main.py
Then open your browser and go to:
🌐 http://127.0.0.1:5000
📄 API Docs: http://127.0.0.1:5000/docs


📊 REST API Endpoints
| Method | Endpoint          | Description        |
| ------ | ----------------- | ------------------ |
| POST   | `/customers`      | Add a customer     |
| GET    | `/customers`      | Get all customers  |
| GET    | `/customers/<id>` | Get customer by ID |
| PUT    | `/customers/<id>` | Update customer    |
| DELETE | `/customers/<id>` | Delete customer    |


| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| POST   | `/products`      | Add product       |
| GET    | `/products`      | Get all products  |
| GET    | `/products/<id>` | Get product by ID |
| PUT    | `/products/<id>` | Update product    |
| DELETE | `/products/<id>` | Delete product    |


| Method | Endpoint             | Description           |
| ------ | -------------------- | --------------------- |
| POST   | `/transactions`      | Add transaction       |
| GET    | `/transactions`      | Get all transactions  |
| GET    | `/transactions/<id>` | Get transaction by ID |
| PUT    | `/transactions/<id>` | Update transaction    |
| DELETE | `/transactions/<id>` | Delete transaction    |


🤖 Future Integration: Product Recommendation Engine
This backend is ML-ready and supports future integration of recommendation features like:

“🛍️ Customers who bought this item also bought…”

“📌 You may also like…”

“✨ Top picks based on your past purchases”

Planned techniques:

📊 Co-purchase analysis

🧠 Collaborative filtering

👥 Customer segmentation using scikit-learn or similar tools


📦 Requirements
Install all required packages with:
bash

pip install -r requirements.txt


🔖 License, Contact & Support

🔒 License  
This project is open-source and available under the MIT License.

📬 Contact  
For questions or feedback, email: sahejkadam0@gmail.com

⭐ Star this repo if it helped you!