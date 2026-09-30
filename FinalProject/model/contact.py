"""Represents contact object"""


class Contact:
    def __init__(self, email, mobile):
        self.email = email
        self.mobile = mobile

    def __str__(self):
        return (
            f"Email: {self.email}\n"
            f"Mobile: {self.mobile}\n"
        )
