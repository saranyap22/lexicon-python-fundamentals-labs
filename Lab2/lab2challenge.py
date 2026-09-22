"""Conference Planning System"""
# Part 1: Design Conference Data
sessions = [
    {"title": "Foundations of Machine Learning ", "speaker": "Ramanadan",
        "room": "ARN11", "duration": 120, "topic": "AI foundations", "max_no_of_participants": 100},
    {"title": "Foundation of Neural Networks ", "speaker": "Anna Bel", "room": "ARN11",
        "duration": 60, "topic": "AI foundations", "max_no_of_participants": 900},
    {"title": "Modernizing public HealthCare Systems", "speaker": "Geogdea", "room": "ARN12",
        "duration": 45, "topic": "AI in Healthcare", "max_no_of_participants": 103},
    {"title": "Advanced Cyber Security for AI and Cloud", "speaker": "Macdonald Graham", "room": "ARN13", "duration": 90,
        "topic": "AI and Cybersecurity", "max_no_of_participants": 50},
    {"title": "Automation with Computer Vision", "speaker": "Jennyfer", "room": "ARN14", "duration": 50,
        "topic": "AI and Robotics", "max_no_of_participants": 98},
    {"title": "Climate Change Mitigation", "speaker": "Geogdea", "room": "ARN13",
        "duration": 30, "topic": "Sustanability", "max_no_of_participants": 300},
    {"title": "Predictive Diagnostics and AI Systems in Healthcare", "speaker": "Jennyfer", "room": "ARN14", "duration": 130,
        "topic": "AI in Healthcare", "max_no_of_participants": 678},
    {"title": "Autonomous Workflows", "speaker": "Geogdea", "room": "ARN12", "duration": 60,
        "topic": "AI and Robotics", "max_no_of_participants": 700}
]

speakers = {
    "Ramanadan": {"age": 50, "city": "Stockholm",
                  "skills": {"Python", "Machine Learning"}},
    "Anna Bel": {"age": 28, "city": "Solna",
                 "skills": {"AI foundations", "Machine Learning", "Neural Networks"}},
    "Jennyfer": {"age": 20, "city": "Goteborg",
                 "skills": {"AI foundations", "Machine Learning", "Predictive Modeling",
                            "Medical Data Analysis", "Python"}},
    "Macdonald Graham": {"age": 80, "city": "Malmo",
                         "skills": {"AI foundations", "Machine Learning",
                                    "Cyber Security", "Cloud Security"}},
    "Geogdea": {"age": 59, "city": "Scotland",
                "skills": {"AI foundations", "Machine Learning", "Predictive Modeling",
                           "Medical Data Analysis", "Python"}}
}

rooms = {
    "ARN11", "ARN12", "ARN13", "ARN14"
}

participants = {
    "Anna": {"age": 50, "city": "Stockholm"},
    "Vidhu": {"age": 28, "city": "Solna"},
    "Meha": {"age": 20, "city": "Goteborg"},
    "Kishore": {"age": 80, "city": "Malmo"},
    "Delna": {"age": 59, "city": "Scotland"},
    "Bob": {"age": 50, "city": "Stockholm"},
    "Victor": {"age": 28, "city": "Solna"},
    "Sara": {"age": 20, "city": "Goteborg"},
    "Danial": {"age": 80, "city": "Malmo"},
    "Mahil": {"age": 59, "city": "Scotland"}
}

topics = {"AI foundations",
          "AI and Cybersecurity",
          "AI in Healthcare",
          "Climate Change Mitigation",
          "AI and Robotics"
          }

speakers_sessions = {
    "Ramanadan":  ["Foundations of Machine Learning"],
    "Anna Bel": ["Foundation of Neural Networks "],
    "Geogdea": ["Modernizing public HealthCare Systems", "Autonomous Workflows",
                "Climate Change Mitigation"],
    "Macdonald Graham": ["Advanced Cyber Security for AI and Cloud"],
    "Jennyfer": ["Predictive Diagnostics and AI Systems in Healthcare"]
}

