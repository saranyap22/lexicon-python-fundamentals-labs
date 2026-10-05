def flatten_grid(grid):
    final_list = []
    """ Return flattened list by looping with indexes"""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            final_list.append(grid[i][j])
    return final_list


def flatten_grid_with_comprehension(grid):
    """ Return a flattened list by using list comprehension"""
    return [
        num
        for list in grid
        for num in list
    ]


grid = [
    [1, 2, 3, 4],
    [6, 4, 3, 2],
    [8, 5, 3, 2]
]

print("Flatterned List: ", flatten_grid(grid))
print("Flatterned List with comprehension: ", flatten_grid(grid))


# Preferred. using comprehension makes Code more readable and simple
def create_multiplication_table(numbers):
    return [[i * j for i in numbers] for j in numbers]


print(create_multiplication_table(range(1, 11)))


def create_passing_student(students):
    return [
        student
        for student in students
        if student["score"] >= 60
    ]


students = [
    {"name": "Allan", "score": 78},
    {"name": "Bob", "score": 54},
    {"name": "Grace", "score": 100}
]
print("Passing Students: ", create_passing_student(students))
