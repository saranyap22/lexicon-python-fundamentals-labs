import sqlite3
import math


def connect_db():
    conn = sqlite3.connect("webshop.db")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def close_db(conn):
    conn.close()


def add_products(conn):

    try:
        name = input("Name: ").strip()
        if not name:
            raise ValueError("Name should not be empty")

        category = input("Category: ").strip()
        if not category:
            raise ValueError("Category should not be empty")

        price = float(input("Price: "))
        if price < 0 or not math.isfinite(price):
            raise ValueError("Price should not be negative or infinite")

        stock = int(input("Stock: "))
        if stock < 0 or not math.isfinite(stock):
            raise ValueError("Stock should not be negative or infinite")

        conn.execute("INSERT INTO products (name,category,price,stock) VALUES (?,?,?,?)",
                     (name, category, price, stock))
        conn.commit()
        print("Product Saved")
    except (ValueError, sqlite3.IntegrityError) as error:
        print(error)


def list_products(conn):
    cursor = conn.execute("SELECT product_id, name, price FROM products")
    for p_id, name, price in cursor.fetchall():
        print(f"{p_id:<20} {name:<20} {price} kr")


def search_customers(conn):
    try:
        city = input("Enter city:").strip()
        if not city:
            raise ValueError("City should not be empty")
        cursor = conn.execute(
            "SELECT first_name, last_name FROM customers WHERE city = ?", (city,))

        rows = cursor.fetchall()
        if not rows:
            print("Customer not found")
        for first_name, last_name in rows:
            print(f"{first_name} {last_name}")

    except ValueError as error:
        print(error)


def update_stock(conn):
    try:
        product_id = int(input("Enter product id: "))
        new_stock = int(input("Enter new stock: "))
        if new_stock < 0:
            raise ValueError("new stock cannot be negative")

        result = conn.execute("UPDATE products SET stock = ? WHERE product_id = ?",
                              (new_stock, product_id))
        conn.commit()

        if result.rowcount <= 0:
            raise ValueError("No records updated")

        print("Stock updated")

    except ValueError as error:
        print(error)


def order_receipt(conn):
    try:
        order_id = int(input("Enter order id: "))
        cursor = conn.execute("""SELECT oi.product_id, p.name, oi.unit_price,oi.quantity, oi.quantity * oi.unit_price AS line_total
                    FROM orders o
                    JOIN order_items oi ON o.order_id = oi.order_id
                    JOIN products p ON oi.product_id = p.product_id
                    WHERE o.order_id = ?""", (order_id,)
                              )
        for product_id, name, price_per_quantity, quantity, line_total in cursor.fetchall():
            print(
                f"{product_id:<10} {name:<20} {price_per_quantity} kr {quantity:^10} {line_total} kr")
    except ValueError as error:
        print(error)


def top3_best_Selling_products(conn):
    try:
        cursor = conn.execute("""
        SELECT p.name,sum(oi.quantity) as sold_units
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
        JOIN orders o ON oi.order_id = o.order_id
        WHERE o.status is not 'cancelled'
        GROUP BY p.product_id
        ORDER BY sold_units DESC
        LIMIT 3
        """)

        result = cursor.fetchall()
        if not result:
            raise ValueError("No results found")

        for product_name, sold_units in result:
            print(product_name, sold_units)

    except (sqlite3.OperationalError, sqlite3.IntegrityError,  sqlite3.ProgrammingError, ValueError) as error:
        print(error)


def main():
    conn = connect_db()

    while (True):
        print("1.List products 2.Add product 3.Search customers 4.Update stock 5.Order receipt 6.Top 3 best selling products 0.Quit ")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_products(conn)
        elif choice == "2":
            add_products(conn)
        elif choice == "3":
            search_customers(conn)
        elif choice == "4":
            update_stock(conn)
        elif choice == "5":
            order_receipt(conn)
        elif choice == '6':
            top3_best_Selling_products(conn)
        elif choice == "0":
            break
        else:
            print("Please enter correct choice: ")

    close_db(conn)


main()
