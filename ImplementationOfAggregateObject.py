class Charger:

    def __init__(self, name):
        self.cname = name
        print("Charger is ready")

    def getCharger(self):
        print("Chaarger is used for charging")

class Mobile:

    def __init__(self, name):
        self.mname = name
        self.c1 = " "
        print("Mobile is ready")

    def hasMobile(self, x):
        self.c1 = x
        print("Both mobile and Charger connected")

m= Mobile("Vivo")
charge = Charger("Vivo's Charger") 
m.hasMobile(charge)
print(m.mname)
print(m.c1.cname)
m.c1.getCharger()

del m
print("After Deleting")
m.hasMobile(charge)
print(m.mname)
print(m.c1.cname)
m.c1.getCharger()

print(charge.cname)
charge.getCharger()