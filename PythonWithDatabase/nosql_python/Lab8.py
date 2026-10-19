from pymongo import MongoClient
from pymongo.errors import WriteError, BulkWriteError

client = MongoClient("mongodb://localhost:27017")
db = client["webshop"]


# Example 1
# Design: a library app shows a book page with the book's title, author and all its reviews. Many
# members borrow the same book. Would you embed or reference the reviews? The members?
# Explain in two sentences.

# Answer:
#  I would use reference for review in book. Because the review list can grow huge.
#  I would choose embed members(list of (_id,borrow_date,return_date) in Book but will have Member collection as a standalone data needed.


# ------------------------------------------------------------------

# Exercise 2
# Our orders copy the product name into each item. Give one advantage and one disadvantage of that copy.

# Answer
# Advantage: Application read the necessary data from a single place. No need to reference data
# Disadvantage: If any change in product name then it has to be updated in many rows acccrows many orders

# ------------------------------------------------------------------

# Excercise 3
# Create a collection newsletter_signups with validation: email is required and must be a string, and
# source can only be "web" or "store" (look up enum). Insert one valid and one invalid document.

# db.create_collection("newsletter_signups", validator={
#     "$jsonSchema": {
#         "required": ["email"],
#         "properties": {
#             "_id": {"bsonType": "int"},
#             "email": {"bsonType": "string"},
#             "source": {"bsonType": "string",
#                        "enum": ["web", "store"]
#                        }
#         }
#     }
# })

try:
    db.newsletter_signups.insert_one(
        {"_id": 1, "email": "sara@gmail.com", "source": "web"})

    db.newsletter_signups.insert_many(
        [{"_id": 3, "email": "hud@gmail.com", "source": "store"}])

    print("Inserted")
except (WriteError, BulkWriteError) as error:
    print(error)


# Exercise 4
# How many customers live in each city? Use $group. Biggest city first.
