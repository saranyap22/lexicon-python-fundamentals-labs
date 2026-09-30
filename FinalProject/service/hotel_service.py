from model.hotel import Hotel


class HotelService:

    hotels = {}

    def create_hotel(self, name, rooms, contact, address, ):
        self.hotels[name] = Hotel(name, rooms, contact, address)

    def find_hotel(self, hotel_name):
        hotel = self.hotels.get(hotel_name)

        if hotel is None:
            raise ValueError("Hotel Not Found")

        return hotel

    def find_room(self, hotel_name, room_number):
        hotel = self.find_hotel(hotel_name)
        rooms = hotel.rooms
        if not rooms:
            raise ValueError("Rooms is Empty")

        for room in rooms:
            if room_number == room.number:
                return room

        raise ValueError("Room not found")

    def add_room_to_hotel(self, hotel_name, room):
        hotel = self.find_hotel(hotel_name)

        hotel.add_room(room)

    def add_rooms_to_hotel(self, hotel_name, rooms):
        hotel = self.find_hotel(hotel_name)
        if not rooms:
            raise ValueError("rooms is empty")

        hotel.add_rooms(rooms)

    def remove_room_from_hotel(self, hotel_name, room):
        room = self.find_room(hotel_name, room)
        hotel = self.find_hotel(hotel_name)
        hotel.remove_room(room)
