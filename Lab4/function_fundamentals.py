""" Module contains fuction excercises"""


def greet(name="Guest"):
    print(f"Hi {name}, Wecome to Lexicon Python session")


def show_course_name(name="Programming Fundamentals"):
    print(f"This course name is: {name}")


def print_separator(char="*", length=50):
    print(char * length)


def introduce(name, city):
    print(f"I am {name} from {city}")


greet()
greet("Saranya")
show_course_name()
show_course_name("Python")
print_separator()
print_separator("-")
print_separator(90)  # 90 will be assigned to char and 90 * 50 = 4500
print_separator(length=90)  # 90 will be passed as argument length
print_separator("&", 200)
introduce("saranya", "solna")


def add(a, b):  # In function definition the values received is called paramaters
    return a + b


# type hint helps to know the expected type but it doesnot enforce for it
def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return round(a / b)


print(add(7, 2))  # In function call the values passed is called arguments
print(add("7", "2"))  # This results as 72 since arguments considered as str
print(subtract(7, 2))
# print(subtract("7", "2"))  # This results in TypeError as argumets are str
print(multiply(7, 2))
print(divide(2, 2))


# Using resuts of function in another function

def calculate_area(width, height):
    return width * height


def calculate_cost(area, amount=200):
    return area * amount


print(calculate_cost(calculate_area(23, 45)))
print(calculate_cost(calculate_area(23, 45), 100))
