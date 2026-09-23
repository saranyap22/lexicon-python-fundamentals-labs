class User:
    users = {}
    permissions = {
        "ADMIN": ("read", "write", "delete"),
        "PREMIUM": ("read", "write"),
        "USER": ("read",)
    }

    def __init__(self, email, role="USER"):
        self.email = email
        self.role = role
        self.username = email
        User.users[self.username] = {
            "email": self.email, "password": "Test", "permissions": User.permissions[role]}

    def login(self, username, password):
        user_info = self.get_user(username)

        if user_info["password"] == password:
            print("Logged in successfully")
        else:
            print("Faiiled to login")

    def get_permissions_info(self, username):
        user_info = self.get_user(username)
        return user_info["permissions"]

    def get_user(self, username):
        user_info = User.users.get(username)

        if not user_info:
            raise ValueError("User name not found")
        return user_info

    def is_existing_user(self, username):
        if self.get_user(username):
            return True
        return False


class AdminUser(User):
    role = "ADMIN"

    def __init__(self, email):
        super().__init__(email, AdminUser.role)

    def delete_user(self, username):
        if self.role == "ADMIN":
            if self.is_existing_user(username):
                User.users.pop(username)
                print(f"User {username} successfully deleted")


class PremiumUser(User):
    role = "PREMIUM"

    def __init__(self, email):
        super().__init__(email, PremiumUser.role)


# User has same attributes as AdminUser and PremiumUser so it shows "IS-A" relation ship. That why chosen Inheritance
admin = AdminUser("saranya@gmail.com")
premium = PremiumUser("vineeth@hotmail.com")
user = User("yathra@microsoft.com")

print("Admin: ", admin.email, admin.role)
print("Premium: ", premium.email, premium.role)
print("User: ", user.email, user.role)

print(admin.get_permissions_info(admin.username))
print(premium.get_permissions_info(premium.username))
print(user.get_permissions_info(user.username))

admin.login(admin.username, "Test")
premium.login(premium.username, "test")
user.login(user.username, "Test")

admin.delete_user(user.username)
print(premium.get_user(premium.username))
print(user.get_user(premium.username))
