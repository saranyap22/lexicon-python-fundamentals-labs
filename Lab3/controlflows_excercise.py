""" Module to explore control flows"""
# number categories
numbers = [1, -12, 3, 18, 4, 3, 5, 0, 7]
for number in numbers:
    if number > 0:
        print("Positive number")
    elif number < 0:
        print("Negative number")
    elif number == 0:
        print("Number is Zero")

# Age grouping
input_age = input("Enter you age: ")
age = int(input_age)
if age <= 2:
    print("Baby")
elif age <= 5:
    print("Toddler")
elif age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
else:
    print("Adult")

# Login check
username = input("Enter username: ")
password = input("Enter the password: ")
if "saranya" == username and "TestPwd" == password:
    print("Login is successful")
else:
    print("Login not successful")

# Shipping rule


def find_membership_status(membership_input):
    if membership_input == "yes":
        is_member = True
    elif membership_input == "no":
        is_member = False
    else:
        is_member = False
    return is_member


total = float(input("Enter total price: "))
have_membership = input("Is member? : yes / no ")

if total >= 2000 and find_membership_status(have_membership):
    print("Free Shipping")
else:
    print("Shipping fee 45 kr")

# Comparison operators
numbers = [1, -12, 3, 18, 4, 3, 5, 0, 7]
# numer > 0 : positive number
# number < 0 : negative number
# number == 0 : zero
# number != 0 : non Zero number
# number >= 10 : number equals or more than 10
# number <= 10 : number lesss than or equal to 10

# Truthy Falsy and Membership examples
inputs = ["", "Hi", " ", 0, 12, [], [1, 5]]
for input_text in inputs:
    if input_text:
        print(input_text, ": True")
    else:
        print(input_text, ": False")

# Membership check
input_launguage = input("Enter your launguage:")

launguages = {"Python", "Java", "C#", "Scala", "Go"}
if input_launguage in launguages:
    print("Your requested launguage supported")
else:
    print("Your requested launguage not supported")

# Reject already existing usernames
input_data = input("Enter the user name to create: ")
existing_user_names = {"saranya", "saranya2", "saranyasamy2", "test"}
if input_data in existing_user_names:
    print("Username already exist!")
else:
    print("User name accepted")

# Non Readable condition
existing_user_names = {"saranya", "saranya2", "saranyasamy2", "test"}
if len(existing_user_names) == 0:  # readable way: if not existing_user_names:
    print("Not Empty")

# if is_member == True:   # readable way: if is_member