registered_session_participants = {
    "Foundations of Machine Learning": {"Anna", "Vidhu", "Meha"},
    "Foundation of Neural Networks ": {"Kishore", "Delna", "Bob"},
    "Modernizing public HealthCare Systems": {"Bob", "Meha"},
    "Climate Change Mitigation": {"Victor", "Sara", "Anna"},
    "Advanced Cyber Security for AI and Cloud": {"Danial"},
    "Predictive Diagnostics and AI Systems in Healthcare": {"Mahil"},
    "Autonomous Workflows": {"Sara", "Vidhu"}
}

# Choose Tuple to represent information that is not going to change during conference. Can be accessed with tuple unpacking
conference_dates = (("20-09-2026", "25-09-2026"))
opening_closing_times = ("09:00", "17:00")
contact_information = (("conference@gmail.com", "07547658444"))

# ----------------------------------------------------------------
# Part 2:  Work with SChedule
print(f"Title: {sessions[0]["title"]}")
print(f"Speaker: {sessions[2]["speaker"]}")
print(f"Room: {sessions[-1]["room"]}")
print(f"All info about session: {sessions[1]}")
print(f"First theree sessions: {sessions[:3]}")
print(f"Last two sessions: {sessions[-2:]}")
print(f"Reversed session schedule: {sessions[::-1]}")
partial_sessions_copy = sessions[:5].copy()
print(f"Partial Session Copy: {partial_sessions_copy}")


# ------------------------------------------------------------
# Part 3: Conference changes
sessions[-1]["room"] = "ARN13"
print(f"Modified room: {sessions[-1]["room"]}")

sessions.append({"title": "Autonomous in Manufacturing", "speaker": "Anna Bel", "room": "ARN11", "duration": 60,
                 "topic": "AI and Robotics", "max_no_of_participants": 150})
print(sessions[-1])

sessions.remove(sessions[-1])
print(sessions[-1])

registered_session_participants["Modernizing public HealthCare Systems"].add(
    "Anna")
print(
    f"Registered: {registered_session_participants["Modernizing public HealthCare Systems"]}")

sessions[-1]["difficulty"] = "Advanced"
print(f"Newly added field: {sessions[-1]["difficulty"]}")


# ----------------------------------------------
# Part 4: Unique Conference Information
unique_skills = speakers["Ramanadan"]["skills"] | speakers["Anna Bel"]["skills"] | speakers[
    "Geogdea"]["skills"] | speakers["Jennyfer"]["skills"] | speakers["Macdonald Graham"]["skills"]
print(f"Unique skills of speakers: {unique_skills}")

participants_in_both = registered_session_participants[
    "Foundations of Machine Learning"] & registered_session_participants["Autonomous Workflows"]
print(f"Participants in Both: {participants_in_both}")

participants_only_for_first = registered_session_participants[
    "Foundations of Machine Learning"] - registered_session_participants["Autonomous Workflows"]
print(f"Participants in First: {participants_only_for_first}")

all_uniqueue_participants = registered_session_participants[
    "Foundations of Machine Learning"] | registered_session_participants["Autonomous Workflows"]
print(f"Participants in First: {all_uniqueue_participants}")


# -----------------------------------------------------
# Part 5: Conference Configurations
email, phone_no = contact_information
start_date, end_date = conference_dates
start_time, end_time = opening_closing_times
print(f"Conference Contact Information: {email} {phone_no}")
print(f"Start date: {start_date}, end date: {end_date}")
print(f"Start Time: {start_time}, end_time: {end_time}")


# ---------------------------------------------------------
# Part 6: Shared Reference Problem

backup_participants = participants
print(f"Original Participants age: {participants["Mahil"]["age"]}")

backup_participants["Mahil"]["age"] = 69
print(f"Backup Participant age update: {backup_participants["Mahil"]["age"]}")
print(
    f"Original participant age after updating Backup participants: {participants["Mahil"]["age"]}")
# Updating in the backup_participants reflected in the participants also.
# Since here we are pointing backup_participants to as same partcipant location update made in the same reference
# To create copy we should use .copy()  which will create new list and we can update independently

print("In Correct way of implementing Backup")
backup_participants = participants.copy()

print(f"Original Participants age: {participants["Mahil"]["age"]}")

backup_participants["Mahil"]["age"] = 80
print(f"Backup Participant age update: {backup_participants["Mahil"]["age"]}")
print(
    f"Original participant age after updating Backup participants: {participants["Mahil"]["age"]}")
