import sqlite3

conn = sqlite3.connect("webshop.db")
curser = conn.cursor()

curser.execute("SELECT name, price FROM products")
rows = curser.fetchall()

print(rows)
conn.close()
