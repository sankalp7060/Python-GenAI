import sqlite3

conn = sqlite3.connect("retail.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM customers WHERE name = ?", ("Riya",))

conn.commit()
conn.close()

print("Customer deleted successfully.")