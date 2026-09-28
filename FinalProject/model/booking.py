class Booking:
    """Represent a Booking"""

    def __init__(self, room, start_date, end_date, no_of_guests, guests=None, status="NEW"):
        self.room = room
        self.guests = guests
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        self.no_of_guests = no_of_guests

    def __str__(self):
        return (
            f"Room: {self.room} \n"
            f"Guests: {self.guests} \n"
            f"Status: {self.status} \n"
            f"Dates: {self.start_date} \n"
            f"Dates: {self.end_date} \n"
            f"No Of Guests: {self.no_of_guests}"
        )
