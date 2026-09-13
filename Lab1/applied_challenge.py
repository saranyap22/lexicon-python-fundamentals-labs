# Registration Summary
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
city = input("Enter city: ")
year_of_birth = input("Enter year of birth: ")
launguage = input(
    "Enter favourite programming launguage: ")
user_id = (first_name[:4] + last_name[-4:] + year_of_birth).lower()
summary = f"""
    First Name:  {first_name} 
    Last Name: {last_name}
    Year Of Birth: {year_of_birth}
    City: {city} | UserId: {user_id} 
"""
print(summary)

initial = f"{first_name[:1]}{last_name[:1]}".upper()
name_without_space = (first_name + last_name).replace(" ", "")
launguage_reverse = launguage[::-1]

print(
    f"Initial : {initial} | Name Length: {len(name_without_space)} | Favourite Launguage: {launguage_reverse}")
