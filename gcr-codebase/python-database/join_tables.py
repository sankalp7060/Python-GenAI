import sqlite3

conn = sqlite3.connect("retail.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    FOREIGN KEY(customer_id) REFERENCES customers(id)
)
""")

# sample data
cursor.execute("INSERT INTO orders (customer_id) VALUES (1)")
cursor.execute("INSERT INTO orders (customer_id) VALUES (2)")

cursor.execute("""
SELECT customers.name, orders.id
FROM customers
INNER JOIN orders ON customers.id = orders.customer_id
""")

rows = cursor.fetchall()

for name, order_id in rows:
    print(f"{name} - OrderID: {order_id}")

conn.commit()
conn.close()