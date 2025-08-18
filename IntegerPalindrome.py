# Integer Palindrome
# -----------------------------------------------------------------------------------------
# - A number is said to be a palindrome if and only if the reversal of the number is same as the original number.

# Eg:
# 121    ===>    121     ===> Int Palin
# -2002  ===>    -2002     ===> Int Palin
# 4000   ===>    4         ===> Not Palin

# n = int(input("Enter a number: "))
# temp = n
# if n < 0:
#     n = n * -1
# rev = 0 
# while n > 0:
#     rem = n%10
#     rev = (rev*10)+rem
#     n = n//10 
# if temp < 0:
#     rev = rev * -1

# if temp == rev:
#     print(f"{temp} is Interger Palindrome")
# else:
#     print(f"{temp} is Not Interger Palindrome")

def IntegerPalindrome(n):
    temp = n

    if n < 0:
        n = n * -1

    rev = 0 
    while n > 0:
        rem = n%10
        rev = (rev*10)+rem
        n = n//10 

    if temp < 0:
        rev = rev * -1

    return temp == rev

n = int(input("Enter a number: "))
I1 = IntegerPalindrome(n)
if I1:
    print("Interger Palindrome")
else:
    print("Not Interger Palindrome")

#  
# 
# 
# 

