import requests

# title, price, description, image, category

new_product = {
    "title": "Test product",
    "price": 100.3,
    "description": "Poduct create from python REST api demo",
    "image": "",
    "category": "electronics"
}

# -------------------------------------------
# Request in JSON format

# response = requests.post("https://fakestoreapi.com/products", json=new_product)
# print(response.status_code)
# print(response.json())

# print(response.request.headers["Content-Type"])
# print(response.request.body)


# Request as data
# response = requests.post("https://fakestoreapi.com/products", data=new_product)
# print(response.status_code)
# print(response.json())

# print(response.request.headers["Content-Type"])
# print(response.request.body)


# ------------------------------------------------------
# PUT

updated_product = {
    "title": "Updated product",
    "price": 10.3,
    "description": "Poduct updated in demo",
    "image": "",
    "category": "electronics"
}

# response = requests.put(
#     "https://fakestoreapi.com/products/1", json=updated_product)

# print(response.status_code)
# print(response.json())


# --------------------------------------------------------
# PATCH

# response = requests.patch(
#     "https://fakestoreapi.com/products/1", json={"price": 48.8})

# print(response.status_code)
# print(response.json())


# ------------------------------------------------------------
# DELETE
# response = requests.delete("https://fakestoreapi.com/products/1")

# print(response.status_code)
# print(response.json())

# --------------------------------------------------------------

# CHECK if products updated or Deleted?

# response = requests.patch("https://fakestoreapi.com/products/1", {"price": 90})
# print(response.json())

# response = requests.delete("https://fakestoreapi.com/products/2")
# print(response.json())
