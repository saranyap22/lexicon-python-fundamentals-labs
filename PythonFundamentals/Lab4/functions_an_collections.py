def calculate_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(f"Total: {calculate_total([5, 7, 2, 9, 10, 6, 7])}")


def count_even(numbers):
    total_even_number = 0
    for number in numbers:
        if (number % 2 == 0):
            total_even_number += 1
    return total_even_number


print(f"Total even Numbers: {count_even([5, 7, 2, 9, 10, 6, 7])}")


def get_long_words(words, minimum_length):
    long_words = []
    for word in words:
        if len(word) >= minimum_length:
            long_words.append(word)
    return long_words


def get_long_words_comprehension(words, minimum_length):
    """ Function to get long words using list comprehension"""
    return [word for word in words if len(word) >= minimum_length]


words = ["ice", "bed", "unberlla", "sofa", "tv", "computer_monitor"]
print(get_long_words(words, 4))
print(get_long_words(words, 7))
print(get_long_words(words, 9))
print(get_long_words_comprehension(words, 1))


def find_student(students, name):
    for student in students:
        if (student["name"] == name):
            return student


students = [
    {"name": "Allan", "city": "solna", "course": "Python"},
    {"name": "Bob", "city": "Stockholm", "course": "Python"},
    {"name": "Allan", "city": "Sollentuna", "course": "Python"}
]
print(find_student(students, "Reka"))
print(find_student(students, "Allan"))


def average_score(students):
    total_score = 0
    for student in students:
        total_score += student.get("score", 0)
    return total_score / len(students)


students = [
    {"name": "Allan", "course": "Python", "score": 80},
    {"name": "Bob", "course": "Python", "score": 30},
    {"name": "Allan", "course": "Python", "score": 20}
]

print(average_score(students))
# print(average_score([])) ZeroDivisionError
# print(average_score(students=[])) ZeroDivisionError


def get_active_users(users):
    active_users = []
    for user in users:
        if user["active"]:
            active_users.append(user)
    return active_users


def get_active_users_with_comprehension(users):
    return [user for user in users if user["active"]]


users = [
    {"name": "Allan", "city": "solna", "active": True},
    {"name": "Bob", "city": "Stockholm", "active": False},
    {"name": "Allan", "city": "Sollentuna", "active": False}
]
print(get_active_users(users))
print("Active Users with comprehension",
      get_active_users_with_comprehension(users))
