"""Represents contact object"""


class Contact:
    def __init__(self, email: str, mobile: str):
        self.email = email
        self.mobile = mobile

    def __str__(self):
        return (
            f"Email: {self.email} "
            f"Mobile: {self.mobile} "
        )

    def __repr__(self):
        return (
            f"Email: {self.email!r}"
            f"Mobile: {self.mobile!r}"
        )
