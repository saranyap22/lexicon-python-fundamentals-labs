import requests

# response = requests.get("https://api.github.com/users/octocat")

# print(response.headers["X-RateLimit-Limit"])
# print(response.headers["X-RateLimit-Remaining"])


# response = requests.get("https://api.github.com/user")

# print(response.status_code)
# print(response.json())

# -----------------------------------------------------

# AUTHORIZATION

# headers = {"Authorization": "Bearer This is fake token"}
# response = requests.get("https://api.github.com/user", headers=headers)
# print(response.json())
# print(response.status_code)

# -----------------------------------------------------

# Reading token from .env file

# import os
# from dotenv import load_dotenv

# token = os.getenv("GITHUB_TOKEN")
# headers = {"Authorization": f"Bearer {token}"}
# response = requests.get("https://api.github.com/user", headers=headers)
# print(response.status_code)
# print(response.json()["login"])
