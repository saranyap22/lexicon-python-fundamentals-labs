class Hotel:
    """Represent a Hotel """

    def __init__(self, name, rooms=None, contact=None, address=None):
        self.name = name
        self.rooms = rooms if rooms is not None else set()
        self.contact = contact if contact is not None else []
        self.address = address if address is not None else []

    def __str__(self):
        return (
            f"Name: {self.name} "
            f"Rooms: {self.rooms} "
            f"Contact: {self.contact} "
            f"Address: {self.address}"
        )

    def add_room(self, room):
        self.rooms.add(room)

    def add_rooms(self, rooms):
        self.rooms.update(rooms)

    def update_hotel(self, name, contact, address):
        self.address = address
        self.contact = contact

    def remove_room(self, room):
        self.rooms.remove(room)
