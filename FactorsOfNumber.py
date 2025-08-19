# Factors of a number
# - A value is said to be a factor of a number  only when the vaal is able to completely reduce the number to 0.
# - All the factors of a number will always lie between 1 to the number itself
# - The least factor of a number is 1.

# WAP to print all the factors of a given number

# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     if n%i == 0:
#         print(i, end = " ")

# --------------------------------------------------------------------------------------------------------------

# WAP to print all the factors of a given number using customized function

# def factorOfNumber(n):
#     for i in range(1, n+1):
#         if n%i == 0:
#             print(i, end = " ")

# n = int(input("Enter a number: "))    
# f1 = factorOfNumber(n)    

# --------------------------------------------------------------------------------------------------------------

# WAP to print all the factors and display the count of number of factors of a given number.

# def factorOfNumber(n):
#     count = 0
#     for i in range(1, n+1):
#         if n%i == 0:
#             print(i, end = " ")
#             count+=1
#     return count            

# n = int(input("Enter a number: "))    
# f1 = factorOfNumber(n)
# print("\n")
# print(f1)

# -----------------------------------------------------------------------------------------

# WAP to print the count of cycles

# def factorOfNumber(n):

#     count = 0
#     countcycles = 0
    
#     for i in range(1, n+1):
#         if n%i == 0:
#             print(i, end = " ")
#             count+=1
#         countcycles+=1    
#     return count, countcycles          

# n = int(input("Enter a number: "))    
# resfact, rescycle = factorOfNumber(n) 
# print(f"\n The count of factors of {n} is: {resfact}")
# print(f"The count of cycles of {n} is : {rescycle}")

# Optimizing the logic to find the factors of a given number:

# --------------------------------------------------------------------------------------------------------------

# - All the factors of a given number can be listed within the direct square root or the lower nearest square root of a given number.

# WAP to count the no of factors 
# Write a program to print the no of factors of a given number
# Write a program to print the no of cycles of a given number

def Factors(n):
    i = 1
    count = 0
    countcycles = 0
    while i*i <= n:
        if n % i == 0:
            print(i, end = " ")
            count += 1
            if i != (n//i):
                print((n//i), end = " ")
                count += 1
        countcycles += 1 
        i += 1 
    return count, countcycles 

n = int(input("Enter a number: "))
resfact, rescycle = Factors(n) 
print(f"\nThe count of factors of {n} is: {resfact}")
print(f"The count of cycles of {n} is : {rescycle}")

