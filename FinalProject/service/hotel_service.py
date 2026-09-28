from model.hotel import Hotel


class HotelService:

    def create_hotel(self, name, rooms, contact, address):
        return Hotel(name, rooms, contact, address)
