# merge setting
def merge_setting(defaults, **overrides):
    merged_settings = {
        "defaults": defaults,
        "overrides": overrides
    }
    return merged_settings


def merge_settings(defaults, **overrides):
    merged_settings = {**overrides, **defaults}
    return merged_settings


default_settings = {
    "theme": "dark",
    "notification_enabled": True,
    "launguage": "en",
    "timezone": "Europe/Stockholm"
}
optional_settings = {
    "extra_features": True,
    "theme": "high_contrast"
}
print(merge_settings(default_settings, **optional_settings))


# Call summary
def call_summary(function_name, *args, **kwargs):

    return f"{function_name}({args},{kwargs})"


print(call_summary("show_profile", "saranya",
                   **{"age": 35, "city": "solna"}))


# flexible statistics function

def statistics(*numbers):
    if len(numbers) <= 0:
        return None
    count = 0
    total = 0
    min_num = numbers[0]
    max_num = numbers[0]
    for num in numbers:
        count += 1
        total += num
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    average = round(total / count, 2)
    return count, total, min_num, max_num, average


numbers = [34, 57, 2, 4, 67, 75]
count, total, min_num, max_num, average = statistics(*numbers)
print(count, total, min_num, max_num, average)


# Predict output scope questions
# 1. What happen if counter updated to 1 inside but not returned -> outside counter = 0
# 2. cleaner approach -> pass the global variable as argument to function and return the updated value to caller, so global value updated
# 3. Is there anyway to access global variable directly inside function -> yes with keyword "global" counter
# 4. is function parameter is local or global scope -> local
# 5. Not recommented approach -> updating by declaring "global" keyword inside functions
counter = 0


def modify_count(count):
    return count + 1


counter = modify_count(counter)
print(counter)
