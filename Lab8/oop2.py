# INHERITANCE

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def eat(self):
#         print(self.name, "is eating")


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def eat(self):
#         print(self.name, "is eating")


# dog = Dog("Rex", 5)
# cat = Cat("Luna", 3)

# dog.eat()
# cat.eat()

# -----------------------------

# Inheritence

# TERMINOLOGY:
# Animal - (Base class | Parent class | Super class)
# Dog,Cat - (Sub class | child class | Derived class)

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def eat(self):
#         print(self.name, "is eating")


# class Dog(Animal):
#     pass


# class Cat(Animal):
#     pass


# dog = Dog("Rex_new", 6)
# cat = Cat("Luna_new", 3)
# dog.eat()
# cat.eat()

# dog = Animal("Rex", 6)
# cat = Animal("Luna", 3)
# dog.eat()
# cat.eat()

# ---------------------------------------------------------------------
# When Inheritance should be used
# Ask question
#  subclass is a parent class? - "IS -A" test

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         return f"{self.name} is eating"

#     def sleep(self):
#         return f"{self.name} is sleeping"


# class Dog(Animal):
#     def bark(self):
#         return f"{self.name} says woof"


# class Cat(Animal):
#     pass


# dog = Dog("Rex")
# print(dog.eat())
# print(dog.sleep())
# print(dog.bark())

# animal = Animal("Unknown")  # NOT optimum way
# print(animal.bark())  # animal does not know bark method

# ----------------------------------------------------------------
# Duplication in __init __ name and age assignment
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def eat(self):
#         return f"{self.name} is eating"

#     def sleep(self):
#         return f"{self.name} is sleeping"


# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed


# dog = Dog("Rex", 5, "Larador")
# print(dog.name, dog.age, dog.breed)
# print(dog.sleep())

# --------------------------------------------------
# super().__init__(name,age) to pass argument to superclass __init__ method
# All the common code should be in BaseClass

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.is_alive = True
#         if age < 0:
#             raise ValueError("Age cannot be negative!")

#     def eat(self):
#         return f"{self.name} is eating"

#     def sleep(self):
#         return f"{self.name} is sleeping"


# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         # We dont need self here since current instance handled automatically
#         super().__init__(name, age)
#         self.breed = breed


# dog = Dog("Rex", 5, "Larador")
# print(dog.name, dog.age, dog.breed)
# print(dog.sleep())


# -----------------------------------------------------


# Method Overriding

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         return "Some Animal Sound"


# class Dog(Animal):
#     def make_sound(self):
#         return "woof!"


# class Cat(Animal):
#     def make_sound(self):
#         return "Meow!"


# animal = Animal("Animal")
# dog = Dog("Rex")
# cat = Cat("Luna")

# print(animal.make_sound())
# print(dog.make_sound())
# print(cat.make_sound())


# --------------------------------------

# class Employee:

#     def get_information(self):
#         return "Employee information"


# class Developer(Employee):

#     def get_information(self):
#         base_info = super().get_information()
#         return base_info + "- Role: Developer"


# developer = Developer()
# print(developer.get_information())

# ---------------------------------------------------------


# Upcoming class polymorphism
# inheritance with polymorphism
# duck typing
