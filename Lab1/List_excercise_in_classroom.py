
# List
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][1])

# List mutability
matrix[1][1] = 0
print(matrix[1][1])


# dictionaries
students = [
    {
        "name": "Anna",
        "score": 85
    },
    {
        "name": "Bob",
        "score": [72, 30]
    }
]
print(students[1]["score"][0])

# dictionary key as integer
# dictionaries
students = [
    {
        1: "Anna",
        2: 85
    },
    {
        1: "Bob",
        2: 72
    }
]
print(students[1][2])
