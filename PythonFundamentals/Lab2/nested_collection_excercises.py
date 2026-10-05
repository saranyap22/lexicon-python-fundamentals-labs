""" Module to explore nested collections"""
books = [
    {"title": "Java Programming", "author": "saranya",
        "pages": 100, "available": True},
    {"title": "Python Programming", "author": "bob",
        "pages": 240, "available": False},
    {"title": "C# Programming", "author": "Anna", "pages": 459, "available": True},
    {"title": "AI", "author": "saranya", "Victor": 800, "available": False},
]

print(books[2]["title"])
print(books[-1]["available"])

books[1]["author"] = "Bobb"
print(books[1]["author"])

books[2]["version"] = "2.0"
print(books[2]["version"])

# create list within dictionary
departments = {
    "production": ["Anna", "Carter", "Martin"],
    "transport": ["Leo", "Victer", "Kiran"],
    "planning": ["Neo", "Raj", "saranya"],
}
print(departments)

# Create data with nested data structures

courses = [
    {"name": "Python", "teacher": "Anna", "topics": [
        "variables", "list", "tuples", "dict", "set"]},
    {"name": "Java", "teacher": "Hussain", "topics": [
        "variables", "list", "map", "set"]},
    {"name": "Project Management", "teacher": "Erik", "topics": [
        "Project Management Essentials", "Agile", "Risk assessment", "Resource allocation"]},
    {"name": "Web Developement", "teacher": "Martin", "topics": [
        "HTML", "CSS", "Javascript", "Design"]}
]

print(courses[3]["topics"][-1])
