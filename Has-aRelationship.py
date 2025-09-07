# Has-a Relationship

class Radio:

    def turnOn(self, x):
        if (x == 1):
            print("Radio is On")
        else:
            print("Radio is Off")

class car:

    def __init__(self, min, max):

        self.min = min
        self.max = max
        self.r = Radio()

c = car(60, 120)
print(c.min)
print(c.min)
c.r.turnOn(1)
c.r.turnOn(2)