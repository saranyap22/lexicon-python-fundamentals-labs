""" Module to explore positional unpacking"""

# Unpack List


def unpack_numbers(a, b, c):
    print(a, b, c)


numbers = [10, 20, 30]
unpack_numbers(*numbers)

# Unpack tuple


def unpack_tuple(first_name, last_name, city):
    print(first_name, last_name, city)


info = ("saranya", "palanisamy", "solna")
unpack_tuple(*info)

# Starred assignment


# anything after *args becomes keyword only. last is keyword only and mandatory
def create_full_name(first, *middle, last):  # *middle pack the the values as tuple
    print(first, get_all_middle_names(*middle), last)


def get_all_middle_names(*middle):
    middle_name = ""
    for mid in middle:
        middle_name += mid + " "
    return middle_name


# create_full_name("Dhiya", "Karthik", "Saranya") -> This will throw TypeError that missing keyword only argument: 'last'
# create_full_name("Dhiya", "Karthik"), create_full_name("Dhiya") -> Mandatory argument missing keyword "last"
create_full_name("Dhiya", last="saranya")
create_full_name("Dhiya", "Karthik", last="Saranya")
create_full_name("Dhiya", "Valaya", "Man", "Karthik", last="Saranya")
middle_name = ("Dan", "Marsh", "Moon")
# *middle_name unpacks tuple and pass as argument
create_full_name("Dhiya", *middle_name, last="Saranya")
