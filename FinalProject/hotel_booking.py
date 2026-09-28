"""Module for simulating Hotel Booking system"""
from service.hotel_service import HotelService
from service.room_service import RoomService
from service.booking_service import BookingService
from model.guest import Guest


hotel_service = HotelService()
booking_service = BookingService()
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

booking_service.create_booking(
    hotel, "101c", "26-9-2026", "27-9-2026", 1, [guest])

booking_service.retrieve_booking_by_guest(guest)

booking_service.summary_of_bookings()
