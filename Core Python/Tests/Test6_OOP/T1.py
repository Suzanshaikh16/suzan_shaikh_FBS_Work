from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, persons):
        self.persons = persons

    @abstractmethod
    def toll(self):
        pass


class TwoWheeler(Vehicle):
    def toll(self):
        extra = max(0, self.persons - 2) * 10
        return 20 + extra


class ThreeWheeler(Vehicle):
    def toll(self):
        extra = max(0, self.persons - 3) * 20
        return 30 + extra


class FourWheeler(Vehicle):
    def toll(self):
        extra = max(0, self.persons - 4) * 40
        return 40 + extra


class HeavyVehicle(Vehicle):
    def toll(self):
        extra = max(0, self.persons - 6) * 100
        return 60 + extra


# Main program
while True:
    print("\n1. Two Wheeler")
    print("2. Three Wheeler")
    print("3. Four Wheeler")
    print("4. Heavy Vehicle")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 5:
        break

    if ch < 1 or ch > 4:
        print("Invalid choice")
        continue

    persons = int(input("Enter number of persons: "))

    if persons <= 0:
        print("Invalid number of persons")
        continue

    if ch == 1:
        v = TwoWheeler(persons)
    elif ch == 2:
        v = ThreeWheeler(persons)
    elif ch == 3:
        v = FourWheeler(persons)
    else:
        v = HeavyVehicle(persons)

    print("Total Toll = Rs.", v.toll())