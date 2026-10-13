from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# Basic methods
# Get all the collections(like tables in sql)
print(db.list_collection_names())

# get specific collection and count of documents (like no of rows in a table)
product = db.products.find_one()
print(product)
# pprint will print collection in multi line format
pprint(product)


# looping over the results
for name in db.list_collection_names():
    print(name, db[name].count_documents({}))

# find()
for customer in db.customers.find():
    print(customer["first_name"], list(customer.keys()))

# insert one

result = db.products.insert_one(
    {"name": "Gloves", "category": "Accessories", "price": 199, "stock": 20})
print(result.inserted_id)
pprint(db.products.find_one({"name": "Gloves"}), sort_dicts=False)

# delete
result = db.products.delete_one({"name": "Gloves"})
print(result.deleted_count)
# count
print(db.products.count_documents({}))

# Important Note
# Mongo DB changes commit immediately
