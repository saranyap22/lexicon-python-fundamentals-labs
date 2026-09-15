""" Module to explore *kwargs"""

# Show profile info


def show_profile(**info):  # **info is pack the dictionary values
    for key, value in info.items():
        print(f"{key}: {value}")


info = {
    "name": "saranya",
    "age": 35,
    "city": "solna"
}
show_profile(**info)  # Unpack the dictionary and passed as arguments


# create user
def create_user(username, **details):
    details["username"] = username
    show_profile(**details)


info = {
    "name": "saranya",
    "age": 35,
    "city": "solna"
}

create_user("saranyasamy2", **info)


# Build product
def build_product(name, price, **metadata):
    product_info = {}
    product_info["name"] = name
    product_info["price"] = price
    product_info.update(metadata)
    return product_info


# Calling same flexible functino with different arguments
print(build_product("Laptop", 1000.00, category="Electronics", stock=1))
print(build_product("Pendrive", 100.00, category="Electronics", stock=10))
print(build_product("Mouse", 10.00, category="Electronics"))
print(build_product("Laptop", 1000.00))


# create settings
def build_settings(**settings):
    final_settings = {}
    for setting, value in settings.items():
        if value is not None:
            final_settings[setting] = value
    return final_settings


user_setting = {"theme": "dark", "launguage": "en",
                "notification_enabled": True, "timezone": "Europe/Stockholm", }
print(build_settings(**user_setting))
print(build_settings(**{"theme": "white", "launguage": "se",
                        "notification_enabled": False, "timezone": None}))


# When to use named parameter vs **kwargs
# Use named parameter like username when we already know the field and need to enforce it
def show_user(user, **details):  # use **kwargs when we do not know the fields that are optional
    show_profile(**details)


info = {
    "name": "saranya",
    "age": 35,
    "city": "solna"
}

show_user("saranyasamy2", **info)
