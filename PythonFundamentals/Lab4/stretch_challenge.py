""" Module contains excercises related to functions"""
# Return two values


def find_min_max(numbers: list) -> tuple:
    """ Function to find minimun and maximum number from list of numbers"""
    min = numbers[0]
    max = numbers[0]
    for number in numbers:
        if number < min:
            min = number
        if number > max:
            max = number
    return min, max


numbers = [3, 7, 2, -9, 5, 0, 45, 12, 45, 77]
min_value, max_value = find_min_max(numbers)
print(f"Minimum value: {min_value}, Maximum value: {max_value}")


# palindrome


def is_palindrome(text: str) -> bool:
    """ function to check if a string is palindrome"""
    reverse = text[::-1]
    if text == reverse:
        return True
    else:
        return False


print(is_palindrome("level"))
print(is_palindrome("hello"))


# Char frequency count
def char_frequency_count(text: str) -> dict:
    """Function to create character frequency count from a string"""
    frequency_count = {}
    for char in text:
        if char in frequency_count:
            frequency_count[char] += 1
        else:
            frequency_count[char] = 1
    return frequency_count


input = "I started lab excercises for Python"
print(char_frequency_count(input))


# numbers frequency count (positive,negative and zero)
def num_frquency_count(numbers: list) -> dict:
    """ Function to find positive, negative and zero count"""
    num_frequency_count = {}
    for num in numbers:
        if num > 0:
            key = "positive"
        elif num < 0:
            key = "negative"
        else:
            key = "zero"
        num_frequency_count[key] = num_frequency_count.get(key, 0)+1
    return num_frequency_count


numbers = [4, 1, -8, 0, 5, 9, 12, 0, -56, -34]
print(num_frquency_count(numbers))
