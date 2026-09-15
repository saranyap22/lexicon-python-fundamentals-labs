""" Module to elplore scope"""

# Local and Global variable
course_name = "Python"


def display():
    course_name = "Java"  # Local course name update does not reflect on global variable
    print("Local: Course Name:", course_name)


display()

# Global variable unaffected by change in local variable
print("Global: course Nameame", course_name)


# Accessing local variable outside function
def show_count():
    counter = 0
    print(counter+1)


show_count()
# print(counter) # counter variable does not remain available outside of method


# Change on global variable inside function # Not preferable way
counter = 0


def update_count_not_preferable():
    global counter
    counter += 1
    print("Local:", counter)
    return counter


update_count_not_preferable()
print("Global:", counter)


def update_count_not_preferable_hidden_dependency():
    counter_new = counter + 1
    return counter_new


counter = update_count_not_preferable_hidden_dependency()
print("Global:", counter)


def update_count_preferable(counter):
    counter += 1
    return counter


counter = update_count_preferable(counter)
print("Global:", counter)


# Nested function with enclosing scope

def display_info():
    count = 0

    def increment_counter():
        return count + 3

    count = increment_counter()
    print("Nested function enclosing variable:", count)


display_info()

# Avoid shadowing built ins
# list = [1, 3, 5, 7, 8]
# str = "shadowing"
# min = 0
# max = 0

# new_scores = list()
# max = max(list)
# min = min(list)

# Corrected way of using built in
my_list = [1, 3, 5, 7, 8]
my_str = "shadowing"
min_value = 0
max_value = 0

new_scores = list(my_list)
max_value = max(my_list)
min_value = min(my_list)
print(new_scores, max_value, min_value)
