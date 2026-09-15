""" Module contains functions to handle  event registration processor"""


def normalize(participant_name):
    normalized_name = participant_name.strip().lower()
    return normalized_name


def is_valid_age(age):
    if age >= 18:
        return True
    return False


def calculate_registration_fee(age, type):
    fee = 100
    if type == "student":
        return 0
    return fee


def create_participants():
    participants = [
        {"name": "Saranya ", "email": "saranya@gmail.com",
            "event": "Python Meetup", "type": "student", "age": 35},
        {"name": " Malar", "email": "malar@gmail.com",
            "event": "Java Meetup", "type": "VIP", "age": 45},
        {"name": "Allan ", "email": "allan@gmail.com",
            "event": "C# Meetup", "type": "student", "age": 24},
        {"name": "Bob", "email": "bob@gmail.com",
            "event": "AI Workshop", "type": "VIP", "age": 60},
        {"name": " Krithik", "email": "krithik@gmail.com",
            "event": "Jobspranget", "type": "student", "age": 16},
        {"name": "Gugan", "email": "gugan@gmail.com",
            "event": "Python Meetup", "type": "General", "age": 21},
        {"name": "Allu", "email": "saranyasamy2@gmail.com",
            "event": "AI workshop", "type": "student", "age": 26}
    ]
    return participants


def main():
    participants = create_participants()
    final_participants = []
    invalid_participants = []
    for participant in participants:
        if is_valid_age(participant["age"]):
            participant["name"] = normalize(participant["name"])
            participant["fee"] = calculate_registration_fee(participant["age"],
                                                            participant["type"])
            final_participants.append(participant)
        else:
            invalid_participants.append(participant)
    print(
        f"Final Participants: {final_participants}, \n\n {invalid_participants}")


main()
