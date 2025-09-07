# C3 linearization algorithm/method resolution order(mro)

#1

class A:
    def disA(self):
        print("inside A")
a=A()
a.disA()
print(A.mro)

#2)
class A:
    def disA(self):
        print("inside A")
class B(A):
    def disB(self):
        print("inside B")
b=B()
b.disB()
b.disA()
print(B.mro())

#3
class A:
    def disA(self):
        print("inside A")
class B:
    def disB(self):
        print("inside B")
class C(A,B):
    def disC(self):
        print("inside C")
c1=C()
c1.disC()
c1.disA()
c1.disB()
print(C.mro())