from model.room import Room


class RoomService:

    def __init__(self, hotel_service):
        self.hotel_service = hotel_service

    def create_room(self, number, category, area, max_guests, price):
        return Room(number, category, area, max_guests, price)

    def update_room(self, hotel, number, area, max_guests, price):
        room = self.find_room(hotel, number)
        room.area = area
        room.max_guests = max_guests
        room.price = price

    def find_room(self, hotel, number):
        return self.hotel_service.find_room(hotel, number)
