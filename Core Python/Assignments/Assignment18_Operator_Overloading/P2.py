class Distance:

    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm

    def __del__(self):
        print("Object destroyed")

    def __add__(self, other):
        cm = self.cm + other.cm
        m = self.m + other.m
        km = self.km + other.km

        if cm >= 100:
            m = m + cm // 100
            cm = cm % 100

        if m >= 1000:
            km = km + m // 1000
            m = m % 1000

        return Distance(km, m, cm)

    def __sub__(self, other):
        d1 = self.km * 100000 + self.m * 100 + self.cm
        d2 = other.km * 100000 + other.m * 100 + other.cm

        diff = abs(d1 - d2)

        km = diff // 100000
        m = (diff % 100000) // 100
        cm = diff % 100

        return Distance(km, m, cm)

    def display(self):
        print(self.km, "km", self.m, "m", self.cm, "cm")


d1 = Distance(2, 500, 80)
d2 = Distance(1, 600, 50)

d3 = d1 + d2
d4 = d1 - d2

print("Addition:")
d3.display()

print("Subtraction:")
d4.display()