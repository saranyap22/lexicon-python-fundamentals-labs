# Python misktake to keep in mind
# PROBLEM: the default parameters initialised only the first time when initialised and could be sharead with other objects

# class Course:
#     def __init__(self, name, students=[]):
#         self.name = name
#         self.students = students

# ---------------------------------


# class BadCourse:
#     def __init__(self, name, students=[]):
#         self.name = name
#         self.students = students

#     def add_student(self, student):
#         self.students.append(student)


# course1 = BadCourse("Python")
# course2 = BadCourse("AI")

# print(course1.students)
# print(course2.students)

# course1.add_student("Ada")
# print(course1.students)
# print(course2.students)


# -------------------------------------------

# Correct pattern to implement

# class Course:
#     def __init__(self, name, students=None):
#         self.name = name
#         if students is None:
#             students = []

#         self.students = students

#     def add_student(self, student):
#         self.students.append(student)


# course1 = Course("Python")
# course2 = Course("AI")

# course1.add_student("Ada")
# print(course1.students, course2.students)


# ----------------------------------------------------------------

# DICTIONARY VS CLASS

# Dictionary good choice simple data
# student_dict = {
#     "name": "Ada",
#     "score": 91
# }


# # Class useful when many object share same structure and common useful functions
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score


# student = Student("Ada", 91)

# print(student_dict, student.name, student.score)


# --------------------------------------------------------------
