# for Loop
names = ["saranya", "Anna", "Josep", "Victor", "Lessi"]

for index, name in enumerate(names):  # By defaut index start from 0
    print(f"Hi {name} at position {index}")

for index, name in enumerate(names, start=1):  # start define the starting index
    print(f"Hi {name} at position {index}")


# Find even numbers

for number in range(1, 50):
    print(f"Number: {number} {"even" if number % 2 == 0 else "odd"}")

# Sum of List manual
numbers = [3, 5, 78, 83, 24, 24]
sum = 0
for number in numbers:
    sum += number
print(f"Sum is: {sum}", )


# Find largest number
numbers = [3, 5, 78, 83, 24, 24]
largest_number = numbers[0]
for index, number in enumerate(numbers):
    if number > largest_number:
        largest_number = number
print(f"Largest Number is: {largest_number} ")

# Looping through string
names = ["saranya", "Anna", "JosepVijay", "Victor", "VegLessi"]
count = 0
for name in names:
    if len(name) > 5:
        count += 1
print(f"Number of words with more than five characters: {count}")

# loop with conditions
scores = [10, 50, 30, 80, 45, 90]
passed = 0
failed = 0
for score in scores:
    if score >= 70:
        passed += 1
    else:
        failed += 1
print(f"Passed: {passed} and Failed: {failed}")

# Looping in Dictionaries
personal_info = {
    "name": "saranya", "age": 35, "city": "Solna", "pin": 17169
}
for key in personal_info:  # By default iterating dictionary loos over keys ex: personal_info.keys()
    print(key)

for value in personal_info.values():
    print(value)

for key, value in personal_info.items():
    print(f"{key} : {value}")

# Nested Loop excercises
# by default step is 1, for 1.. 10 -> range(1,10), for 1,3,5..9 range(1,10,2)
for num in range(10, 2, -1):
    print(f"Number: {num}")

# Multiplication table
user_input = input("Enter the number to generate Multiplication table: ")
for num in range(1, 21):
    print(f"{num} * {user_input} = {num * int(user_input)}")

playlist = ["Shape of you", "Blinding Lights", "The magic moon"]
for index, song in enumerate(playlist, 1):
    print(f"{index} : {song}")

# Nested loops
for x in range(1, 4):
    for y in range(1, 4):
        print(f"({x},{y})")

# 5 * 5 Text grid

for x in range(1, 6):
    for y in range(1, 6):
        print("*", end="   ")
    print()


# while loop

count = 10
while count >= 0:
    print(count)
    count -= 1

# While loop for password check
while True:
    input_password = input("Enter your password:")
    if ("test" == input_password):
        print("Successful")
        break

# while loop until finding a string (create menu until quit)

while (True):
    item = input("Enter the item to add in menu or 'quit' to stop: ")
    if ("quit" == item):
        break
    else:
        print(f"{item} added to Menu")

# Find total of entered numbers until 0
total = 0
while True:
    input_num = input("Enter the number: ")
    number = int(input_num)
    if int(number) == 0:
        break
    total += number
print("Total:", total)

# Guessing loop with secret number
secret = 100
while True:
    input_number = input("Guess the secret number: ")
    number = int(input_number)
    if secret == number:
        print("You got it!")
        break
    elif number < secret:
        print("Number is lower than secret")
    else:
        print("Number is higher than secret")


# Break and Continue
for num in range(1, 101):
    if num % 7 == 0 and num % 9 == 0:
        print("First number divisible by both 7 and 9: ", num)
        break

# Find in list using loop
words = ["I", "am", "a", "AI", "Developer"]
input_word = input("Enter a word to find: ")
for word in words:
    if word == input_word:
        print("found")
        break
else:  # else can be come with if, while, for, try. Should have break inside loop to have else with loop
    print("Not found in the list of words")

# Process numeric values
numeric_values = [0, 4, -999, -2, 7, 8, 0, 3, 999, -0, 332, 23, 78779, -999, 9]
numbers = []
for num in numeric_values:
    if num == 999:
        break
    elif num < 0:
        continue
    else:
        numbers.append(num)
print("Final Number List:", numbers)
