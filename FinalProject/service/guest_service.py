"""Represent Guest object"""
from model.guest import Guest


class GuestService:

    guests = {}

    def create_guest(self, name, age, contact, address):
        self.guests[name] = Guest(name, age, contact, address)

    def update_guest(self, name, age=None, contact=None, address=None):
        guest = self.find_guest(name)

        if age is not None:
            guest.age = age
        if contact is not None:
            guest.contact = contact
        if address is not None:
            guest.address = address

    def find_guest(self, name):
        guest = self.guests.get(name)

        if guest is None:
            raise ValueError("Guest doest not exist")

        return guest

    def get_all_guest_names(self, guests):
        return [guest.name for guest in guests]
