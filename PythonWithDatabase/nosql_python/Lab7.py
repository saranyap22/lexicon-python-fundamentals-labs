from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# Exercise 1
# Show the name and price of all products that cost more than 1000 kr.
products = db.products.find({"price": {"$gt": 1000}}, {
                            "name": 1, "price": 1, "_id": 0})

for product in products:
    print(product["name"], product["price"])

# Note: Ex: print(product["name"], product["price"], product["_id"], product["stock"])
# If no "_id": 0 in projection product["_id"] will be coming by defaut even no inluded
# product["stock"] will cause keyerror since it is not included in projection

# --------------------------------------------------------

# Exercise 2
# Show all orders that are not delivered. Use $ne. Print the _id and status.

orders = db.orders.find({"status": {"$ne": "delivered"}})
for order in orders:
    print(order["_id"], order["status"], order["order_date"])

# ----------------------------------------------------------

# Exercise 3
# Show customers who live in Stockholm or Malmö, using $in.

# Solution 1: more conditions with $or
customers = db.customers.find(
    {"$or": [{"city": "Stockholm"}, {"city": "Malmö"}]})

for customer in customers:
    print(customer["first_name"], customer["last_name"])

# Solution 2: efficient one with $in
customers = db.customers.find(
    {"city": {"$in": ["Stockholm", "Malmö"]}})

for customer in customers:
    print(customer["first_name"], customer["last_name"])

# ------------------------------------------------------

# Exercise 4
# Which products are white? Use dot notation.

products = db.products.find({"details.color": "white"}, {"name": 1})

for product in products:
    print(product["_id"], product["name"])

# -------------------------------------------------------

# Exercise 5
# Which products have the tag sport? Show only name and tags, without _id.

products = db.products.find(
    {"tags": "sport"}, {"name": 1, "tags": 1, "_id": 0})

for product in products:
    print(product["name"], product["tags"])
# Note
# For checking in array in document directly giing value checks in the array {"tags": "sport"} works like {"tags": {"$in": "sport"}}
# For checking product having all the tags sport and winter. {"tags": {"$all"}: ["sport","winter"]}

# -----------------------------------------------

# Exercise 6
# Show the 5 cheapest products, cheapest first. Only name and price

products = db.products.find(
    {}, {"name": 1, "price": 1, "_id": 0}).sort("price", 1).limit(5)

for product in products:
    print(product["name"], product["price"])

# -----------------------------------------------

# Exercise 7
# Which orders contain product 2 (T-shirt White)? Hint: dot notation works on arrays of objects too: "items.product_id"

orders = db.orders.find({"items.product_id": 2}, {"items": 1})
for order in orders:
    print(order["_id"], order["items"])

# ------------------------------------------------

# Exercise 8
# Raise the price of all Accessories by 20 kr with $inc. Then print the Accessories with their new prices.

products_count = db.products.count_documents({"category": "Accessories"})
print(products_count)

result = db.products.update_many({"category": "Accessories"}, {
                                 "$inc": {"price": 20}})
print(result.matched_count, result.modified_count)
# ----------------------------------------
