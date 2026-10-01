from datetime import datetime
from model.room import Room
from model.guest import Guest
from model.booking_status import BookingStatus


class Booking:
    """Represent a Booking"""

    def __init__(self, room: Room, start_date: str, end_date: str, no_of_guests: int, guest: Guest | None = None):
        if room is None:
            raise ValueError("Room is Required")
        if not start_date or not end_date:
            raise ValueError("start_date and end_date is required")
        if datetime.strptime(start_date, "%d-%m-%Y").date() > datetime.strptime(end_date, "%d-%m-%Y").date():
            raise ValueError("start_date must be before end_date")
        if no_of_guests <= 0:
            raise ValueError("no_of_guests must be greater than 0")
        if no_of_guests > room.max_guests:
            raise ValueError(
                f"no_of_guests exceeds room capacity ({room.max_guests})")
        if guest is None:
            raise ValueError("Guest is required")
        self.room = room
        self.guest = guest
        self.start_date = start_date
        self.end_date = end_date
        self.no_of_guests = no_of_guests
        self.checked_in_time = None
        self.checked_out_time = None
        self.status = None

    def __str__(self):
        return (
            f"Room: {self.room} "
            f"Guests: {self.guest} "
            f"Status: {self.status} "
            f"Dates: {self.start_date} "
            f"Dates: {self.end_date} "
            f"No Of Guests: {self.no_of_guests}"
        )

    def is_active(self):
        return self.status in (BookingStatus.CONFIRMED,)

    def is_confirmed(self):
        return self.status in (BookingStatus.CONFIRMED,)

    def confirm(self):
        self.status = BookingStatus.CONFIRMED

    def is_checked_in(self):
        return self.status in (BookingStatus.CHECKED_IN,)

    def cancel(self):
        self.status = BookingStatus.CANCELLED

    def check_in(self, checked_in_time):
        self.status = BookingStatus.CHECKED_IN
        self.checked_in_time = checked_in_time

    def check_out(self, checked_out_time):
        self.status = BookingStatus.CHECKED_OUT
        self.checked_out_time = checked_out_time
