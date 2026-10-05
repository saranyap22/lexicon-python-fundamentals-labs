""" Module to explore Sets"""

# sets use
courses = ["Python", "Java", "C#", "Java"]
courses_set = set(courses)
print(f"List: {courses} and Set: {courses_set}")

# Union, intersection and difference
developer_one_skills = {"Java", "Python", "SQL"}
developer_two_skills = {"DevOps", "Python", "C#", "SQL"}

print(f"Union | : {developer_one_skills | developer_two_skills}")
print(f"Intersection & : {developer_one_skills & developer_two_skills}")
print(f"Difference - : {developer_one_skills - developer_two_skills}")
print(f"Difference - : {developer_two_skills - developer_one_skills}")

# Methods in sets
courses = {"Python", "Java", "C#", "Java"}
courses.add("DevOps")
print(f"Add to set: {courses}")
# courses.remove("Perl")  # Throws Keyerror if element does not exist
courses.remove("C#")
print(f"Remove from set: {courses}")
courses.discard("C#")  # Does not raise exception if element does not exist
