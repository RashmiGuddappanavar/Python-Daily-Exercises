str1 = "rama"
str2 = "sita"
str3 = "ravana"
str4 = "rama"
str5 = "rama"
str6 = "sita"
str7 = "ravana"

print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)
print(str7)

# First, the Python Virtual Machine (PVM) checks in the string intern pool (Global Dictionary).
# If the string value is already present, it reuses the same memory location (no new object is created).
# If the string is not present, a new memory block is allocated.
# This behavior is called **string interning**, which helps save memory for immutable strings.
# Note: String interning applies mostly to string literals and small strings.

# The id() function returns the memory address of the object.
# The actual id values may differ every time the program is run,
# depending on Python's memory management and garbage collection.

print(id(str1))
print(id(str2))
print(id(str3))
print(id(str4))
print(id(str5))
print(id(str6))
print(id(str7))

