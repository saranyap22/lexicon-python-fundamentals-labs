"""Module for simulating Hotel Booking system"""
from service.hotel_service import HotelService
from service.room_service import RoomService
from service.booking_service import BookingService
from model.guest import Guest
from model.contact import Contact

# ----------------------------------------
# Simulate creating holtel
hotel_service = HotelService()

address = "Arvid tydens alle10"
hotel_contact = Contact("mh_hotel@gmail.com", "0734333347")
hotel_service.create_hotel(
    "Hotel Grand Palace", rooms=None, contact=hotel_contact, address=address)

# ----------------------------------------
# Simulate creating rooms
room_service = RoomService(hotel_service)
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
hotel_service.add_rooms_to_hotel("Hotel Grand Palace", rooms)

# ----------------------------------------
# Simulate creating guest
guest_contact = Contact("grace@gmail.com", "0756543423")
guest = Guest("Grace", 25, guest_contact, "Diktarvagen 11")


# ----------------------------------------
# Simulate creating Booking

booking_service = BookingService(hotel_service, room_service)

booking_service.create_booking("Hotel Grand Palace",
                               "101c", "26-9-2026", "27-9-2026", 1, [guest])

booking_service.retrieve_booking_by_guest(guest)

booking_service.summary_of_bookings()


# ----------------------------------------
# Simulate update Booking
room_service.update_room("Hotel Grand Palace", "101c", 13, 2, 1500.00)
print(room_service.find_room("Hotel Grand Palace", "101c"))
