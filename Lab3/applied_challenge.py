""" Console Study Tracker"""

study_sessions = [
    {"subject": "Maths", "minutes": 49},
    {"subject": "Physics", "minutes": 80},
    {"subject": "Chemistry", "minutes": 20},
    {"subject": "Biology", "minutes": 45},
    {"subject": "ComputerScience", "minutes": 49},
    {"subject": "Biology", "minutes": 5},
    {"subject": "Maths", "minutes": 10},
    {"subject": "Maths", "minutes": 49},
    {"subject": "Finance", "minutes": 30},
    {"subject": "Physics", "minutes": 15}
]

while (True):

    print("1. View all sessions")
    print("2. View total time")
    print("3. Filter by subject")
    print("4. Longest session")
    print("5. Longer than 45 min session")
    print("6. Quit")
    choice = input(f"Coose an option : ")

    if choice == "6":
        break

    elif choice == "1":
        for index, session in enumerate(study_sessions):
            print(f"{index}: {session["subject"]} : {session["minutes"]}")

    elif choice == "2":
        total_minutes = 0
        for session in study_sessions:
            total_minutes += session.get("minutes", 0)
        print(f"Total study minutes: {total_minutes}")

    elif choice == "3":
        while True:
            subject = input("Enter the subject to view total time or 'Quit': ")
            if subject == 'Quit':
                break
            total = 0
            for session in study_sessions:
                if session.get("subject") == subject:
                    total += session.get("minutes")

            print(total if total else "No sessions found")

    elif choice == '4':
        longest_session = {}
        longest_session_minutes = 0

        for session in study_sessions:
            minutes = session.get("minutes", 0)
            if minutes > longest_session_minutes:
                longest_session_minutes = minutes
                longest_session = session
        print(
            f"Longest Session: Subject: {longest_session.get("subject")}, minutes: {longest_session.get("minutes")}")

    elif choice == '5':
        session_longer_than_45_minutes = []
        for session in study_sessions:
            minutes = session.get("minutes", 0)
            if minutes > 45:
                session_longer_than_45_minutes.append(session)
        print(
            f"Sessions in Longer than 45 minutes: {session_longer_than_45_minutes}")
