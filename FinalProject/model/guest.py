class Guest:
    """Represent a Guest in a Booking"""

    def __init__(self, name, age, contact, address):
        self.name = name
        self.age = age
        self.contact = contact
        self.address = address

    def __str__(self):
        return (
            f"Name: {self.name} "
            f"Age: {self.age} "
            f"Contact: {self.contact} "
            f"Address: {self.address}"
        )

    def __repr__(self):
        return (
            f"Name={self.name!r}"
            f"Age={self.age!r}"
            f"Contact={self.contact!r}"
            f"Address={self.address!r}"
        )
