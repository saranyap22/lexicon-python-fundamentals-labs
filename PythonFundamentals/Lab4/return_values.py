# find even
def is_even(number):
    if number % 2 == 0:
        return True
    return False


print(is_even(10))
print(is_even(11))
# is_even("10")  # TypeError during number %2
print(is_even(10.2))
# is_even("test")  # TypeError during number %2


# Get largest number
def get_larger(num_one, num_two):
    if (num_one > num_two):
        return num_one
    elif (num_two > num_one):
        return num_two
    return None


print(get_larger(6, 80))
print(get_larger(80, 80))
print(get_larger(90, 80))

# Classify score


def classify_score(score):
    if score >= 75:
        return "PASS"
    else:
        return "FAIL"


print(classify_score(45))
print(classify_score(75))
print(classify_score(80))

# write full name


def write_fullname(first_name, last_name):
    return f"{first_name} {last_name}"


print(write_fullname("saranya", "palanisamy"))


# calculate discount

# function does not return any value to the caller
def calculate_discount(price, percent):
    print(price * percent / 100)


print(calculate_discount(300, 3))  # This call does not receive any response
