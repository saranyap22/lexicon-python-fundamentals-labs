class Employee:
    def __init__(self, name):
        self.name = name

    def get_information(self):
        return f"Employee name {self.name}"


class Developer(Employee):
    def __init__(self, name):
        super().__init__(name)

    def get_programming_skills(self):
        return "Python, Java"


class Tester(Employee):
    def __init__(self, name):
        super().__init__(name)

    def get_testing_skills(self):
        return "selinium"


developer1 = Developer("Juvith")
tester1 = Tester("Hemanth")
print(developer1.get_information())
print(tester1.get_information())
print(developer1.get_programming_skills())
print(tester1.get_testing_skills())

employee = Employee("Aanand")
print(employee.get_information)
# employee.get_testing_skills()- Method only in subclass not visible for base class object
# employee.get_technical_skills() - Method only in subclass not visible for base class object
