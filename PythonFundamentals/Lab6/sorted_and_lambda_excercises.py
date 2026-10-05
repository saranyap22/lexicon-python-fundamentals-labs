def sort_words(words):  # Preferred way
    """Return list of sorted words using len"""
    return sorted(words, key=len)


def sort_words_lambda(words):
    """Return list of sorted words using lambda"""
    return sorted(words, key=lambda word: len(word))  # lambda may not be necessary as we have builtin len function


words = ["I", "am", "very", "happy", "to", "attend", "python", "class"]
print(sort_words(words))
print("Sort with lambda: ", sort_words_lambda(words))


def sort_students(students, descending=False):
    """ Return a sorted list of dictionaries ascending """
    return sorted(students, key=lambda student: student["score"], reverse=descending)


students = [
    {"name": "Ram", "score": 45},
    {"name": "Anna", "score": 53},
    {"name": "Victor", "score": 12}
]

print("Sorted students in Ascending Order:", sort_students(students))
print("Sorted students in Descending Order:",
      sort_students(students, descending=True))


def sort_products(products):
    """Return a list of dictionary sorted by price of products"""
    return sorted(products, key=lambda product: product["price"])


products = [
    {"name": "laptop", "price": 7890, "category": "Electronics"},
    {"name": "Monitor", "price": 45, "category": "Electronics"},
    {"name": "Mouse", "price": 450, "category": "Electronics"}
]

print("Sorted Products by Price: ", sort_products(products))


def filter_by(name):
    """Return sort key from name"""
    return name["last_name"]

# Not preferred. filter_by method can be written short with lambda


def sort_names_without_lambda(names):
    """Return a list of dictionaries sorted by last_name without lambda"""
    return sorted(names, key=filter_by)


# Preferred. filter_by method replaced with lambda

def sort_names(names):
    """Return a list of dictionaries sorted by last_name with lambda"""
    return sorted(names, key=lambda name: name["last_name"].lower())


names = [
    {"first_name": "saranya", "last_name": "palanisamy"},
    {"first_name": "Allan", "last_name": "Gustav"},
    {"first_name": "Bob", "last_name": "Mandh"}
]


print("Sorted Names by last_name: ", sort_names(names))
