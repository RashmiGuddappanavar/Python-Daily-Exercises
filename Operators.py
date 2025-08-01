# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# 1. Arithmetic Operators - used to perform mathematical operations
# - Input: numbers (Integers or Decimals)
# - Output: numbers (Integers or Decimals)
# - Operators: +, -, *, **

# --------------------------------------------------------------------------------------------
# Addition (+)
# - With 2 or more numbers → Performs addition
# - With a single number   → Represents a positive number

print("--------------------------------------")
print(10 + 17)                        # Addition
print(23.8 + 4.9 + 7.8 + 8.5 + 0 + 9) # Addition
print(+4)                             # Represents positive number
print(+23.4)                          # Represents positive number
print("--------------------------------------")

# --------------------------------------------------------------------------------------------
# Subtraction (-)
# - With 2 or more numbers → Performs subtraction
# - With a single number   → Represents a negative number

print("--------------------------------------")
print(100 - 90 - 2)         # Subtraction
print(100.8 - 76.3 - 4.5)   # Subtraction
print(-32)                  # Represents negative number
print(-88.9)                # Represents negative number
print("--------------------------------------")

# --------------------------------------------------------------------------------------------
# Multiplication (*)
# - Requires at least 2 numbers → Performs multiplication

print("--------------------------------------")
print(5 * 8)
print(10 * 5 * 6.7 * 7)
# print(*4) # Error: '*' cannot be used with a single operand
print("--------------------------------------")

# --------------------------------------------------------------------------------------------
# Exponentiation (**)
# - Syntax: base ** power
# - Returns base raised to the power of exponent

print("--------------------------------------")
print(2 ** 3)  # 2^3 = 8
print(3 ** 2)  # 3^2 = 9
print("--------------------------------------")

# --------------------------------------------------------------------------------------------
# Division Operators

# a. Floor Division (//) - Returns integer part of quotient
print("--------------------------------------")
print(10 // 3)
print(22 // 7)
print("--------------------------------------")

# b. Float Division (/) - Returns decimal quotient
print("--------------------------------------")
print(10 / 3)
print(22 / 7)
print("--------------------------------------")

# c. Modulus (%) - Returns remainder
print("--------------------------------------")
print(10 % 3)
print(22 % 7)
print("--------------------------------------")

# Note:
# If the left number is smaller than the right number, modulus returns the left number itself
print(3 % 15)   # Output: 3
print(22 % 65)  # Output: 22
print("--------------------------------------")

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------

# Comparison Operators (<, >, <=, >=)
# - Input: values of any datatype
# - Output: Boolean value

print(25 > 23)
print((2 * 3) < (5 ** 0))
print(True >= True)
# print(False <= 'ab') # Invalid
print(False <= 35)
# print(35 <= '35')    # Invalid

# Equality Operators (==, !=)
print((5 * 2) != "abc")
# Note: >, <, etc., are not allowed between incompatible types
print("--------------------------------------")

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------

# Logical Operators (and, or, not)

print((23 > (10 ** 1)) and True and 55)
print((True ** False) and -10 and ((5 + 5) <= (2 ** 2)))

print(-3 or -5 or (10 ** 0))
print(0 or (10 % 2) or (23 > 2) and (35 <= 6))
print("--------------------------------------")

print(5 and 0)  # 5 is True, 0 is False → returns 0 (False)
print(not ((5 and 0) or (25 > 12) or (True ** 5)))
print(not (not ((35 <= 45) and (26 > 13) and (not True))))
print(not ((True or False) or (True) and (True)))
print(not ((True and False) or (False) and (True)))
print("--------------------------------------")

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# Bitwise Operators

# - Bitwise AND        (&)
# - Bitwise OR         (|)
# - Bitwise NOT        (~)
# - Bitwise XOR        (^)
# - Bitwise Left Shift (<<)
# - Bitwise Right Shift(>>)

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# Assignment Operator (=)
# - Does not return a value
# - Used to assign or copy values to variables

# Syntax:
#   Variable assignment:
#     var_name = value        e.g., a = 10
#   Variable copying:
#     var_name = other_var    e.g., z = b

print("--------------------------------------")