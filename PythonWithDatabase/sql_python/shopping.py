import sqlite3


def connect_db():
    conn = sqlite3.connect("webshop.db")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def close_db(conn):
    conn.close()


def add_products(conn):
    name = input("Name: ")
    category = input("Category: ")
    price = int(input("Price: "))
    stock = int(input("Stock: "))
    conn.execute("INSERT INTO products (name,category,price,stock) VALUES (?,?,?,?)",
                 (name, category, price, stock))
    conn.commit()
    print("Product Saved")


def list_products(conn):
    cursor = conn.execute("SELECT product_id, name, price FROM products")
    for p_id, name, price in cursor.fetchall():
        print(f"{p_id:<20} {name:<20} {price} kr")


def search_customers(conn):
    city = input("Enter city:")
    cursor = conn.execute(
        "SELECT first_name, last_name FROM customers WHERE city = ?", (city,))

    rows = cursor.fetchall()
    if not rows:
        print("Customer not found")
    for first_name, last_name in rows:
        print(f"{first_name} {last_name}")


def update_stock(conn):
    product_id = input("Enter product id: ")
    new_stock = int(input("Ebter new stock: "))

    conn.execute("UPDATE products SET stock = ? WHERE product_id = ?",
                 (new_stock, product_id))
    conn.commit()
    print("Stock updated")


def order_receipt(conn):
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


def main():
    conn = connect_db()

    while (True):
        print("1.List products 2.Add product 3.Search customers 4.Update stock 5.Order receipt 0.Quit ")
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
        elif choice == "0":
            break
        else:
            print("Please enter correct choice: ")

    close_db(conn)


main()
