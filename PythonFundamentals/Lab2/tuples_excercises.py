""" Tuples"""

# Tuples unpacking
rgb_value = ("RED", "GREEN", "BLUE")
r, g, b = rgb_value
print(f"r: {r}, g: {g}, b: {b}")

# Unpacking Mixed collection types

person_details = ("Saranya", 36, "Solna")
name, age, city = person_details
print(f"Name: {name}, Age: {age}, City: {city}")

# Tuple is immutable
# person_details[0] = "Karthik"  // Tuples does not support item assignment. Throw TypeError.
# //So tuples should be used when values should not be changed

# List of tuples
coordinates = [
    (10, 20), (15, 19), (30, 40), (2, 100)
]

print(coordinates[0][1])
print(coordinates[0][-1])
# coordinates[2][2] Runtime error : IndexError tuple index out of range
print(coordinates[1][1])
