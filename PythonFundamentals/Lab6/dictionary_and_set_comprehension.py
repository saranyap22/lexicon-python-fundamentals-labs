def num_square(range_of_numbers):
    """Returns a dictionary mapping each number to its square"""
    return {
        num: num ** 2
        for num in range_of_numbers
    }


print("Squares", num_square(range(1, 11)))


def word_length(words):
    """Return a dictinary mapping each word to its length"""
    return {
        word: len(word) for word in words
    }


words = ["Hello", "launguage", "my", "name", "sara"]
print("Word length:", word_length(words))


def normalise_name(names):
    """Return a set with lowercase normalised value"""
    return {
        name.lower() for name in names
    }


names = ["saranya", "Barbe", "Tintu", "saranya"]
print(normalise_name(names))


def filter_products(produts, price_threshold):
    """Return a dictionary of products whose price is within a threshold"""
    return {
        product: price
        for product, price in produts.items()
        if price < price_threshold
    }


products = {"Laptop": 12000,
            "pendrive": 120,
            "mouse": 100}
print("Filtered Products by Price", filter_products(products, 110))


# Not an ideal way since we need to iterate twice
def create_student_results(students):
    """ Return a dictionary mapping of student names to PASS/FAIL"""
    passed = {
        student["name"]: "PASS"
        for student in students
        if student["score"] >= 60
    }
    failed = {
        student["name"]: "FAIL"
        for student in students
        if student["score"] < 60
    }
    return {**passed, **failed}


# Preferred solution. Only one iteration through the list
def create_student_result(students):
    """ Return a dictionary mapping of student names to PASS/FAIL"""
    results = {}
    for student in students:
        if student["score"] >= 60:
            results[student["name"]] = "PASS"
        else:
            results[student["name"]] = "FAIL"
    return results


students = [
    {"name": "Allan", "score": 78},
    {"name": "Bob", "score": 54},
    {"name": "Grace", "score": 100}
]
print("Student Results", create_student_results(students))
print("Student Result", create_student_result(students))
