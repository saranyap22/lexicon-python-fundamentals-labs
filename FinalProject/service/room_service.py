from model.room import Room


class RoomService:

    def __init__(self, hotel_service):
        self.hotel_service = hotel_service

    def create_room(self, room_number, category, area, max_guests, price):
        return Room(room_number, category, area, max_guests, price)

    def update_room(self, hotel_name, room_number, area, max_guests, price):
        room = self.find_room(hotel_name, room_number)
        room.area = area
        room.max_guests = max_guests
        room.price = price
        return room

    def find_room(self, hotel_name, number):
        return self.hotel_service.find_room(hotel_name, number)
