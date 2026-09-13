launguage = ["Python", "Java", "C#", "JavaScript",
             "NodeJS", "NextJS", "Ruby", "Go", "C#", "C", "C++"]
launguage_two = ["Python", "Java", "C#", "JavaScript",
                 "NodeJS", "NextJS", "Ruby", "Go", "C#", "C", "C++"]

# Accessing List with index
print(launguage[0])
print(launguage[-1])
print(launguage[2])
print(launguage[-2])

# slicing

print(launguage[:3])  # first 2 element
print(launguage[-3:])  # last 3 elements
print(launguage[1:-1])  # elemets excluding first and last
print(launguage[::1])  # every first element
print(launguage[::2])  # every second element
print(launguage[::-1])  # rever of string

# Methods frequently used
print(f"Unmodified List: {launguage}")
launguage.append("SQL")  # Add SQL in the end of list
print(f"Appended List: {launguage}")

launguage.insert(2, "Scala")  # Insert "Scala" at index 2
print(f"Inserted at index 2 List: {launguage}")

launguage.remove("C#")  # Removes first occurance of element from list
print(f"Removed C# from List: {launguage}")

# launguage.remove("Perl") ## Remove with unknown element result ValueError
print(f"Current from List: {launguage}")

# Remove element from index and give the elememt as response
popped_laun = launguage.pop(-2)
print(f"Current from List: {launguage} and popped Laungusge: {popped_laun}")

# Methods supporting numeric operations

numbers = [20, 10, 40, 60, 80, 100, 10, 100]
numbers_two = [4, 3, 7, 9, 2, 4, 6, 8, 10]
print(numbers)

print(f"Count: {numbers.count(100)}")  # Returns count of specific element
print(f"Maximun num: {max(numbers)}")  # Return Max number of the list
print(f"Maximun num: {min(numbers)}")  # Return Min number of the list
print(f"Sum: {sum(numbers)}")
numbers.sort()
print(f"Sort list: {numbers}")  # sorted in ascending
# Prefer to use when need to sort non modifyable collection
print(f"Sorted list: {sorted(numbers_two)}")
numbers.sort(reverse=True)
print(f"Decending  list: {numbers}")  # sorted in decending
print(f"Decending list: {sorted(numbers_two, reverse=True)}")

# Compare character by character do like dictionary sort return Max
print(f"Maximun launguage: {max(launguage)}")
# Compare character by character do like dictionary sort return min
print(f"Maximun launguage: {min(launguage)}")
launguage.sort()
print(f"Sorted launguage: {launguage}")  # sorted in ascending
# Prefer to use when need to sort non modifyable collection
print(f"Sorted launguage: {sorted(launguage_two)}")

launguage.sort(reverse=True)
# sorted in decending
print(f"Sort  launguage decending : {launguage}")
# Prefer to use when need to sort decending non modifyable collection
print(f"Sorted  launguage decending: {sorted(launguage_two, reverse=True)}")


# Reference Copy issue // when a referene re assigned then pointing of object also changed
a = [1, 2, 3, 4, 4]
b = [6, 7, 7, 3, 0]
b = a
print(f"List a: {a}")
print(f"List b: {b}")
