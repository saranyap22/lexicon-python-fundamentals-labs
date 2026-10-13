import sqlite3

conn = sqlite3.connect("webshop.db")
cursor = conn.cursor()

# Exercise 1

cursor.execute(
    "SELECT concat(concat_ws(' ', first_name,last_name), '(', city, ')') AS customer FROM customers")

for (customer,) in cursor.fetchall():
    print(customer)

# More flexible way of doing Exercise 1
cursor.execute("SELECT first_name,last_name,city FROM customers")

for first_name, last_name, city in cursor.fetchall():
    print(f"{first_name} {last_name} ( {city} )")

# Exercise 2
max_price_limit = input("Please enter your max price limit: ")
price = int(max_price_limit)

cursor.execute(
    "SELECT name,category,price,stock FROM products WHERE price <= ?", (price,))

for name, category, price, stock in cursor.fetchall():
    print(f"{name:<20} {category:<20} {price} kr {stock:15}")

# Exercise 3
product_category = input("Enter product category to see number of products: ")

cursor.execute("SELECT COUNT(*) FROM products WHERE category = ?",
               (product_category,))

print(f"{product_category:<15} : {cursor.fetchone()[0]}")

# Exercise 4 : Problem of building SQL with f string
# In this case user can inject direct SQL query in the input that might harm output or corrupt the database (Ex. DELETE * FROM products;)
product_category = input("Enter product category to see number of products: ")

cursor.execute(
    f"SELECT COUNT(*) FROM products WHERE category = '{product_category}'")
print(f"{product_category:<15} : {cursor.fetchone()[0]}")

# In the below input SQL Injection is happened and every row incorrectly counted
# Enter product category to see number of products: ' OR '1' = '1
# ' OR '1' = '1   : 12


# Excercise 5
