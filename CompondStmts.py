# Compound Statements
# +=, -=, *=, **=, //=, /=, %=

# Note: "+" and "*" operators can be used with string val's to perform string Operations. Ex: print("a" + "b") # "ab" print("a" * 2) # "aa"

print("a" + "b")
print("a" * 2)

a = 10 
b = 20 
a = a + b # a+=b
print(a)

x = 10
x = x**2 # x**=2

a = 5
a -= a # a = a - a
print(a)

x = 2
y = 2
z = 3
x *= (y*z) # x=x*(y*z)
print(x)


e = 100
e *= "10 "
e *= y #error
print(e.split(","))
print("Rashmi " * 10)

a = 10
b = 15
a = b - a

x = 2
x = ~x # Not Compound Statement
print(x) # -3

# ~ --> does not support compound stmt, because, it requires only one operand

# Rules:
# 1. It is used when the operand used on the LHS  foe operation and on LHS side for updation.
# 2. The same operand that is used on RHS operation and LHS for updation shld be loacted on the LHS of the operation stmt 

# Ex:        a = 20 
#            b = 10
#            then, 
#            a = a-b     and not, a = b - a bcz it cannot converted into compound stmts
#  - Even consrants can be part of the expressions
#  - It is compulsory to have atleast 2 operands, to form a compound stmt
#  - It is compulsory to use only initialized variables

# Note: 
# ======

# ~= is not supported as, bitwise not(~) requires only one operand to perform operation

a = 2
b = 3
c = 5
a *= (b+c)

print(a)

# x = 10 
# y = 2
# y %= x
# print(x)

