"""Module to explore *args"""


def add_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(add_all(1, 2, 4, 6, 7, 8))

# Average of numbers


def average(*numbers):
    # Unpack numbers (*numbers) and pass it as argument to add_all method. If only (numbers) passed then it will go as tuple
    total = add_all(*numbers)
    if len(numbers) <= 0:
        return None
    return total / len(numbers)


print(average())
print(average(1, 3, 6, 5, 54, 22, 45, 34))

# Longest word


def longest_word(*words):
    if len(words) <= 0:
        return None
    long_word = words[0]
    for word in words:
        if len(word) > len(long_word):
            long_word = word
    return long_word


print(longest_word())
print(longest_word("one", "nineteen", "two", "ten"))


# Build sentence


def build_sentence(separator, *words):
    sentence = ""
    for word in words:
        sentence = sentence + word + separator
    return sentence


print("Sentence: ", build_sentence("-", "I", "am", "doing", "good"))


# Describe scores
def describe_scores(student_name, *scores):
    count = len(scores)
    if count <= 0:
        return student_name, 0, 0.0
    total = 0
    for score in scores:
        total += score
    return student_name, count, f"{total/count:.2f}"


name, count, average = describe_scores("saranya", 40, 50, 26, 86, 48, 99)
print(f"Score Details: {name}, Count: {count}, Average: {average}")
