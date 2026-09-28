from model.room import Room


class RoomService:

    def create_room(self, number, category, area, max_guests, price):
        return Room(number, category, area, max_guests, price)

    def update_room(self, hotel, number, area, max_guests, price):
        room = self.find_room(hotel, number)
        room.area = area
        room.max_guests = max_guests
        room.price = price
        return room

    def find_room(self, hotel, number):
        for room in hotel.rooms:
            if number == room.number:
                return room
