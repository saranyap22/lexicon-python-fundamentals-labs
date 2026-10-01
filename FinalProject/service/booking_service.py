from datetime import datetime
from model.booking import Booking
from model.room import Room
from service.hotel_service import HotelService
from service.room_service import RoomService
from service.guest_service import GuestService


class BookingService:
    bookings: list[Booking] = []

    def __init__(self, hotel_service: HotelService, room_service: RoomService, guest_service: GuestService):
        self.hotel_service = hotel_service
        self.room_service = room_service
        self.guest_service = guest_service

    def create_booking(self, hotel_name: str, room_number: str, start_date: str, end_date: str, no_of_guests: int, guest_name):
        room = self.room_service.find_room(hotel_name, room_number)
        guest = self.guest_service.find_guest(guest_name)

        self.validate_room(start_date, end_date, room)

        booking = Booking(room, start_date, end_date,
                          no_of_guests, guest, status="CONFIRMED")
        self.bookings.append(booking)
        print(f"Created Booking: {booking} and added to Booking List")

    def check_in_booking(self, room_number: str, start_date: str, end_date: str):
        bookings = self.filter_active_booking_by_date(
            self.retrieve_booking_by_room(room_number), start_date, end_date)

        if not bookings:
            raise ValueError("No active Booking not Found")

        for booking in bookings:
            if not booking.is_confirmed():
                raise ValueError(
                    f"Booking status {booking.status} not confirmed")
            booking.check_in(datetime.now())

    def check_out_booking(self, room_number: str, start_date: str, end_date: str):
        bookings = self.filter_active_booking_by_date(
            self.retrieve_booking_by_room(room_number), start_date, end_date)

        for booking in bookings:
            if not booking.is_checked_in():
                raise ValueError(
                    f"Booking status {booking.status} not checked in")
            booking.check_out(datetime.now())

    def validate_room(self, start_date: str, end_date: str, room: Room):
        if room is None:
            raise ValueError(
                "Room is not available in the room list")

        if not room.is_available:
            raise ValueError(f"Room {room.number} is not available to book")

        self.check_availability_for_dates(room, start_date, end_date)

    def retrieve_booking_by_guest(self, guest_name: str):
        return [
            booking
            for booking in self.bookings
            if self.guest_service.find_guest(guest_name) == booking.guest
        ]

    def retrieve_booking_by_room(self, room_number: str):
        return [
            booking
            for booking in self.bookings
            if room_number == booking.room.number
        ]

    def filter_active_booking_by_date(self, filtered_by_room_bookings: list[Booking], start_date: str, end_date: str):
        return [
            booking
            for booking in filtered_by_room_bookings
            if booking.start_date == start_date and booking.end_date == end_date
        ]

    def cancel_booking(self, room_number: str, start_date: str, end_date: str):
        bookings = self.filter_active_booking_by_date(
            self.retrieve_booking_by_room(room_number), start_date, end_date)

        if not bookings:
            raise ValueError("No active Booking not Found")
        for booking in bookings:
            if not booking.is_active():
                raise ValueError(
                    f"Booking status {booking.status} not cancellable")
            booking.cancel()

    def __str__(self):
        return (
            f"Bookings: {booking}"
            for booking in self.bookings
        )

    def check_availability_for_dates(self, room_number: str, start_date: str, end_date: str):
        matched_bookings = self.retrieve_booking_by_room(room_number)

        for booking in matched_bookings:
            if start_date <= booking.end_date and end_date >= booking.start_date:
                raise ValueError(
                    f"Room {booking.room.number} not available, already booked for the requested dates")

    def summary_of_bookings(self):
        print(f"{"Room":10} {"Start Date":^10} {"End Date":^10} {"No Of Guests":^15} {"Status":<15} {"Guests":<10}")
        print("---------------------------------------------------------------------")
        for booking in self.bookings:
            print(f"{booking.room.number:<10}",
                  f"{booking.start_date:^10}"
                  f"{booking.end_date:^10}"
                  f"{booking.no_of_guests:^15}"
                  f"{booking.status:<15}"
                  f"{booking.guest.name:<10}")
