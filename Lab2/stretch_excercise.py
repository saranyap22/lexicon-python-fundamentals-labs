# challenge 1
list_one = ["user_one", "user_two", "user_three", "user_one"]
list_two = ["use_four", "user_five", "user_one", "user_two"]
unique_usernames = set(list_one) | set(list_two)
print(unique_usernames)

# challenge 2
courses = [
    {"name": "System developer Python", "teacher": "Anna", "students": ["Alen", "Bob", "Victor"],
     "topics": ["Fundamentals", "collection", "control flow"]},
    {"name": "System developer AI", "teacher": "Henrik", "students": ["Bob", "Vineeth"],
     "topics": ["Machine Learning", "Deep Learning", "Model Training"]}
]

# challenge 3
inventories = {
    "PRD-1": {"name": "computer", "price": 7000.0, "quantity_in_stock": 120},
    "PRD-2": {"name": "mouse", "price": 200.0, "quantity_in_stock": 20},
    "PRD-3": {"name": "speaker", "price": 1000.0, "quantity_in_stock": 10},
    "PRD-4": {"name": "monitor", "price": 70.0, "quantity_in_stock": 50},
    "PRD-5": {"name": "mobile", "price": 700.0, "quantity_in_stock": 150}
}

inventories["PRD-2"]["quantity_in_stock"] = 90
inventories["PRD-5"]["quantity_in_stock"] = 25
total_units = 0
total_value = 0.0
print("Current Inventory details: ")
for product, details in inventories.items():
    units = details["quantity_in_stock"]
    price = details["price"]
    prosuct_total_value = units * price

    total_units += units
    total_value += prosuct_total_value
    print(
        f"{product} {details["name"]} {units} {price}  {prosuct_total_value}")

# Challenge 4
# List vs Tuple Vs Set Vs Dictionary
# List: Ordered Collection of data can be accessed with index. Can be used when we want to handle duplicate elements and mutable elements
# Tuple: Ordered Collection of data can be accessed with index. Can be used when we want to handle duplicate elemets and Immutable elements
# Set : UnOrdered Collection of data with no duplicates. Can be used for to remove duplicates elements and set is Mutable but elements inside set are immutable
# Dictionary: Unordered Collection of data with no duplicates.Can be used to handle data in (Kay, value) structure, Keys are immutable and values are mutable.
