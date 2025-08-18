# Factors of a number
# - A value is said to be a factor of a number  only when the vaal is able to completely reduce the number to 0.
# - All the factors of a number will always lie between 1 to the number itself
# - The least factor of a number is 1.

# WAP to print all the factors of a given number

# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     if n%i == 0:
#         print(i, end = " ")

# WAP to print all the factors of a given number using customized function

# def factorOfNumber(n):
#     for i in range(1, n+1):
#         if n%i == 0:
#             print(i, end = " ")

# n = int(input("Enter a number: "))    
# f1 = factorOfNumber(n)    

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

# WAP to print the count of cycles

def factorOfNumber(n):

    count = 0
    countcycles = 0
    
    for i in range(1, n+1):
        if n%i == 0:
            print(i, end = " ")
            count+=1
        countcycles+=1    
    return count, countcycles          

n = int(input("Enter a number: "))    
f1 = factorOfNumber(n)
print("\n")
print(f1)

