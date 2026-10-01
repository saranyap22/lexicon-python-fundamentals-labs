from model.room import Room
from model.guest import Guest


class Booking:
    """Represent a Booking"""

    def __init__(self, room: Room, start_date: str, end_date: str, no_of_guests: int, guest: Guest | None = None, status="UNKNOWN"):
        self.room = room
        self.guest = guest
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        self.no_of_guests = no_of_guests
        self.checked_in_time = None
        self.checked_out_time = None

    def __str__(self):
        return (
            f"Room: {self.room} \n"
            f"Guests: {self.guest} \n"
            f"Status: {self.status} \n"
            f"Dates: {self.start_date} \n"
            f"Dates: {self.end_date} \n"
            f"No Of Guests: {self.no_of_guests}"
        )

    def is_active(self):
        return self.status in ("RESERVED", "CONFIRMED")

    def is_confirmed(self):
        return self.status in ("CONFIRMED")

    def is_checked_in(self):
        return self.status in ("CHECKED_IN")

    def cancel(self):
        self.status = "CANCELLED"

    def check_in(self, checked_in_time):
        self.status = "CHECKED_IN"
        self.checked_in_time = checked_in_time

    def check_out(self, checked_out_time):
        self.status = "CHECKED_OUT"
        self.checked_out_time = checked_out_time
