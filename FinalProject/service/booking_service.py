from model.booking import Booking
from datetime import datetime


class BookingService:
    bookings = []

    def __init__(self, hotel_service, room_service, guest_service):
        self.hotel_service = hotel_service
        self.room_service = room_service
        self.guest_service = guest_service

    def create_booking(self, hotel, room_number, start_date, end_date, no_of_guests, guest_name):
        room = self.room_service.find_room(hotel, room_number)
        guest = self.guest_service.find_guest(guest_name)

        self.validate_room(room_number, start_date, end_date, room)

        booking = Booking(room, start_date, end_date,
                          no_of_guests, [guest], status="CONFIRMED")
        self.bookings.append(booking)
        print(f"Created Booking: {booking} and added to Booking List")

    def check_in_booking(self, room, start_date, end_date):
        bookings = self.filter_active_booking_by_date(
            self.retrieve_booking_by_room(room), start_date, end_date)

        if not bookings:
            raise ValueError("No active Booking not Found")

        for booking in bookings:
            if not booking.is_confirmed():
                raise ValueError(
                    f"Booking status {booking.status} not confirmed")
            booking.check_in(datetime.now())

    def check_out_booking(self, room, start_date, end_date):
        bookings = self.filter_active_booking_by_date(
            self.retrieve_booking_by_room(room), start_date, end_date)

        for booking in bookings:
            if not booking.is_checked_in():
                raise ValueError(
                    f"Booking status {booking.status} not checked in")
            booking.check_out(datetime.now())

    def validate_room(self, room_number, start_date, end_date, room):
        if room is None:
            raise ValueError(
                f"Room {room_number} is not available in the room list")

        if not room.is_available:
            raise ValueError(f"Room {room_number} is not available to book")

        self.check_availability_for_dates(room, start_date, end_date)

    def retrieve_booking_by_guest(self, guest_name):
        return [
            booking
            for booking in self.bookings
            if self.guest_service.find_guest(guest_name) in booking.guests
        ]

    def retrieve_booking_by_room(self, room_number):
        return [
            booking
            for booking in self.bookings
            if room_number == booking.room.number
        ]

    def filter_active_booking_by_date(self, filtered_by_room_bookings, start_date, end_date):
        return [
            booking
            for booking in filtered_by_room_bookings
            if booking.start_date == start_date and booking.end_date == end_date
        ]

    def cancel_booking(self, room, start_date, end_date):
        bookings = self.filter_active_booking_by_date(
            self.retrieve_booking_by_room(room), start_date, end_date)

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

    def check_availability_for_dates(self, room, start_date, end_date):
        matched_bookings = self.retrieve_booking_by_room(room)

        for booking in matched_bookings:
            if start_date <= booking.end_date and end_date >= booking.start_date:
                raise ValueError(
                    f"Room {booking.room.number} not available, already booked for the requested dates")

    def summary_of_bookings(self):
        print(f"{"Room":10} {"Start Date":^10} {"End Date":^10} {"No Of Guests":^3} {"Status":<10} {"Guests":<10}")
        print("---------------------------------------------------------------------\n")
        for booking in self.bookings:
            print(f"{booking.room.number}",
                  f"{booking.start_date:^10}"
                  f"{booking.end_date:^10}"
                  f"{booking.no_of_guests:^3}"
                  f"{booking.status:<10}"
                  f"{self.guest_service.get_all_guest_names(booking.guests)}")
