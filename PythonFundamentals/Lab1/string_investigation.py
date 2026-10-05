# Idexing and Slicing
text = "Welcome to day 2 of Lexicon System Developer Python and AI training"

# "Welcome to day 2 of Lexicon System Developer Python and AI training" - also (0:)
print(text[:])

# reverse of "Welcome to day 2 of Lexicon System Developer Python and AI training"
print(text[:: -1])

# "Welcome to day 2 of Lexicon System Developer Python and AI trainin"
print(text[: -1])

# "elcome to day 2 of Lexicon System Developer Python and AI trainin"
print(text[1: -1])

# " day "  - Fistart index included and end index excluded.
print(text[10: 15])

print(text[0])  # "W" - element at index 0
print(text[-1])  # "g" - element at last index
print(text[11])  # "d"
# print(text[200])  # Index Error

# Slicing
text = "ArtificialIntelligence"

print(text[:])  # return original - "ArtificialIntelligence"

print(text[0:])  # return original - "ArtificialIntelligence"

# return  text without last char - "ArtificialIntelligenc"
print(text[0:-1])

# return text without start and end char - "rtificialIntelligenc"
print(text[1:-1])

print(text[::])  # return original - "ArtificialIntelligence"
print(text[::-1])  # return reverse

# return text start from 0 index and skip every next 2 index - "AtfcaItliec"
print(text[::2])

# return text start from 0 index and skip every next 4 index - "Afatic"
print(text[::4])

# return text start from last index reverse and skip every next 2 index - "AtfcaItliec"
print(text[::-2])

# return text start from 0 index reverse and skip every next 4 index - "Afatic"
print(text[::-4])


# Invetigate difference
text = " I am fine "
# split() - split string with space if no parameter and return list of string - text.split() -> [" I","am","fine "]
print(text.split())

# strip() - remove space before and after string - text.strip() -> "I am fine"
print(text.strip())

# replace() - replace part of given string in source with target string - text.replace("I am", "We are") -> " We are fine"
print(text.replace("I am", "We are"))

# in operator - check if substring found in the string - "am" in text - True
print("am" in text)

# Str immutability
text = "I am taking System Developer Python course"
# text[0] = "W" - text not support item assignment - not possible

# replace target String in first occurance of source - W am taking System Developer Python course
print(text.replace("I", "W"))
