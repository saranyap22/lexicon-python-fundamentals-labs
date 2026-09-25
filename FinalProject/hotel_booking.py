"""Module contains functions that support manging the hotel rooms booking related operations"""


class Hotel:
    def __init__(self, name, rooms=None, contact=None, address=None):
        self.name = name,
        self.rooms = rooms if rooms is not None else []
        self.contact = contact if contact is not None else []
        self.address = address if address is not None else []

    def __str__(self):
        return (
            f"Name: {self.name} "
            f"Rooms: {self.rooms} "
            f"Contact: {self.contact} "
            f"Address: {self.address}"
        )


class Room:
    def __init__(self, number, category, area, max_guests):
        self.number = number
        self.type = category
        self.area = area
        self.max_guests = max_guests

    def __str__(self):
        return (
            f"Room Number: {self.number} "
            f"Room Type: {self.type} "
            f"Area: {self.area} "
            f"Max Guests: {self.max_guests}"
        )


class Guest:
    def __init__(self, name, age, contact, address):
        self.name = name,
        self.age = age,
        self.contact = contact
        self.address = address

    def __str__(self):
        return (
            f"Name: {self.name} "
            f"Age: {self.age} "
            f"Contact: {self.contact} "
            f"Address: {self.address}"
        )


class Booking:
    def __init__(self, room, dates, no_of_guests, guests=None, status="NEW"):
        self.room = room
        self.guests = guests
        self.status = status
        self.dates = dates
        self.no_of_guests = no_of_guests

    def __str__(self):
        return (
            f"Room: {self.room} "
            f"Guests: {self.guests} "
            f"Status: {self.status} "
            f"Dates: {self.dates} "
            f"No Of Guests: {self.no_of_guests}"
        )


class BookingSystem:
    bookings = []

    def create_booking(self, room, dates, no_of_guests, guests):
        booking = Booking(room, dates, no_of_guests, guests, status="NEW")
        self.bookings.append(booking)
        print(f"Created Booking: {booking} and added to Booking List")


booking_system = BookingSystem()
address = "Arvid tydens alle10"
contact = {"email": "mh_hotel@gmail.com", "mobile": "0734333347"}
rooms = {
    Room("101b", "AC", 34, 3),
    Room("10h", "NONAC", 12, 1),
    Room("1k", "AC", 56, 4),
    Room("56l", "NONAC", 23, 2),
    Room("10h", "AC", 20, 2),
    Room("78t", "NONAC", 45, 3),
    Room("98r", "NONAC", 10, 1),
    Room("55f", "AC", 40, 4),
    Room("101c", "NONAC", 34, 3)
}

hotel = Hotel("Hotel Grand Palace", rooms, contact, address)
