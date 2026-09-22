# class Student:
#     pass


# student1 = Student()
# student2 = Student()
# print(type(student1))
# print(student1)
# print(student2)
# print(student1 is student2)
# # --------------------------------------

# # Add infor manually

# student1 = Student()
# student1.name = "saranya"
# student1.age = 36

# print(student1.name)
# print(student1.age)

# student2 = Student()
# student2.name = "Victor"
# student2.age = 3

# print(student2.name)
# print(student2.age)


# # ---------------------------------------------------


# class Student:
#     def __init__(self, name, score):  # self is not keyword. But use as self as conveion to be clear
#         self.name = name
#         self.score = score


# student1 = Student("Ada", 78)
# print(student1.name)
# print(student1.score)

# # self -> object student1


# student2 = Student("Meena", 7)
# print(student2.name)
# print(student2.score)

# # self-> object student2

# # -------------------------------------


# class Student:
#     def __init__(self, student_name, student_score):
#         self.name = student_name
#         self.score = student_score


# student1 = Student("sara", 78)
# print(student1.name)
# print(student1.score)

# # -------------------------------------------


# class Student:
#     def __init__(self, name, score=0, active=True):
#         self.name = name
#         self.score = score
#         self.active = active

#     def introduce(self):
#         print(f"Hello my name is: {self.name}")

#     def get_status(self):
#         if self.score >= 60:
#             return "Pass"
#         return "Fail"

#     def update_score(self, new_score):
#         if new_score < 0 and new_score <= 100:
#             raise ValueError("Score must be between 0 and 100")
#         self.score = new_score


# student1 = Student("Fati", 78, False)

# # Wron arg passed will be accepted without causing error
# student2 = Student(78, "Fati", False)

# student3 = Student(name="Grace", score=65, active=False)

# student4 = Student("Grace", active=False)
# student5 = Student("Grace", 20, True)

# print(student1.name, student1.score, student1.active)
# print(student2.name, student2.score, student2.active)
# print(student3.name, student3.score, student3.active)
# print(student4.name, student4.score, student4.active)
# student5.introduce()
# status = student5.get_status()
# print(status)

# student5.update_score(90)
# print(student5.get_status())
# # -------------------------------------------------


# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         if amount < 0:
#             raise ValueError("Amount shou;ld be more than zero")


# account1 = BankAccount("sara", 560)
# print(account1.owner, account1.balance)

# account2 = BankAccount("Mio", 19)
# print(account2.owner, account2.balance)
# account2.deposit(100)

# print(account2.balance)
# account2.deposit(-100)

# # ----------------------


# class Student:

#     school = "Lexicon"

#     def __init__(self, student_name, student_score):
#         self.name = student_name
#         self.score = student_score

#     def update_score(self, score):
#         self.score = score


# student1 = Student("sara", 78)
# print(student1.name)
# print(student1.score)

# student1.name = "Saranya"
# print(student1.name)


# # accessing class attribute with class name. Shared at class level
# print(Student.school)
# Student.school = "AI academy"
# print(Student.school)

# # instance attributes : Data belonging to an indivudual object
# student1.school = "New School"
# print(student1.school)
# print(Student.school)

# # -------------------------------------------


# class Product:
#     tax_rate = 0.25

#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def price_with_tax(self):
#         return self.price + self.price * self.tax_rate


# product1 = Product("keyboard", 100)
# product2 = Product("Mouse", 50)

# print(product1.price_with_tax())
# print(product2.price_with_tax())


# # --------------------------------------------------
# Collection of objects

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def get_status(self):
#         if self.score >= 60:
#             return "Pass"

#         return "Fail"


# students = [
#     Student("sara", 10),
#     Student("Maya", 100),
#     Student("Kavya", 78)
# ]

# for student in students:
#     print(student.name,
#           student.score,
#           student.get_status())

# passed_students = [
#     student
#     for student in students
#     if student.score >= 60
# ]

# for student in passed_students:
#     print(student.name)

# ----------------------------------------------------
# Object within another object
# class Teacher:
#     def __init__(self, name):
#         self.name = name


# class Course:
#     def __init__(self, name, teacher):
#         self.name = name
#         self.teacher = teacher


# teacher1 = Teacher("sara")
# course1 = Course("Python", teacher1)


# print(course1.name, course1.teacher.name)

# --------------------------------------------

class Student:
    def __init__(self, name):
        self.name = name


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)


student1 = Student("Hema")
student2 = Student("Grace")

course = Course("Python")

course.add_student(student1)
course.add_student(student2)

for student in course.students:
    print(student.name)

student3 = Student("Yusuf")
student4 = Student("Peter")

course2 = Course("Java")

course2.students.append(student3)
course2.students.append(student4)

for student in course2.students:
    print(student.name)
