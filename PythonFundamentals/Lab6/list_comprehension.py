# square of numbers
def square_with_loop(range):
    squares = []
    for number in range:
        squares.append(number**2)
    return squares


def square_with_comprehension(range_of_numbers):
    return [
        number ** 2
        for number in range_of_numbers
    ]


print("Square using loop:", square_with_loop(range(1, 21)))
print("Square using list comprehension:", range(1, 21))


def get_even_numbers(range_of_numbers):
    """Function to return list of even numbers"""
    return [
        num
        for num in range_of_numbers
        if num % 2 == 0]


print("Even Numbers:", get_even_numbers(range(1, 101)))


def transform_names(names):
    """Function to strip and title case names"""
    return [
        name.strip().title()
        for name in names
    ]


names = ["alex ", " georgia", "saranya", "Zeron"]
print("Transaformed Names", transform_names(names))


def passed_sores(scores):
    """Function to find passed score from list of scores"""
    return [
        score for score in scores
        if score >= 60
    ]


scores = [34, 67, 25, 90, 32, 56]
print("Passed Scores:", passed_sores(scores))


def create_label(scores):
    """Function to label score PASS / FAIL"""
    results = {}
    passed = []
    failed = []
    for score in scores:
        if score >= 60:
            passed.append(score)
        else:
            failed.append(score)
    results["PASS"] = passed
    results["FAIL"] = failed

    return results  # combine using unpacking


scores = [34, 67, 25, 90, 32, 56]
print("PASS/FAIL", create_label(scores))
