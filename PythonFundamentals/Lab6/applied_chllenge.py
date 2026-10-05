"""Module contains fuctions for data cleanup excercise"""


def clean_products(products):
    """ Return a list of products with normalised name and category"""
    for product in products:
        product["name"] = product.get("name", None).strip().lower()
        product["category"] = product.get("category", None).strip().lower()
    return products


def get_instock_products(products):
    """Return list of products with stocks atleast 1"""
    return [product for product in products if product["stock"] >= 1]


def get_unique_categories(products):
    """Return set of categories"""
    return {product["category"] for product in products}


def create_product_inventory(products):
    """Return a dictionary by mapping product name and inventory value"""
    return {
        product["name"]: product["stock"] * product["price"]
        for product in products
    }


def sort_products(products):
    """Return list of sorted product in reverse"""
    return sorted(products, key=lambda product: product["price"] * product["stock"], reverse=True)


def print_report(products, inventory):
    """Print a list of ranked product"""
    print(f"{"Rank":<5} {"Product":<10} {"Price": <10} {"category":<15} {"stock":<10} {"Inventory Value":<10} ")
    for position, product in enumerate(products, start=1):
        print(
            f"{position:<5} {product["name"]:<10} {product["price"]:<10} {product["category"]:<15} {product["stock"]:<10} {inventory[product["name"]]:<10}")


products = [
    {"name": " pen ", "price": 4.66, "category": " Stationary", "stock": 220},
    {"name": " Eraser", "price": 2, "category": "Stationary ", "stock": 15},
    {"name": " mouse ", "price": 230.6, "category": "  electronics ", "stock": 50},
    {"name": " Computer ", "price": 6000, "category": "Electronics", "stock": 598},
    {"name": " t-shitrt  ", "price": 200, "category": "clOthing", "stock": 140},
    {"name": " pendrive   ", "price": 120,
        "category": "electronics", "stock": 60},
    {"name": " unmberlla ", "price": 80, "category": "Accessaries", "stock": 900},
    {"name": " pant ", "price": 111, "category": "clothing   ", "stock": 5},
    {"name": " Shoes ", "price": 349, "category": "FootWear", "stock": 6000},
    {"name": " sharpner", "price": 4, "category": "Stationary", "stock": 0},
    {"name": "jackET ", "price": 700, "category": " clothing", "stock": 150},
    {"name": "  note book ", "price": 4, "category": "Stationary", "stock": 78}
]


normalised_products = clean_products(products)
in_stock_products = get_instock_products(normalised_products)
unique_categories = get_unique_categories(in_stock_products)
product_inventory = create_product_inventory(in_stock_products)
sorted_products = sort_products(in_stock_products)
print_report(sorted_products, product_inventory)
