# built in fuction to print strings
print("Saranya Palanisamy" + "\n" + "System Developer Python and AI" + "\n" +
      "Today's lesson focussed on Python fundamentals like data types, operators, Strings , methods that ca be used with string and built in functions")

# Data types str, int, float, bool
name = "Saranya Palanisamy"
age = 35
height = 1.5
is_student = True

print(f"name + {type(name)}")
print(f"age + {type(age)}")
print(f"height + {type(height)}")
print(f"is_student + {type(is_student)}")

# Conversion error incompatible types
# print(f"name + {int(name)}") // ValueError invalid literal for int()
# print(float(name)) // ValueError could not convert to float

# Conversion from other data types to boolean result True
print(bool(name))
print(bool(age))
print(bool(height))
print(bool(is_student))
print(bool(" "))

# Conversion from other data types to boolean result False
print(bool(""))
print(bool([]))
print(bool(0))

# Data type conversion
name = "Saranya Palanisamy"
age = "35"
height = "1.5"
is_student = "True"
con_age = int(age)
con_height = float(height)
con_is_student = bool(is_student)

print(f"age + {type(con_age)}")
print(f"height + {type(con_height)}")
print(f"is_student + {type(con_is_student)}")


# Operators
input_one = 5
input_two = 3
print(f"Addition: {input_one + input_two}")
print(f"Subraction: {input_one - input_two}")
print(f"Multiplication: {input_one * input_two}")
print(f"Division: {input_one / input_two}")
print(f"Floor division: {input_one // input_two}")
print(f"Exponential: {input_one ** input_two}")
print(f"Mod: {input_one % input_two}")


# Examples of type conversion necessary
age = "19"
amount = 100
height = 1.5
person_age = int(age)
person_amount = float(amount)
person_height = str(height)
print("Age:" + str(person_age) + ":" + str(type(person_age)) + ", Amount:" + str(person_amount) +
      ":" + str(type(person_amount)) + ", Height:" + str(person_height) + ":" + str(type(person_height)))
