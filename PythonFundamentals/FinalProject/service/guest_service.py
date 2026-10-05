"""Represent Guest object"""
from model.guest import Guest
from model.contact import Contact


class GuestService:

    guests: dict[str, Guest] = {}

    def create_guest(self, name: str, age: int, contact: Contact, address: str):
        self.guests[name] = Guest(name, age, contact, address)

    def update_guest(self, name: str, age: int | None = None, contact: Contact | None = None, address: str | None = None):
        guest = self.find_guest(name)

        if age is not None:
            guest.age = age
        if contact is not None:
            guest.contact = contact
        if address is not None:
            guest.address = address

    def find_guest(self, name: str):
        guest = self.guests.get(name)

        if guest is None:
            raise ValueError("Guest doest not exist")

        return guest
