"""Module contains functions that support manging the hotel rooms booking related operations"""


class Hotel:
    """Represent a Hotel """

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

    def add_room(self, room):
        self.rooms.append(room)

    def update_hotel(self, name, contact, address):
        hotel.address = address
        hotel.contact = contact


class Room:
    """Represent a bookable Room in a Hotel"""

    def __init__(self, number, category, area, max_guests, price):
        self.number = number
        self.type = category
        self.area = area
        self.max_guests = max_guests
        self.price = price

    def __str__(self):
        return (
            f"Room Number: {self.number} "
            f"Room Type: {self.type} "
            f"Area: {self.area} "
            f"Max Guests: {self.max_guests}"
            f"Price: {self.price}"
        )


class Guest:
    """Represent a Guest in a Booking"""

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

    def __repr__(self):
        return f"Guest(name={self.name!r},age={self.age!r},contact={self.contact!r},address={self.address!r})"


class Booking:
    """Represent a Booking"""

    def __init__(self, room, dates, no_of_guests, guests=None, status="NEW"):
        self.room = room
        self.guests = guests
        self.status = status
        self.dates = dates
        self.no_of_guests = no_of_guests

    def __str__(self):
        return (
            f"Room: {self.room} \n"
            f"Guests: {self.guests} \n"
            f"Status: {self.status} \n"
            f"Dates: {self.dates} \n"
            f"No Of Guests: {self.no_of_guests}"
        )


class RoomService:

    def create_room(self, number, category, area, max_guests, price):
        return Room(number, category, area, max_guests, price)

    def update_room(self, hotel, number, area, max_guests, price):
        room = self.find_room(hotel, number)
        room.area = area
        room.max_guests = max_guests
        room.price = price
        return room

    def find_room(self, hotel, number):
        for room in hotel.rooms:
            if number == room.number:
                return room


class HotelService:

    def create_hotel(self, name, rooms, contact, address):
        return Hotel(name, rooms, contact, address)


class BookingService:
    bookings = []

    def create_booking(self, room, dates, no_of_guests, guests):
        booking = Booking(room, dates, no_of_guests, guests, status="NEW")
        self.bookings.append(booking)
        print(f"Created Booking: {booking} and added to Booking List")

    def retrieve_booking(self, guest):
        for booking in self.bookings:
            if guest in booking.guests:
                print(f"Booking: {booking}")

    def __str__(self):
        return (
            f"Bookings: {booking}"
            for booking in self.bookings
        )


hotel_service = HotelService()
booking_system = BookingService()
room_service = RoomService()
address = "Arvid tydens alle10"
hotel_contact = {"email": "mh_hotel@gmail.com", "mobile": "0734333347"}
rooms = set()
rooms.add(room_service.create_room("101b", "AC", 34, 3, 2000.00))
rooms.add(room_service.create_room("10h", "NONAC", 12, 1, 1675.00))
rooms.add(room_service.create_room("1k", "AC", 56, 4, 4900.50))
rooms.add(room_service.create_room("56l", "NONAC", 23, 2, 900.88))
rooms.add(room_service.create_room("10h", "AC", 20, 2, 600))
rooms.add(room_service.create_room("78t", "NONAC", 45, 3, 4500.65))
rooms.add(room_service.create_room("98r", "NONAC", 10, 1, 300.00))
rooms.add(room_service.create_room("55f", "AC", 40, 4, 1400.78))
rooms.add(room_service.create_room("101c", "NONAC", 34, 3, 1500.00))


hotel = hotel_service.create_hotel(
    "Hotel Grand Palace", rooms, hotel_contact, address)
guest_contact = {"email": "grace@gmail.com", "mobile": "0756543423"}
guest = Guest("Grace", 25, guest_contact, "Diktarvagen 11")

room_service.update_room(hotel, "101c", 13, 2, 1500.00)
print(room_service.find_room(hotel, "101c"))

booking_system.create_booking("101c", ("26-9-2026", "27-9-2026"), 1, [guest])

for booking in booking_system.bookings:
    print("Booking:", booking)

booking_system.retrieve_booking(guest)
