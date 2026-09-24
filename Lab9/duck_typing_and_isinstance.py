# Duck typing

class Printer:
    def display_status(self):
        print("Working in good condition")


class Screen:
    def display_status(self):
        print("Not working. Repair needs to be done")

# Here both class have same method display_status(). But does not have any relationship
# Both class does not share common class, Still it can be called based on method corresponds to it s object


products = [
    Printer(),
    Screen(),
    Screen(),
    Printer()
]

for product in products:
    product.display_status()


# -----------------------------------------------------------

# isinstance() - built in function to check if object is instance of specific class

class User:
    pass


class AdminUser(User):
    pass


user = User()
admin = AdminUser()

print(isinstance(user, AdminUser))
print(isinstance(user, User))
print(isinstance(user, str))
print(isinstance(admin, User))
print(isinstance(admin, AdminUser))
print(isinstance(admin, str))

# all subclass object is intance of baseclass and subclass
# all baseclass object is instance of only baseclass
