# Identity Operators (is, is not):
# =====================================
# - It is used to check and compare the ID's of the given to val's that is assigned by PVM during execution time based on the memory allocation and the val's stored.
# - returns boolean val
# Syntax:        print(val1 is val2)
#                =======================
#                var_name = val1 is val2

# To check whether same memory allocation

a = 10
b = 10
c = 10
print(a == b == c)
print(a is b is c)

print("===================================================================")

s1 = "abc"
s2 = "abc"
print(s1 == s2)
print(s1 is s2)

print("===================================================================")

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2) # Checks for the Equality of the contents
print(l1 is l2) # Checks for the Memory of the contents

print("===================================================================")

