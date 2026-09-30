"""Represent Guest object"""
from model.guest import Guest


class GuestService:

    guests = {}

    def create_guest(self, name, age, contact, address):
        self.guests[name] = Guest(name, age, contact, address)

    def update_guest(self, name, age, contact, address):
        guest = self.guests.get(name)

        if self.guests.get(name) is None:
            raise ValueError("Guest doest not exist")

        guest.age = age
        guest.contact = contact
        guest.address = address
