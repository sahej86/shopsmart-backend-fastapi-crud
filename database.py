import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="3666",
    database="shopsmart"
)

cursor = conn.cursor(dictionary=True)
