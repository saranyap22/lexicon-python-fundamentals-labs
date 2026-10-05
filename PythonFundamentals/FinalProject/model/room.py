class Room:
    """Represent a bookable Room in a Hotel"""

    def __init__(self, number: str, category: str, area: int, max_guests: int, price: float, is_available: bool = True):
        self.number = number
        self.type = category
        self.area = area
        self.max_guests = max_guests
        self.price = price
        self.is_available = is_available

    def __str__(self):
        return (
            f"Room Number: {self.number} "
            f"Room Type: {self.type} "
            f"Area: {self.area} "
            f"Max Guests: {self.max_guests}"
            f"Price: {self.price}"
        )
