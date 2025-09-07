class OS:
    def __init__(self):
        self.status = True
        print("OS is ready")

    def getOS(self):
        print("OS is still executing")

class Mobile:
    def __init__(self, name):
        self.mname = name  
        self.o = OS()

        print("Mobile is ready")
        print("With OS installed")

m = Mobile("Vivo")
print(m.mname)
print(m.o.status)
m.o.getOS()

del m
print("After Deleting")
print(m.mname)
print(m.o.status)
m.o.getOS()