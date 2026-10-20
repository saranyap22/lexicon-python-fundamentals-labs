import requests
from api_client import get_json

BASE_URL = "https://fakestoreapi.com"


# def get_json(url, params=None, headers=None, timeout=5):
#     try:
#         response = requests.get(
#             url, params=params, headers=headers, timeout=timeout)
#         response.raise_for_status()
#         return response.json()
#     except requests.exceptions.Timeout:
#         print("The request took too long")
#     except requests.exceptions.ConnectionError:
#         print("Could not connect to the server")
#     except requests.exceptions.HTTPError as error:
#         print(f"The server said no: {error.response.status_code}")
#     except requests.exceptions.JSONDecodeError:
#         print("The answer was not JSON")
#     except requests.exceptions.RequestException as error:
#         print(f"Something else went wrong: {type(error).__name__}")
#     return None


# Excercise 1
# Sort the products by price
def retrieve_products():
    products = get_json(f"{BASE_URL}/products")
    if products is not None:
        sorted_products = sorted(
            products, key=lambda product: product["price"])
        for line_item, product in enumerate(sorted_products, 1):
            print(
                f"{line_item} {product["title"]:<100} {product["price"]} kr")


# Look at the categories
def retrieve_categories():
    categories = get_json(f"{BASE_URL}/products/categories")
    if categories is not None:
        for category in categories:
            print(category)

        retrieve_category_statistics(categories)


def retrieve_category_statistics(categories):
    while (True):
        input_category = input(
            "Enter category from the list to view staticstics or q to quit: ").strip().lower()

        if input_category == "q":
            break

        if input_category not in categories:
            print(f"{input_category} is not a valid category. Try again")
            continue

        products = get_json(
            f"{BASE_URL}/products/category/{input_category}")

        if not products:
            print(f"products empty for category {input_category}")
            continue

        cheapest_product = min(
            products, key=lambda product: product["price"])
        print(
            f"""Total no of products in {input_category} is {len(products)}.
        The cheapest product is {cheapest_product["title"]:<100} {cheapest_product["price"]} kr""")


def create_product():
    new_product = {
        "title": "Testing adding new product",
        "price": "89",
        "description": "This is a product created for testing create endpoint",
        "image": "https://champion.se/thumb/916/2560x0/CHBR220_1.webp",
        "category": "electronics"
    }
    try:
        response = requests.post(f"{BASE_URL}/products",
                                 json=new_product, timeout=1)
        response.raise_for_status()

        product = response.json()
        print(product["title"], product["description"],
              product["category"], product["price"])

    except


def update_product():
    update_product = {"price": 900}

    response = requests.patch(
        f"{BASE_URL}/products/1", json=update_product, timeout=1)
    response.raise_for_status()

    product = response.json()
    print(product["price"])


def main():
    retrieve_products()
    retrieve_categories()
    create_product()
    update_product()


main()
