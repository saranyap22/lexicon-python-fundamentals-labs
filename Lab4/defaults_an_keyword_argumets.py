# Keyword and positional arguments
def greet(name, greeting="Hello"):
    return f"{greeting} {name}"


print(greet("saranya"))


# works fine. Positional first , keyword after
print(greet("Allen", greeting="Hi"))

# Do not work. keyword argument cannot come after Positional argument
# print(greet(greeting="Hi", "Allen"))


print(greet(greeting="Hi", name="Allen"))  # works fine. Both Keyword arguments


# create profile with default parameter and call with positional argument and keyword argument
def create_profile(name, city="Unknown", active=True):
    profile = {"name": name, "city": city, "active": active}
    return profile


print(create_profile("saranya", "solna", True))
print(create_profile("saranya", "solna", False))
print(create_profile(name="saranya", city="solna", active=False))
# print(create_profile(city="solna", "saranya", active=False)) # cannot have positional argument after keyword argument
print(create_profile("Aaron"))
print(create_profile("Vinay", "Sundbyberg"))
print(create_profile("Vinay"))
