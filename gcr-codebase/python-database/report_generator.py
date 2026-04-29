import sqlite3

conn = sqlite3.connect("retail.db")
cursor = conn.cursor()

cursor.execute("""
SELECT customers.name, COUNT(orders.id) as order_count
FROM customers
JOIN orders ON customers.id = orders.customer_id
GROUP BY customers.id
ORDER BY order_count DESC
LIMIT 3
""")

rows = cursor.fetchall()

print("Top 3 Customers:")
for i, (name, count) in enumerate(rows, start=1):
    print(f"{i}. {name} - {count} Orders")

conn.close()