# FizzBuzz from 1 to 100
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(num, "FizzBuzz")
    elif num % 3 == 0:
        print(num, "Fizz")
    elif num % 5 == 0:
        print(num, "Buzz")

# Count vowvels with loop
text = "I am studing System developer Python and AI"
vowvels = "aeiou"
count = 0
for char in text:
    if char in vowvels:
        count += 1
print("Number of Vowvels: ", count)

# Find duplicate values in list using loops
launguages = ["Python", "Java", "C#", "Scala", "SQL", "Python", "C#"]
launguage_count = {}
duplicate_launguages = set()
for launguage in launguages:
    if launguage in launguage_count:
        launguage_count[launguage] += 1
    else:
        launguage_count[launguage] = 1
for lan, count in launguage_count.items():
    if count > 1:
        duplicate_launguages.add(lan)
print("Duplicate values: ", duplicate_launguages)


# Text Histogram for numbers
numbers = [3, 6, 8, 1, 2, 4, 9]
for number in numbers:
    print(number * "*")
