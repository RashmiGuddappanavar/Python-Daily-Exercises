# Function Overloading - The process of declaring 2 or more functions with the same name but different number of parameters is reffered to as function overloading

# Python doesn't suppourt function Overlaoding

# In python, we can declare 2 or more functions with the same name and same number of paramerters. In this case, it will consider the last declared function for execution

# def fun1():
#     print("Inside first fun")
# def fun1(a):
#     print("Inside 2nd fun")
# def fun1(a, b):
#     print("Inside 3rd fun")
# def fun1(a, b, c):
#     print("Inside 4th fun")       
# fun1()  



def fun1():
    print("Inside first fun")
def fun1():
    print("Inside 2nd fun")
def fun1():
    print("Inside 3rd fun")
def fun1():
    print("Inside 4th fun")       
fun1() 
