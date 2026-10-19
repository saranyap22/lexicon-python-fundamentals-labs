import requests
# response = requests.get("https://fakestoreapi.com/products")

# print(response)

# # print(response[0]) - wrong

# # Response processing
# # 1.status code, 2.headers 3. body

# print(response.status_code)
# print(response.headers["Content-Type"])
# print(response.text[:200])  # Getting response as Text. first 200 letters

# # python can't fetch like text[0]['title]. we need to convert tp json
# data = response.json()  # Type of data is 'list'
# print(type(data))
# print(len(data))  # len of list
# print(data[0])  # first item in the list

# for product in data[:5]:
#     print(f"{product["id"]}, {product["title"]:<20}, {product["price"]} kr")

# ---------------------------------------
# Getting specific product

# response = requests.get("https://fakestoreapi.com/products/15")
# product = response.json()
# print(product)

# print(product["rating"])
# print(product["rating"]["rate"])

# print(product["title"], product["rating"]["rate"])


# --------------------------------------
# QUERY PARAMETERS

# response = requests.get("https://fakestoreapi.com/products?limit=5")
# print(len(response.json()))

# response = requests.get("https://fakestoreapi.com/products",
#                         params={"limit": 5, "sort": "desc"})
# print(len(response.json()))
# print(len(response.json()))
# print(response.url)
# print([product["id"] for product in response.json()])

# response = requests.get("https://fakestoreapi.com/products/categories")
# print(response.json())

# -----------------------------------

# response = requests.get("https://fakestoreapi.com/products/",
#                         headers={"accept": "application/json"})

# print(response.status_code)

# ------------------------------------------------------------------
# PART2
# ------------------------------------------------------------------


# response = requests.get("https://api.github.com/users/octocat")
# print(response.status_code)
# print(response.json())
# print(response.json()["name"])


# response = requests.get("https://api.github.com/users/user-not-exist-123")
# print(response.status_code)
# print(response.json())
# print(response.json()["name"])

# response = requests.get("https://api.github.com/users/user-not-exist-123")

# if response.status_code == 200:
#     print(response.json()["name"])
# elif response.status_code == 404:
#     print("The user does not exist")
# else:
#     print(f"Something went wrong: {response.status_code}")


# -------------------------------------------------

# RAISE for status ( raise_for_status())
# try:
#     response = requests.get("https://api.github.com/users/user-not-exist-123")
#     response.raise_for_status()
#     print(response.json()["name"])
# except requests.exceptions.HTTPError as error:
#     print(f"The server said no: {error.response.status_code}")


# -------------------------------------------------
# TIMEOUT

# response = requests.get("https://api.github.com/users/oactocat", timeout=0.001)
# If no timeout set application wait forever
# Always  set timeout

# ---------------------------------------------------

# CONNECTION ERROR
# respose = requests.get("https://this-domain-doest-not-exists.com")


# MissingSchema: INVALID URL
# response = requests.get("fakestoreapi.com/products")


# JSONDecoderError
# response = requests.get("https://example.com")
# print(response.status_code)
# print(response.json())

# -------------------------------------------------------

def get_json(url, params=None, headers=None, timeout=5):
    try:
        response = requests.get(
            url, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("The request took too long")
    except requests.exceptions.ConnectionError:
        print("Could not connect to the server")
    except requests.exceptions.HTTPError as error:
        print(f"The server said no: {error.response.status_code}")
    except requests.exceptions.JSONDecodeError:
        print("The answer was not JSON")
    except requests.exceptions.RequestException as error:
        print(f"Something else went wrong: {type(error).__name__}")
    return None


# calling with common function get_json()
get_json("https://api.github.com/users/octocat")['name']

# invalid resource # HttpError
get_json("https://api.github.com/users/user-not-exist-123")

# timeout
get_json("https://api.github.com/users/oactocat", timeout=0.001)

# Connection Error : ConnectionError
get_json("https://this-domain-doest-not-exists.com")

# not a json response # JSONDecoderError
get_json("https://example.com")

# Invalid url # RequestExceptions
get_json("fakestoreapi.com/products")

# proper way of calling and accessing data
data = get_json("https://api.github.com/users/octocat")
if data is not None:
    print(data["name"])
