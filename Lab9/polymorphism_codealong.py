# Polymorphism

# class Dog:
#     def make_sound(self):
#         return "Woof!"


# class Cat:
#     def make_sound(self):
#         return "Meow!"


# class Cow:
#     def make_sound(self):
#         return "Moo!"


# animals = [
#     Dog(),
#     Cat(),
#     Cow()
# ]

# for animal in animals:
#     print(animal.make_sound())


# -----------------------------------------------------------

# Polymorphism with inheritance

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         return "Unknown sound"


# class Dog(Animal):

#     def make_sound(self):
#         return "Woo!"


# class Cat(Animal):

#     def make_sound(self):
#         return "Meow!"


# animals = [
#     Dog("Rex"),
#     Cat("Luna")
# ]

# for animal in animals:
#     print(animal.name, animal.make_sound())


# -----------------------------------------
# Duck Typing

# class Robot:
#     def make_sound(self):
#         return "Beep"


# class Dog:
#     def make_sound(self):
#         return "Woof"


# things = [
#     Robot(),
#     Dog()
# ]

# for thing in things:
#     print(thing.make_sound())

# ----------------------------

# isinstance()

# class Animal:
#     pass


# class Dog(Animal):
#     pass


# dog = Dog()
# print(isinstance(dog, Dog))
# print(isinstance(dog, Animal))
# print(isinstance(dog, str))


# ---------------------------------------------------------------------

# class not having non readable class while printing


# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score


# student = Student("Ada", 91)
# print(student)  # print the class name and object

# text = str(student)
# print(text)
# ------------------------------------

# Useful feature of class


# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def __str__(self):
#         return f"{self.name} - Score: {self.score}"


# Student = Student("Ada", 91)
# print(Student)  # print readable format

# text = str(student)
# print(text)
# -----------------------------------------


# __str__with inheritance

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def __str__(self):
#         return (
#             f"Name: {self.name} -"
#             f"Salary: {self.salary}"
#         )


# class Developer(Employee):
#     def __init__(self, name, salary, launguage):
#         super().__init__(name, salary)
#         self.launguage = launguage

#     def __str__(self):
#         return (
#             f"{self.name} - Developer -"
#             f"{self.launguage}"
#         )


# employee = Employee("Grace", 10000)
# developer = Developer("Ada", 67899, "Python")

# print(employee)
# print(developer)


# -----------------------------------------------------------

# So far seen inheritance with
# "Is-A" (relationship)

# Now another way of relating classes Together
# HAS-A (composition)

# class Engine:
#     def __init__(self, horsepower):
#         self.horsepower = horsepower


# class Car:
#     def __init__(self, brand, engine):
#         self.brand = brand
#         self.engine = engine


# engine = Engine(200)
# car = Car("Volvo", engine)

# print(car.brand)
# print(car.engine.horsepower)


# -----------------------------------------------------
