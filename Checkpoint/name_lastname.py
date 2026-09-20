# ==================================================
# TASK 1
# ==================================================

products = [
    {"name": "Laptop", "price": 12000, "stock": 4},
    {"name": "Mouse", "price": 350, "stock": 0},
    {"name": "Keyboard", "price": 800, "stock": 6},
    {"name": "Monitor", "price": 3200, "stock": 3},
    {"name": "Headset", "price": 950, "stock": 0},
    {"name": "Webcam", "price": 1100, "stock": 5}
]

# 1. Loop through the products.
# 2. Print the name of every product that is in stock.
# 3. Calculate the total value of all products in stock.
#    The value of a product is price * stock.
# 4. Print the total value.
# 5. Keep track of which in-stock product has the highest price
#    without using max(), and print its name.


# Write your solution below:

product_in_stock = [product for product in products if product["stock"] > 0]

total = 0
highest_price = products[0]["price"]

print(f"{"Product name":<15} {"Total value":>15}")

for product in product_in_stock:

    product_value = product["price"] * product["stock"]
    print(f"{product["name"]:<15}: {product_value:<15}")
    total += product_value

    if product["price"] > highest_price:
        highest_price = product["price"]
print(f"Total value of in stock products: {total}")
print(f"Highest priced Product: {highest_price}")

# ==================================================
# TASK 2
# ==================================================

scores = [78, 92, 55, 81, 67, 95, 73]

# Create a function called calculate_average that:
# - receives a list of scores
# - calculates and returns the average score
#
# Create another function called create_result that:
# - receives a list of scores
# - uses calculate_average()
# - returns "PASS" if the average is 70 or higher
# - otherwise returns "FAIL"
#
# Call create_result() using the scores above.
# Print both the average score and the final result.


# Write your solution below:
def calculate_average(scores):
    total_score = 0
    for score in scores:
        total_score += score
    return total_score / len(scores)


def create_result(scores):
    if calculate_average(scores) >= 70:
        return "PASS"
    return "FAIL"


print(
    f"Average score: {calculate_average(scores):.2f}, Result: {create_result(scores)}")

# ==================================================
# TASK 3
# ==================================================


product_prices = [250, 400, 150, 700]

order_settings = {
    "discount": 10,
    "shipping": 49,
    "priority": True
}

# Create a function called calculate_order that:
# - receives a customer name as a normal parameter
# - receives any number of product prices using *args
# - receives optional settings using **kwargs
# - calculates the subtotal of all product prices
# - applies the discount percentage if "discount" exists
# - adds shipping if "shipping" exists
# - returns a dictionary containing:
#       customer
#       subtotal
#       final_total
#       settings
#
# Call the function using:
# - customer name "Anna"
# - the values from product_prices using unpacking
# - the values from order_settings using dictionary unpacking
#
# Print the returned dictionary.


# Write your solution below:
def calculate_order(customer, *prices, **optional_settings):
    subtotal = 0
    final_total = 0
    if prices:
        for price in prices:
            subtotal += price

    if optional_settings:
        for setting, value in optional_settings.items():
            if setting == "discount":
                final_total = subtotal - subtotal * (value / 100)

            if setting == "shipping":
                final_total += value

    return {"customer": customer, "subtotal": subtotal, "final_total": final_total,
            "settings": optional_settings}


print(calculate_order("Anna", *product_prices, **order_settings))
# ==================================================
# TASK 4
# ==================================================


players = [
    {"name": "  anna", "score": 85, "active": True},
    {"name": "DAVID ", "score": 72, "active": False},
    {"name": " sara ", "score": 94, "active": True},
    {"name": "LEO", "score": 67, "active": True},
    {"name": " emma", "score": 88, "active": True},
    {"name": "OSCAR ", "score": 76, "active": False}
]

# 1. Create a new list containing normalized player names.
#    Remove unnecessary whitespace and use consistent capitalization.
#    Use a list comprehension.
#
# 2. Create a new list containing only the active players
#    with a score of 80 or higher.
#    Use a list comprehension.
#
# 3. Sort the original players by score from highest to lowest.
#    Use sorted() with a lambda.
#
# 4. Print the ranking in the following format:
#
#    1. Sara - 94
#    2. Emma - 88
#    ...
#
#    Generate the ranking numbers using enumerate().
#
# 5. Create a separate list containing the player names and
#    another list containing their scores.
#    Combine them using zip() and print each name together
#    with its score.


# Write your solution below:
def normalise(players):
    return [

        {**player, "name": player["name"].strip().capitalize()}
        for player in players
    ]


def filter_by_score(players, score):
    return [
        player for player in players
        if player["active"] and player["score"] >= score
    ]


def sorted_players(players):
    return sorted(players, key=lambda player: player["score"], reverse=True)


def print_rank(players):
    for rank, player in enumerate(players, start=1):
        print(
            f"{rank:<5} {player["name"]: <7} {"-": ^5} {player["score"]: > 5}")


def zip_and_print(players):
    names = []
    scores = []
    for player in players:
        names.append(player["name"])
        scores.append(player["score"])
    names_scores = dict(zip(names, scores))

    for position, (name, score) in enumerate(names_scores.items(), start=1):
        print(f"{position:<3} {name:<5} {"-":^3} {score:>5}")


normalised_players = normalise(players)
print("Normalised Players:", normalised_players)

filtered_players = filter_by_score(normalised_players, 80)
print("Players with active status and score above 80:", filtered_players)

sorted_players = sorted_players(normalised_players)
print_rank(sorted_players)

zip_and_print(sorted_players)
