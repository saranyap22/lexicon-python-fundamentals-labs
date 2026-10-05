# -------------------------------------------------------
# Wrong way: mutable Default argument initialization: Pythonic pitfalls
class BadTeam:

    # Not Preferred. Default arguments initialized only once and shared by objects.
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add_member(self, member):
        self.members.append(member)


bad_team1 = BadTeam("Woo")
bad_team1.add_member("Nisha")
bad_team1.add_member("Aana")

print(bad_team1.name, bad_team1.members)

bad_team2 = BadTeam("Hoo")
bad_team2.add_member("Vicky")
bad_team2.add_member("Meha")

# members attributes shared between object. bad_team2.members has include 4 members 2 member from bad_team1
print(bad_team2.name, bad_team2.members)


# -----------------------------------------------
# Correct way of implementing mutable default arguments

class Team:

    # Preferred.  Mutable default argument of members set to None
    # Default arguments initialized when default arguments is None received anything for each object.
    def __init__(self, name, members=None):
        self.name = name
        if members is None:
            self.members = []
        else:
            self.members = members

    def add_member(self, member):
        self.members.append(member)


team1 = Team("Joo")
team1.add_member("Jill")
team1.add_member("Anky")

print(team1.name, team1.members)

team2 = Team("Foo")
team2.add_member("Vicky")
team2.add_member("Meha")

# members attributes creates for each object. team2 only has added members of team
print(team2.name, team2.members)
