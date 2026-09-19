numbers = [1, 3, 57, 8]
doubled_numbers = []
for num in numbers:
    doubled_numbers.append(num * 2)

print(doubled_numbers)

# List comprehension

doubled_numbers = [num*2 for num in numbers]
print(doubled_numbers)

# square of number
numbers = [1, 2, 3, 4, 5]
squares = [num**2 for num in numbers]
print(squares)

names = ["ada", "grace", "saranya", "allan"]
upper_names = [name.upper() for name in names]
print(upper_names)

# even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print("Without using comprehenseion", even_numbers)

# with List comprehension
even_numbers = [num for num in numbers if num % 2 == 0]
print("Wit comprehenseion", even_numbers)

names = ["Ada", "Bob", "Alexandra", "Grace"]
filtered_names = [name for name in names if len(name) >= 5]
print(filtered_names)


# Dictionary comprehension

# without dict comprehension
numbers = [1, 2, 3, 4, 5]
squares = {}
for num in numbers:
    squares[num] = num ** 2
print("squares without dictionary comprehension", squares)

# with Dictionary comprehension
squares = {num: num**2 for num in numbers}
print("With list comprehension: ", squares)

# From dictionary to another dictionary using dict comprehension
prices = {
    "apple": 10,
    "banana": 20,
    "mango": 100
}

doubled_prices = {product: price*2 for product, price in prices.items()}

print("With Dictionary comprehension", doubled_prices)


# dict comprehension with better readability
scores = {
    "Anna": 60,
    "Bob": 30,
    "Venkat": 90,
    "Victor": 85
}

passed = {
    person: score
    for person, score in scores.items()
    if score >= 60
}

print("Passed:", passed)


# Set comprehension
launguages = {"Python", "Java", "C#", "Java", "Scala"}

launguages_len = {launguage for launguage in launguages if len(launguage) > 3}
print(launguages_len)


# Zip
names = ["Anna", "Bob", "Charlie"]
scores = [45, 67, 23]
name_score = {}

for name, score in zip(names, scores):
    name_score[name] = score
print(name_score)

# tuple unpacking
pairs = list(zip(names, scores))
print(pairs)


names = ["Anna", "Bob", "Charlie"]
scores = [45, 67, 23]
cities = ["malmo", "stockholm", "solna"]

for name, score, city in zip(names, scores, cities):
    print(name, score, city)

print(list(zip(names, scores, cities)))


# Zip with short number of entries zip stop at least no of positions
names = ["Anna", "Bob", "Charlie", "Mohana"]
scores = [45, 67, 23]
cities = ["malmo", "stockholm", "solna", "Goteborg"]
names_dict = {}


for name, score, city in zip(names, scores, cities):
    print(name, score, city)
    names_dict[name] = {"score": score, "city": city}
print(names_dict)

# Unpacking list, tuples
coordinates = (10, 20)
x, y = coordinates
print(x, y)

names = ["Allan", "Bob", "Grace"]
first, second, third = names
print(first, second, third)

numbers = [10, 20, 30, 44]
first, *rest = numbers
print("First:", first)
print("Rest:", rest)

first, *middle, last = numbers
print("First:", first)
print("Middle:", middle)
print("last:", last)

# Unpacking with skip intension
person = ("Ada", 34, "London")
name, _, place = person
print(name)
print(_)
print(place)

# Combine
first = [1, 2, 3, 4]
second = [6, 7, 2]
combined = [*first, *second]
print(combined)

# combine with dictionary
defaults = {
    "launguage": "English",
    "theme": "light"
}

user_settings = {
    "launguage": "Swedish",
    "notification": True
}

# later(user_settings) replaces override entries
settings = {**defaults, **user_settings}
print(settings)

# later (defaults) replaces override entries
settings = {**user_settings, **defaults}
print(settings)


# Lambda (lambda parameters colon expression)
# double = lambda number: number *2


# Sorting with different styles

names = ["Alexandra", "Bob", "Jessica", "Mena"]
print(sorted(names))

# Sort with length of name


def get_length(person_name):
    return len(person_name)


print(sorted(names, key=get_length))

# sort with length of name using lambda

sorted_names = sorted(names, key=lambda name: len(name))
print(sorted_names)


# Map
numbers = [1, 2, 3, 4, 5, 8, 6, 8]
# map returns as iterator object
doubled = map(lambda number: number * 2, numbers)

print("Map and list:", list(doubled))

# Once iterated then we cant reduce double object
print("Map and Set:", set(doubled))

# Filter

even_numbers = filter(lambda number: number % 2 == 0, numbers)
print("Filter and list:", list(even_numbers))
print("Filter and set:", set(even_numbers))  # This set will be empty


# Correct way
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print("Filter and list:", even_numbers)
print("Filter and set:", set(even_numbers))  # This set will be empty
