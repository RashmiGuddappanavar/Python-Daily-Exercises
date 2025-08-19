# Local Scope

# x = 10
# def fun1():
#     x = 15

#     def fun2():
#         x = 20
#         print(x)

#     fun2() 
# fun1()       

#----------------------------------------------------------------------------------------- 

# Enclosed Scope

# x = 10
# def fun1():
#     x = 15

#     def fun2():
#         # x = 20
#         print(x)

#     fun2() 
# fun1() 

#----------------------------------------------------------------------------------------- 

# Global Scope

# x = 10
# def fun1():
#     # x = 15

#     def fun2():
#         # x = 20
#         print(x)

#     fun2() 
# fun1()

#----------------------------------------------------------------------------------------- 

# Built-in Scope

# x = 10
# def fun1():
#     # x = 15

#     def fun2():
#         # x = 20
#         print(x)

#     fun2() 
# fun1()

# How the variable search happens in built-in scope

from math import pi

# pi = 10
def fun1():
    # pi = 15

    def fun2():
        # pi = 20
        print(pi)

    fun2() 
fun1()