# Inheritence or composition
class CPU:
    def __init__(self, model):
        self.model = model


class Computer:
    def __init__(self, brand, cpu):
        self.brand = brand
        self.cpu = cpu


# Computer Has a CPU - "HAS - A relationship".
# Computer is not a type of CPU .so no inheritence or shared attributes

cpu = CPU("Intel")
computer = Computer("Dell", cpu)
print(computer.brand, computer.cpu.model)


# --------------------------------------------------

# Car / Engine  - Car HAS-A Engine
# Manager/Employee - Manager IS-A Employee
# Course/ Teacher - Course HAS-A Teacher
# Phone/ Device - Phone IS-A Device
