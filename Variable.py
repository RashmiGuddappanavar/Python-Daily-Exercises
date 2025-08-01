# Variable - Stored memory location which holds single value data (unless tuple, list, etc.)

a = 10          # 'a' stores integer value 10
b = (2 * 5)     # 'b' stores result of expression 2 * 5 → 10
c = (8 + 2)     # 'c' stores result of expression 8 + 2 → 10
d = b           # 'd' copies the value of 'b', so d = 10

# Print values of the variables
print(a)
print(b)
print(c)
print(d)

# Print memory addresses (id) of the variables
print(id(a))    # Same id for a, b, c, d since all have value 10 (immutable & interned)
print(id(b))
print(id(c))
print(id(d))

# Reassigning new value to 'd'
d = (15 + 5)    # 'd' is now reassigned to 20
print(d)
print(id(d))    # New id (since 20 is a different integer object now)

print(a == d)   # Checks equality of a and d → False (10 != 20)

# Reassigning more values to 'd'
d = 25
print(d)
print(id(d))    # id changes again

d = 45
print(d)
print(id(d))    # id changes again

# Variable 'e' updated multiple times
e = 100         # 'e' initialized with 100
print(e)
e = 200         # 'e' updated to 200
print(e)
e = 300         # 'e' updated again to 300
print(e)
print(type(e))  # Output: <class 'int'> → Latest value is 300 (int)

# Assigning multiple values to 'g' as a tuple
g = 55, 64, 90  # Tuple packing → g is now a tuple with 3 integers
print(g)
print(type(g))  # Output: <class 'tuple'>

# Another single value assignment
k = 2500        # 'k' stores integer 2500
print(k)

# Below lines are commented out because they would raise NameError if run
# print(z)          # Error: z is not defined
# a = b + y         # Error: y is not defined
# print(a)
# i = j             # Error: j is not defined
