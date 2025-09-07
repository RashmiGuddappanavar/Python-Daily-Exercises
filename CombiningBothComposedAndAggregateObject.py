#combining both composed and aggregate object

class car:
    def __init__(self,name):
        self.cname=name
        print("car is ready")
    def getcar(self):
        print("car is used for driving")
class heart:
    def __init__(self):
        self.status=True
        print("heart is ready")
    def getheart(self):
        print("heart is waiting")
class person:
    def __init__(self,name):
        self.pname=name
        self.h=heart()
        self.c1=" "
        print("person is ready")
    def hasperson(self,c):
        self.c1=c
        print("person is using car for long drive")
p=person("rama")
ca=car("Thar")
p.hasperson(ca)
print(p.pname)
print(p.h.status)
print(p.c1.cname)
p.c1.getcar()
p.h.getheart()
del p
print("after deleting")
print(p.h.status)
p.h.getheart()
print(ca.cname)
ca.getcar()