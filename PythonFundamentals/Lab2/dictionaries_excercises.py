"""Module to explore Dictionaries"""

computer_info = {"brand": "DELL", "model": "ABC",
                 "RAM": "8GB", "storage": "120GB", "price": 120000}
print(f"Brand: {computer_info["brand"]}")
print(f"Model: {computer_info["model"]}")
print(f"RAM: {computer_info["RAM"]}")
print(f"Storage: {computer_info["storage"]}")
print(f"price: {computer_info["price"]}")

computer_info["price"] = 100000
print(f"Updated price: {computer_info}")
computer_info["operating_system"] = "Windows"
print(f"Added operating system: {computer_info}")
computer_info.pop("model")  # Raise KeyError if unknow key was tried to pop
print(f"Removed model: {computer_info}")
# Pop specific element . If not exist return default value given
price_popped = computer_info.pop("pric", 1000)
print(f"price popped: {price_popped}")
brand_value = computer_info.popitem()  # Remove last added item and return
print(f"Removed brand: {computer_info}")

# Getting all Keys and Values separately as list
print(f"Keys: {computer_info.keys()}")
print(f"Keys: {computer_info.values()}")

# Dictionary Mapping
courses = {"Java": 5, "Python": 10, "C#": 16}
print(f"Total hours: {sum(courses.values())}")
