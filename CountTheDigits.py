# WAP to count digits in a given number

# n = int(input("Enter num: "))

# c = 0
# if n < 0: # Checking for negative num
#     n = -(n) # Or n = n * -1
# while n > 0:
#     n = n // 10
#     c += 1
# print(c)    

# WAP to count digits in a given number using customized function

def countTheDigit(n):

    if n < 0: # Checking for negative num
        n = -(n) # Or n = n * -1
    c = 0    
    while n > 0:
        n = n // 10
        c += 1
    return c

n = int(input("Enter num: "))
f1 = countTheDigit(n)
print(f1)