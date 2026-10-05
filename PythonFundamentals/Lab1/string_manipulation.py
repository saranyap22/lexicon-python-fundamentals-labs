"""This module contains Methods for String manipulation """
text = "I am a Java developer"
print(text.replace("Java", "Python"))

email_address = "saranyasamy2@gmail.com"
index = email_address.index("@")
print("Part before @: " + email_address[:index] + "\n" +
      "Part after @:" + email_address[index+1:])


def generate_username(first_name, last_name):
    """Function to generate username """
    first_name = first_name.strip().lower()
    last_name = last_name.strip().lower()
    user_name = first_name[:3] + last_name[:5]
    print("username: " + user_name)

    first_name = input("Enter First name:")
    last_name = input("Enter last name:")
    generate_username(first_name, last_name)

    text = "python programming"
    print(text[0])
    print(text[-1])
    print(text[:6])
    print(text[-7:])
    print(text[::-1])

    first_name = input("Enter first name:")
    last_name = input("Enter last name")
    print(f"{first_name} {last_name}")

    text = "Today is the first day of Lexicon System Developer Python and AI"
    print(len(text))
    print(text.upper())
    print(text.lower())
    print(text.strip().lower())
    print(text.strip().upper())
