# Python supports for OOP, Script, functionality
#         has
# Object ------> Properties/ Variables

#         does
# Object ------> Behaviour/ Method

# Method Types:
# 1. Instance method
# 2. Static method
# 3. class method

class Calculator:
    def __init__(self):
        self.a = 10
        self.b = 20

    def add(self):
        z = 0
        x = 100
        y = 200
        z = x + y
        print("Sum is", z)

c1 = Calculator()
print(c1.a)
print(c1.b)

c1.add()







