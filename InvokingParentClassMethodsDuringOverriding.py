class A:
    def display(self):
        print("Inside A")

class B:
    def display(self):
        print("Inside B")

class C:
    def display(self):
        print("Inside c")

class D(C):
    def dispD(self):
        A.display(self)
        B.display(self)
        C.display(self)

d1 = D()
d1.dispD()