from model.booking import Booking


class BookingService:
    bookings = []

    def __init__(self, hotel_service, room_service):
        self.hotel_service = hotel_service
        self.room_service = room_service

    def create_booking(self, hotel, room_number, start_date, end_date, no_of_guests, guests):
        room = self.room_service.find_room(hotel, room_number)

        if room is None:
            raise ValueError(
                f"Room {room_number} is not available in the room list")

        if not room.is_available:
            raise ValueError(f"Room {room_number} is not available to book")

        self.check_availability_for_dates(room, start_date, end_date)

        booking = Booking(room, start_date, end_date,
                          no_of_guests, guests, status="NEW")
        self.bookings.append(booking)
        print(f"Created Booking: {booking} and added to Booking List")

    def retrieve_booking_by_guest(self, guest):
        return [
            booking
            for booking in self.bookings
            if guest in booking.guests
        ]

    def retrieve_booking_by_room(self, room):
        return [
            booking
            for booking in self.bookings
            if room == booking.room
        ]

    def retrieve_active_booking_by_date(self, room, start_date, end_date):
        return [
            booking
            for booking in self.bookings
            if booking.start_date == start_date and booking.end_date == end_date and booking.status != "CANCELLED"
        ]

    def cancel_booking(self, room, start_date, end_date):
        booking = self.retrieve_active_booking_by_date(
            self.retrieve_booking_by_room(room), start_date, end_date)
        if booking:
            booking.status = "CANCELLED"

    def __str__(self):
        return (
            f"Bookings: {booking}"
            for booking in self.bookings
        )

    def check_availability_for_dates(self, room, start_date, end_date):
        matched_bookings = self.retrieve_booking_by_room(room)

        for booking in matched_bookings:
            if start_date < booking.end_date or end_date > booking.start_date:
                raise ValueError(
                    f"Room {room.number} not available, already booked for the requested dates")

    def summary_of_bookings(self):
        for booking in self.bookings:
            print(f"Room: {booking.room} \n",
                  f"Start Date: {booking.start_date} \n"
                  f"End Date: {booking.end_date} \n"
                  f"No of Guests: {booking.no_of_guests} \n"
                  f"Guests: {booking.guests} \n")
