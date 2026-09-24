class Device:
    def __init__(self, brand, year, is_active=True):
        self.brand = brand
        if year <= 0:
            raise ValueError("year cannot be negative")
        self.year = year
        self.is_active = is_active


class Laptop(Device):
    def __init__(self, brand, year, ram_gb, is_active):
        super().__init__(brand, year, is_active)
        self.ram_gb = ram_gb


class Monitor(Device):
    def __init__(self, brand, year, resolution, size, is_active):
        super().__init__(brand, year, is_active)
        self.resolution = resolution
        self.size = size


device1 = Laptop("Dell", 2021, 128, True)
# device2 = Laptop("Dell", -9, 128, True) - value error raised during base class init
device3 = Monitor("Lenovo", 2000, "Full HD", 75, False)
print(device1.brand, device1.year, device1.ram_gb, device1.is_active)
print(device3.brand, device3.year, device3.resolution,
      device3.size, device3.is_active)
