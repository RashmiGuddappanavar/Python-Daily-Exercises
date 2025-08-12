# a = 10

# def fun1():
#     a = 100
#     print(a)
#     b = 20
#     print(b)

# def fun2():
#     a = 1000
#     print(a)
#     c = 30
#     print(c)

# print(a)
# fun1()
# print(a)
# print(fun2) # <function fun2 at 0x000001638073C0E0>
# print(a)

# Accessing the gloabal variable and modifying local variable as the global variable

a = 10

def fun1():
    global a 
    a = 100
    print(a)
    b = 20
    print(b)

def fun2():
    global a 
    a = 1000
    print(a)
    c = 30
    print(c)

print(a)
fun1()
print(a)
fun2()
print(a)