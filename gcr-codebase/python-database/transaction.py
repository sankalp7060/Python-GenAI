import sqlite3

conn = sqlite3.connect("retail.db")
cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", ("Temp", "temp@mail.com"))
    cursor.execute("DELETE FROM customers WHERE id = ?", (999,))  # might fail logically

    # force error
    cursor.execute("INSERT INTO customers (id, name) VALUES (?, ?)", (1, "Duplicate"))

    conn.commit()
except Exception:
    conn.rollback()
    print("Transaction rolled back due to error.")
finally:
    conn.close()