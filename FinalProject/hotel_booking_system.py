from model.contact import Contact
from service.hotel_service import HotelService
from service.room_service import RoomService
from service.guest_service import GuestService
from service.booking_service import BookingService

# ----------------------------------------
# Simulate creating holtel

print("Welcome to Hotel Grand Palace")

hotel_service = HotelService()
address = "Arvid tydens alle10"
hotel_contact = Contact("mh_hotel@gmail.com", "0734333347")
hotel_name = "Hotel Grand Palace"
hotel_service.create_hotel(
    hotel_name, rooms=None, contact=hotel_contact, address=address)

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
guest_service = GuestService()

guest_contact = Contact("grace@gmail.com", "0756543423")
guest_name = "Grace"
guest_service.create_guest(guest_name, 25, guest_contact, "Diktarvagen 11")
print("Guest Information: ", guest_service.guests)

# --------------------------------------------------------
# Booking System Simulation

booking_service = BookingService(hotel_service, room_service, guest_service)

while (True):
    print("\n\n")
    print("1. Display Room Information")
    print("2. Book a room")
    print("3. Check-in room")
    print("4. Check-out room")
    print("5. Cancel a Booking")
    print("6. Booking Summary")
    print("7. Close")

    choice = input("Choose an option: ")

    if choice == "7":
        break

    if choice == "2":
        room_number = input("Enter Room Number: ")
        start_date = input("Enter Start date (dd-mm-yyyy): ")
        end_date = input("Enter End date (dd-mm-yyyy): ")
        no_of_guests = int(input("Enter Number of Guests: "))
        try:
            booking_service.create_booking(
                hotel_name, room_number, start_date, end_date, no_of_guests, guest_name)
        except ValueError as error:
            print(f"Error: {error}")

    if choice == "3":
        room_number = input("Enter Room Number: ")
        start_date = input("Enter Start date (dd-mm-yyyy): ")
        end_date = input("Enter End date (dd-mm-yyyy): ")
        try:
            booking_service.check_in_booking(room_number, start_date, end_date)
        except ValueError as error:
            print(f"Error: {error}")

    if choice == "4":
        room_number = input("Enter Room Number: ")
        start_date = input("Enter Start date (dd-mm-yyyy): ")
        end_date = input("Enter End date (dd-mm-yyyy): ")
        try:
            booking_service.check_out_booking(
                room_number, start_date, end_date)
        except ValueError as error:
            print(f"Error: {error}")

    if choice == "5":
        room_number = input("Enter Room Number: ")
        start_date = input("Enter Start date (dd-mm-yyyy): ")
        end_date = input("Enter End date (dd-mm-yyyy): ")
        try:
            booking_service.cancel_booking(
                room_number, start_date, end_date)
        except ValueError as error:
            print(f"Error: {error}")

    if choice == "6":
        booking_service.summary_of_bookings()
